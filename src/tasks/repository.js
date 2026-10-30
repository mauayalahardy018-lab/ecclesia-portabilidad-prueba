// El proyecto destino aporta una conexión o pool configurado.
let database;
export function useDatabase(client) {
  database = client;
}

export async function insertTask(input) {
  if (!database) throw new Error("Conecta el repositorio al pool del proyecto");
  const result = await database.query("INSERT INTO tasks(title) VALUES($1) RETURNING id,title", [input.title]);
  return result.rows[0];
}
