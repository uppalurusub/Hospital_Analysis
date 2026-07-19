import { useEffect, useMemo, useState } from "react";
import { useParams } from "react-router-dom";
import { modules, defaultModule } from "../config/modules";
import { dashboardEndpoints } from "../config/dashboardEndpoints";
import { fetchEndpoint } from "../api/analyticsApi";
import { apiErrorMessage } from "../api/http";
import ResponseView from "../components/ResponseView";
import DashboardView from "../components/DashboardView";
import { RefreshCw, AlertTriangle } from "lucide-react";

type DashboardItem = { endpoint: string; data?: unknown; error?: string };

export default function AnalyticsPage() {
  const { moduleId } = useParams();
  const mod = useMemo(() => modules.find(m => m.id === moduleId) ?? defaultModule, [moduleId]);
  const [ep, setEp] = useState(mod.endpoints[0]?.path ?? "");
  const [data, setData] = useState<unknown>(null);
  const [dashboard, setDashboard] = useState<DashboardItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => setEp(mod.endpoints[0]?.path ?? ""), [mod]);
  useEffect(() => { if (ep) void load(); }, [ep, mod]);

  const isDashboard = ep === "/dashboard-kpis";

  async function load() {
    setLoading(true); setError(""); setData(null); setDashboard([]);
    try {
      if (isDashboard) {
        const endpoints = dashboardEndpoints[mod.id] ?? mod.endpoints.map(e => e.path).filter(p => p !== "/dashboard-kpis" && p !== "/dashboard");
        if (!endpoints.length) throw new Error(`No JSON analytics endpoints configured for ${mod.label}`);
        const results = await Promise.all(endpoints.map(async endpoint => {
          try { return { endpoint, data: await fetchEndpoint(`${mod.prefix}${endpoint}`) }; }
          catch (e: unknown) { return { endpoint, error: apiErrorMessage(e) }; }
        }));
        setDashboard(results);
      } else {
        setData(await fetchEndpoint(`${mod.prefix}${ep}`));
      }
    } catch (e: unknown) { setError(apiErrorMessage(e)); }
    finally { setLoading(false); }
  }

  return <main className="main">
    <header className="page-head">
      <div><p className="eyebrow">Healthcare intelligence</p><h1>{mod.label}</h1>
      <p>{isDashboard ? "React-native dashboard composed from JSON analytics APIs." : "Interactive API-driven analytics with structured cards, visualizations and detailed tables."}</p></div>
      <button onClick={() => void load()}><RefreshCw size={16}/> Refresh</button>
    </header>

    <section className="endpoint-tabs">
      {mod.endpoints.map(e => <button key={e.path} className={ep === e.path ? "selected" : ""} onClick={() => setEp(e.path)}>{e.label}</button>)}
    </section>

    {loading && <div className="state">Loading analytics…</div>}
    {error && <div className="error"><AlertTriangle/><div><strong>Unable to load endpoint</strong><p>{error}</p></div></div>}
    {!loading && isDashboard && dashboard.length > 0 && <DashboardView items={dashboard}/>}
    {!loading && !isDashboard && data !== null && <ResponseView response={data}/>}
  </main>;
}
