"""
CodeOrbit Tech Internship - Project 1
Rule-Based Chatbot

A beginner-friendly chatbot that uses predefined rules and keyword matching.
No third-party packages are required.
"""

import random
import re


def normalize_text(text):
    """Convert text to lowercase and remove punctuation for easier matching."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def get_response(user_input):
    """
    Select a response using simple keyword / pattern matching.
    The order matters: more specific rules are checked before general rules.
    """
    message = normalize_text(user_input)

    if not message:
        return "I didn't receive any text. Please type something."

    # Exit rule
    if any(word in message.split() for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Thanks for chatting with me. Have a great day!"

    # Greeting rules
    if any(word in message.split() for word in ["hello", "hi", "hey", "hii", "hola"]):
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! What would you like to know?",
            "Hey! Nice to meet you."
        ])

    # Identity / introduction
    if "your name" in message or "who are you" in message:
        return "I am CodeOrbit Bot, a simple rule-based chatbot created using Python."

    if "how are you" in message:
        return "I'm doing well, thank you! How can I help you?"

    # Common questions / FAQ rules
    if "python" in message:
        return (
            "Python is a beginner-friendly programming language used for "
            "web development, automation, data science, and artificial intelligence."
        )

    if "internship" in message:
        return (
            "An internship is a learning opportunity where you gain practical "
            "experience by working on tasks or projects."
        )

    if "codeorbit" in message:
        return "CodeOrbit Tech is the organization named in this internship project."

    if "project" in message:
        return (
            "This project is a Rule-Based Chatbot. It responds to user messages "
            "using predefined keywords and if-elif logic."
        )

    if "help" in message:
        return (
            "You can ask me about Python, internships, this project, or my name. "
            "You can also say hello or bye."
        )

    if "thank" in message:
        return random.choice([
            "You're welcome!",
            "Happy to help!",
            "No problem!"
        ])

    # Fallback for unknown input
    return (
        "Sorry, I don't understand that yet. Try asking about Python, "
        "internships, projects, or type 'help'."
    )


def main():
    """Run the chatbot conversation loop."""
    print("=" * 55)
    print("        CODEORBIT TECH - RULE-BASED CHATBOT")
    print("=" * 55)
    print("Bot: Hello! I am CodeOrbit Bot.")
    print("Bot: Type 'help' to see what I can answer.")
    print("Bot: Type 'bye' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Thanks for chatting with me.")
            break

        response = get_response(user_input)
        print(f"Bot: {response}\n")

        normalized = normalize_text(user_input)
        if any(word in normalized.split() for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()
