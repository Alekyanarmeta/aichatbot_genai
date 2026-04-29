async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;

    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    // show user message
    chatBox.innerHTML += `<div class="user">You: ${message}</div>`;
    input.value = "";

    // send request to backend
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // show bot response
    chatBox.innerHTML += `<div class="bot">Bot: ${data.response}</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;
}