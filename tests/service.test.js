import { expect, it } from "vitest";
import { normalizeTitle } from "../src/tasks/service.js";

it("normaliza un título antes de guardarlo", () => {
  expect(normalizeTitle("  Preparar   informe  ")).toBe("Preparar informe");
  expect(() => normalizeTitle(" x ")).toThrow("Título demasiado corto");
});
