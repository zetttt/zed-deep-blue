// Generic JavaScript preview; no external services.
const LIMIT = 42;
const names = ["Ada", "Lin"];
export function welcome(name, enabled = true) {
  if (!enabled) return null;
  return { message: `Hello ${name}`, count: LIMIT };
}
names.map((name) => welcome(name));
