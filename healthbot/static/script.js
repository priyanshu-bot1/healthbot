async function sendMessage() {
    let input = document.getElementById("userInput");
    let question = input.value.trim();
    if (question === "") return;

    addMessage(question, "user-msg");
    input.value = "";
    scrollChat();

    showTyping(true);

    let response = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: question})
    });

    let data = await response.json();

    showTyping(false);

    addMessage(data.answer, "bot-msg");
    scrollChat();
}


function addMessage(text, className) {
    let chatbox = document.getElementById("chatbox");
    let msg = document.createElement("div");
    msg.classList.add("message", className);
    msg.innerText = text;
    chatbox.appendChild(msg);
}

function scrollChat() {
    let chatbox = document.getElementById("chatbox");
    chatbox.scrollTop = chatbox.scrollHeight;
}


function showTyping(show) {
    document.getElementById("typing").classList.toggle("hidden", !show);
}


function checkEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
