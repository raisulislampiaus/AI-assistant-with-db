
import React, { useState } from "react";
import ChatWindow from "./components/ChatWindow";
import ChatInput from "./components/ChatInput";
import Loader from "./components/Loader";

const App = () => {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (query) => {
    const userMessage = { sender: "user", content: query };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      const botMessage = { sender: "bot", content: data.response };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [...prev, { sender: "bot", content: "Error occurred!" }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <ChatWindow messages={messages} />
      {loading && <Loader />}
      <ChatInput onSend={handleSend} />
    </div>
  );
};

export default App;
