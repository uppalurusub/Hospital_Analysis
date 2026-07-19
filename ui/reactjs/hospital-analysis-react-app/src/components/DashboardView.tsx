import KpiCard from "./KpiCard";
import ChartView from "./ChartView";
import DataTable from "./DataTable";
import MarkdownCard from "./MarkdownCard";
import { isPrimitive, titleCase, unwrap } from "../utils/formatters";

type DashboardItem = { endpoint: string; data?: any; error?: string };

const rows = (value: any): any[] => {
  const data = unwrap(value);
  if (Array.isArray(data)) return data.filter(v => v && typeof v === "object");
  if (data && typeof data === "object")
    return Object.entries(data).map(([name, value]) => ({ name, value }));
  return [];
};

export default function DashboardView({ items }: { items: DashboardItem[] }) {
  const kpis: { name: string; value: unknown }[] = [];
  const sections: { endpoint: string; data: any }[] = [];

  for (const item of items) {
    if (item.error) continue;
    const data = unwrap(item.data);
    if (isPrimitive(data)) {
      kpis.push({ name: item.endpoint, value: data });
      continue;
    }
    if (data && typeof data === "object" && !Array.isArray(data)) {
      const primitiveEntries = Object.entries(data).filter(([, v]) => isPrimitive(v));
      if (primitiveEntries.length && primitiveEntries.length <= 8) {
        primitiveEntries.forEach(([name, value]) => kpis.push({ name, value }));
        const complex = Object.fromEntries(Object.entries(data).filter(([, v]) => !isPrimitive(v)));
        if (Object.keys(complex).length) sections.push({ endpoint: item.endpoint, data: complex });
        continue;
      }
    }
    sections.push({ endpoint: item.endpoint, data });
  }

  return <div className="dashboard-view">
    {kpis.length > 0 && <div className="kpi-grid">{kpis.map((k, i) => <KpiCard key={`${k.name}-${i}`} name={k.name} value={k.value}/>)}</div>}
    <div className="dashboard-grid">
      {sections.map(({ endpoint, data }) => {
        const chartRows = rows(data);
        if (typeof data === "string") return <MarkdownCard key={endpoint} title={titleCase(endpoint)} text={data}/>;
        return <div className="dashboard-section" key={endpoint}>
          <ChartView title={endpoint} data={chartRows}/>
          <DataTable title={`${endpoint} details`} rows={chartRows}/>
        </div>;
      })}
    </div>
  </div>;
}
