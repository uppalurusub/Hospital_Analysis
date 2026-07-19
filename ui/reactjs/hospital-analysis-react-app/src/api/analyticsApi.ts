import axios from "axios";
import { API_BASE_URL, http } from "./http";

const candidates = (path: string) => {
  const clean = path.startsWith("/") ? path : `/${path}`;
  return /\/api$/i.test(API_BASE_URL) ? [clean] : [`/api${clean}`, clean];
};

async function withPrefixFallback<T>(path: string, request: (candidate: string) => Promise<T>): Promise<T> {
  let lastError: unknown;
  for (const candidate of candidates(path)) {
    try { return await request(candidate); }
    catch (error) {
      lastError = error;
      if (!axios.isAxiosError(error) || error.response?.status !== 404) throw error;
    }
  }
  throw lastError;
}

export async function fetchEndpoint(path: string) {
  return withPrefixFallback(path, async candidate => {
    const response = await http.get(candidate, { responseType: "json" });
    return response.data;
  });
}
