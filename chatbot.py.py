import re
import sys

# Define knowledge base and intent patterns
INTENTS = [
    {
        "intent": "business_hours",
        "patterns": [r"\bhours\b", r"\btiming\b", r"\bopen\b", r"\bwhen are you open\b", r"\bwork hours\b"],
        "response": "🕒 Our standard support hours are Monday to Friday, 9:00 AM to 6:00 PM IST."
    },
    {
        "intent": "product_faqs",
        "patterns": [r"\bpricing\b", r"\bcost\b", r"\bplans\b", r"\bfee\b", r"\bprice\b"],
        "response": "💰 Our internships and basic platform evaluations feature zero enrollment fees! Check our catalog for advanced enterprise solutions."
    },
    {
        "intent": "contact_support",
        "patterns": [r"\bcontact\b", r"\bemail\b", r"\bsupport\b", r"\bhelp\b", r"\btalk to human\b"],
        "response": "📧 You can reach out directly to our technical support team at hello@datheon.in."
    },
    {
        "intent": "services",
        "patterns": [r"\bservices\b", r"\bwhat do you do\b", r"\bofferings\b", r"\bstudio\b"],
        "response": "🚀 Datheon is an AI engineering studio specializing in Voice AI Agents, Workflow Automation, AI-Native SaaS, and Knowledge AI systems."
    }
]

FALLBACK_RESPONSES = [
    "🤔 I'm not quite sure I understand your query. Could you rephrase or ask about our business hours, services, pricing, or support?",
    "🤖 Hmm, that's beyond my current rule set. Try asking about our support email or operating hours!",
    "⚠️ I didn't catch that. Type 'help' to see what you can ask me."
]

def run_chatbot():
    print("=" * 60)
    print("🤖 Welcome to Datheon Rule-Based Terminal Assistant!")
    print("Type your questions below. Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 60)
    
    # State management: greeting -> active conversation
    print("Bot: Hello! How can I assist you with Datheon systems and programs today?\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye! Have a great day!")
            break

        if not user_input:
            continue

        normalized_input = user_input.lower()

        # Exit commands check
        if normalized_input in ['bye', 'exit', 'quit']:
            print("Bot: Goodbye! Thank you for chatting with Datheon Support. Have a great day! 👋")
            break

        # Match intents using Regex
        matched = False
        for intent in INTENTS:
            for pattern in intent["patterns"]:
                if re.search(pattern, normalized_input):
                    print(f"Bot: {intent['response']}\n")
                    matched = True
                    break
            if matched:
                break

        # Fallback response if no regex matched
        if not matched:
            import random
            print(f"Bot: {random.choice(FALLBACK_RESPONSES)}\n")

if __name__ == "__main__":
    run_chatbot()