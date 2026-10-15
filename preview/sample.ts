/** Generic theme preview: functions, types, constants and parameters. */
// 中文字体回退：深蓝主题；English / 0123456789.
interface Person {
  name: string;
  age: number;
}

const LIMIT = 42;
const greeting = "Hello, Deep Blue!";
const pattern = /blue\s+sky/gi;

export function greet(person: Person, enabled = true): string {
  if (!enabled || person.age < LIMIT) {
    return `${greeting} ${person.name}\n`;
  }
  return person.name.toUpperCase();
}
