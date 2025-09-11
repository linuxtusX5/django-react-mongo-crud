import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import CRUD from "./pages/CRUD";

function App() {
  const handleLogin = (token: string) => {
    // Handle login logic, e.g., save token to state or localStorage
    console.log("Logged in with token:", token);
  };

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={<CRUD token="" />} />
      </Routes>
    </Router>
  );
}

export default App;
