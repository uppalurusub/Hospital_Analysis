import axios, { AxiosError } from "axios";

export const API_BASE_URL =
  (import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000").replace(/\/$/, "");

export const http = axios.create({
  baseURL: API_BASE_URL,
  timeout: 120000,
});

http.interceptors.response.use(
  response => response,
  error => {
    const e = error as AxiosError<{ detail?: string }>;
    return Promise.reject(e);
  }
);

export function apiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const detail = error.response?.data?.detail;
    const status = error.response?.status;
    const url = `${error.config?.baseURL ?? ""}${error.config?.url ?? ""}`;
    return detail
      ? `${status ?? ""} ${detail} — ${url}`.trim()
      : `${status ?? "API"} request failed — ${url}`;
  }
  return error instanceof Error ? error.message : "API request failed";
}
