import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";

const API_URL = process.env.REACT_APP_API_URL || "https://affiliate-marketing-bot.onrender.com";

function App() {
  const [deals, setDeals] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/deals`)
      .then((res) => res.json())
      .then(setDeals)
      .catch((err) => console.error("Error fetching deals:", err));
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>🔥 Affiliate Deals</h1>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Title</th>
            <th>Price</th>
            <th>Affiliate Link</th>
          </tr>
        </thead>
        <tbody>
          {deals.map((deal, i) => (
            <tr key={i}>
              <td>{deal.title}</td>
              <td>${deal.price}</td>
              <td>
                <a href={deal.affiliate_link} target="_blank" rel="noreferrer">
                  View Deal
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
