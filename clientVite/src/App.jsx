import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Navigation } from "./components/Navigation";
import { ClienteNuevo } from "./pages/clienteNuevo";
import { Cliente } from "./pages/cliente";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto">
        <Navigation />
        <Routes>
          {/* redirect to cliente */}
          <Route path="/" element={<Navigate to="/optica" />} />
          <Route path="/cliente" element={<Cliente />} />
          <Route path="/cliente/:rutCliente" element={<ClienteNuevo />} />
          <Route path="clienteNuevo" element={<ClienteNuevo />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
