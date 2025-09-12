import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Index from "./pages/Signup";
import PublicRoute from "./components/PublicRoute";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";

import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route
          path="/signup/login"
          element={
            <PublicRoute>
              <Index />
            </PublicRoute>
          }
        />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
