import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="flex justify-between py-3 items-center">
      <button className="bg-indigo-500 p-3 rounded-lg">
        <Link to="/Cliente">Clientes</Link>
      </button>

      <button className="bg-indigo-500 p-3 rounded-lg">
        <Link to="/ClienteNuevo">Crear Cliente</Link>
      </button>
    </div>
  );
}
