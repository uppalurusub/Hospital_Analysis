export type JsonValue = string | number | boolean | null | JsonValue[] | { [key: string]: JsonValue };
export interface ApiEnvelope { success?: boolean; data?: JsonValue; [key: string]: JsonValue | undefined; }
export interface EndpointConfig { path: string; label: string; }
export interface ModuleConfig { id: string; label: string; prefix: string; endpoints: EndpointConfig[]; }