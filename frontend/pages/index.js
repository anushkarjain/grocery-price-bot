import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [list, setList] = useState("");
  const [prices, setPrices] = useState(null);

  const fetchPrices = async () => {
    const items = list.split(",");
    const response = await axios.post("http://127.0.0.1:8000/compare-prices", { grocery_list: items });
    setPrices(response.data.data);
  };

  return (
    <div className="container">
      <h1>Compare Grocery Prices</h1>
      <input type="text" value={list} onChange={(e) => setList(e.target.value)} placeholder="Enter items (comma-separated)" />
      <button onClick={fetchPrices}>Compare</button>

      {prices && (
        <div>
          {Object.entries(prices).map(([item, details]) => (
            <p key={item}>{item}: {details.price} ({details.store})</p>
          ))}
        </div>
      )}
    </div>
  );
}
