import axios from "axios";

const API = axios.create({
  baseURL: process.env.VITE_BE_API_URL,
});

export const register = (data: {
  username: string;
  email: string;
  password: string;
}) => API.post("/auth/register/", data);

export const login = (data: { username: string; password: string }) =>
  API.post("/auth/login/", data);

export const fetchItems = (token: string) =>
  API.get("/items/", {
    headers: { Authorization: `Bearer ${token}` },
  });

export const createItem = (
  token: string,
  data: { name: string; description: string }
) =>
  API.post("/items/", data, {
    headers: { Authorization: `Bearer ${token}` },
  });
