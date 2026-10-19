const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");
const sendButton = document.getElementById("send-button");

if (form && input && messages && sendButton) {

    function addMessage(text, sender) {
        const message = document.createElement("div");
        message.className = `message ${sender}`;

        const bubble = document.createElement("div");
        bubble.className = "bubble";

        // Safely display text without executing HTML.
        bubble.textContent = text;

        message.appendChild(bubble);
        messages.appendChild(message);
        messages.scrollTop = messages.scrollHeight;

        return message;
    }

    async function sendMessage(text) {
        const question = text.trim();

        if (!question || sendButton.disabled) {
            return;
        }

        addMessage(question, "user");
        input.value = "";
        sendButton.disabled = true;
        input.disabled = true;

        const loadingMessage = addMessage(
            "CampusAI is thinking...",
            "bot"
        );

        try {
            const response = await fetch("/api/chatbot", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: question
                })
            });

            const data = await response.json();

            if (!response.ok || !data.success) {
                throw new Error(
                    data.reply || "Unable to get an answer."
                );
            }

            loadingMessage.querySelector(".bubble").textContent =
                data.reply || "Sorry, I couldn't generate a response.";

        } catch (error) {
            loadingMessage.querySelector(".bubble").textContent =
                error.message ||
                "Unable to connect. Please try again.";

            console.error("CampusAI error:", error);

        } finally {
            sendButton.disabled = false;
            input.disabled = false;
            input.focus();
            messages.scrollTop = messages.scrollHeight;
        }
    }

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        sendMessage(input.value);
    });

    document.querySelectorAll("[data-question]").forEach((button) => {
        button.addEventListener("click", () => {
            sendMessage(button.dataset.question);
        });
    });

} else {
    console.error(
        "Chatbot elements are missing. Check chatbot.html IDs."
    );
}
