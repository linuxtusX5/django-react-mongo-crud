import React, { useState } from "react";
import Login from "./pages/Login";
import CRUD from "./pages/CRUD";

const App: React.FC = () => {
  const [token, setToken] = useState<string | null>(null);

  return (
    <div>{!token ? <Login onLogin={setToken} /> : <CRUD token={token} />}</div>
  );
};

export default App;
