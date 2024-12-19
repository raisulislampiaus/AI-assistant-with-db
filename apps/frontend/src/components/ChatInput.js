// import React, { useState } from "react";

// const ChatInput = ({ onSend }) => {
//   const [query, setQuery] = useState("");

//   const handleSend = () => {
//     if (query.trim()) {
//       onSend(query);
//       setQuery("");
//     }
//   };

//   return (
//     <div className="input-container">
//       <input
//         type="text"
//         value={query}
//         onChange={(e) => setQuery(e.target.value)}
//         placeholder="Type your query..."
//         className="chat-input"
//       />
//       <button onClick={handleSend} className="send-button">
//         Send
//       </button>
//     </div>
//   );
// };

// export default ChatInput;
// import React, { useState } from "react";

// const ChatInput = ({ onSend }) => {
//   const [input, setInput] = useState("");

//   const handleVoiceInput = () => {
//     // Check if SpeechRecognition is supported
//     const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

//     if (!SpeechRecognition) {
//       alert("Your browser does not support Speech Recognition.");
//       return;
//     }

//     const recognition = new SpeechRecognition();
//     recognition.lang = "en-US";
//     recognition.interimResults = false;

//     recognition.onstart = () => {
//       console.log("Voice recognition started. Speak into the microphone.");
//     };

//     recognition.onresult = (event) => {
//       const transcript = event.results[0][0].transcript;
//       console.log("Transcript:", transcript);
//       setInput(transcript); // Set the transcript to the input field
//       onSend(transcript); // Send the transcript as a message
//     };

//     recognition.onerror = (event) => {
//       console.error("Speech recognition error:", event.error);
//       alert("Error during speech recognition. Please try again.");
//     };

//     recognition.onend = () => {
//       console.log("Voice recognition ended.");
//     };

//     recognition.start();
//   };

//   const handleSend = () => {
//     if (input.trim()) {
//       onSend(input.trim());
//       setInput("");
//     }
//   };

//   return (
//     <div className="chat-input">
//       <input
//         type="text"
//         value={input}
//         onChange={(e) => setInput(e.target.value)}
//         placeholder="Type your message here..."
//       />
//       <button onClick={handleSend}>Send</button>
//       <button onClick={handleVoiceInput}>🎤 Speak</button>
//     </div>
//   );
// };

// export default ChatInput;
import React, { useState } from "react";
import { TextField, IconButton, Box } from "@mui/material";
import MicIcon from "@mui/icons-material/Mic";
import SendIcon from "@mui/icons-material/Send";

const ChatInput = ({ onSend }) => {
  const [input, setInput] = useState("");

  const handleVoiceInput = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Your browser does not support Speech Recognition.");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript);
      onSend(transcript);
    };

    recognition.onerror = () =>
      alert("Error occurred during speech recognition.");
    recognition.start();
  };

  const handleSend = () => {
    if (input.trim()) {
      onSend(input.trim());
      setInput("");
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        alignItems: "center",
        border: "1px solid #ddd",
        borderRadius: "50px",
        padding: "2px 8px",
        boxShadow: "0 1px 3px rgba(0, 0, 0, 0.1)",
        backgroundColor: "#fff",
      }}
    >
      <IconButton onClick={handleVoiceInput} color="default">
        <MicIcon sx={{ color: "gray" }} />
      </IconButton>

      <TextField
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type Message"
        variant="standard"
        InputProps={{
          disableUnderline: true,
          style: { marginLeft: 8, flex: 1, fontSize: "14px" },
        }}
        sx={{ flex: 1 }}
      />

      <IconButton onClick={handleSend} color="primary">
        <SendIcon />
      </IconButton>
    </Box>
  );
};

export default ChatInput;
