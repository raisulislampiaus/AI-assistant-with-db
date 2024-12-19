import React from "react";

const ChatWindow = ({ messages }) => {
  return (
    <div className="chat-window">
      {messages.map((message, index) => (
        <div
          key={index}
          className={`message ${message.sender === "user" ? "user-message" : "bot-message"}`}
        >
          {message.content}
        </div>
      ))}
    </div>
  );
};

export default ChatWindow;
