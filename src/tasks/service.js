import { insertTask } from "./repository.js";

export function normalizeTitle(title) {
  const normalized = title.trim().replace(/\s+/g, " ");
  if (normalized.length < 3) throw new Error("Título demasiado corto");
  return normalized;
}

export function createTask(input) {
  return insertTask({ title: normalizeTitle(input.title) });
}
