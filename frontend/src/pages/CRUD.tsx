import { useState, useEffect } from "react";
import { fetchItems, createItem } from "../api";

interface Item {
  id: string;
  name: string;
  description: string;
}

const CRUD: React.FC<{ token: string }> = ({ token }) => {
  const [items, setItems] = useState<Item[]>([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const loadItems = async () => {
    const res = await fetchItems(token);
    setItems(res.data);
  };

  const addItem = async () => {
    await createItem(token, { name, description });
    setName("");
    setDescription("");
    loadItems();
  };

  useEffect(() => {
    loadItems();
  }, []);

  return (
    <div>
      <h1>My Items</h1>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <input
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Description"
      />
      <button onClick={addItem}>Add Item</button>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name}: {item.description}
          </li>
        ))}
      </ul>
    </div>
  );
};
export default CRUD;
