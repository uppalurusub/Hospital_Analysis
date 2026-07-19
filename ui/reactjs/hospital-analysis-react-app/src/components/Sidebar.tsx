import { NavLink } from "react-router-dom"; 
import { modules } from "../config/modules"; 
import { HeartPulse } from "lucide-react";

export default function Sidebar()
{return <aside className="sidebar"><div className="brand"><HeartPulse/><div><strong>HealthSight</strong><span>Analytics Platform</span></div></div><nav>{modules.map(m=><NavLink key={m.id} to={`/analytics/${m.id}`} className={({isActive})=>isActive?"active":""}>{m.label}</NavLink>)}</nav></aside>}