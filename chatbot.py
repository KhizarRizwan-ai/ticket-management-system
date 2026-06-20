import os
from dotenv import load_dotenv
import requests
import json

class SimpleChatbot:
    """A simple chatbot with conversation memory"""
    
    def __init__(self, system_prompt="You are a helpful assistant."):
        """Set up the chatbot"""
        # This loads the .env file
        load_dotenv()
        
        # This grabs the key from inside the .env file
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        # We are using the free Llama model so it works right away
        self.model = "openai/gpt-4o-mini"
        
        # Start history with the system prompt
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
    
    def chat(self, user_message):
        """Send a message and get a response"""
        
        # Add your message to the history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Send everything to OpenRouter
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json", 
            },
            data=json.dumps({
                "model": self.model,
                "messages": self.conversation_history
            })
        )
        
        response_data = response.json()

        # 3. Check for errors from OpenRouter
        if "error" in response_data:
            error_message = response_data["error"].get("message", "Unknown error")
            return f"Error: {error_message}"

        # 4. If no error, get the AI's answer
        if "choices" in response_data:
            assistant_message = response_data["choices"][0]["message"]["content"]
            
            # Add the AI's answer to the history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            return assistant_message
            
        return "Sorry, I did not get a valid response."
    
    def get_history(self):
        """Return the conversation history"""
        return self.conversation_history
    
    def clear_history(self, keep_system=True):
        """Clear the history to start over"""
        if keep_system and self.conversation_history:
            system_msg = self.conversation_history[0]
            self.conversation_history = [system_msg]
        else:
            self.conversation_history = []


def main():
    """Run the chatbot"""
    
    # Create the chatbot
    chatbot = SimpleChatbot(
        system_prompt="You are a friendly Python programming tutor. Keep responses short."
    )
    
    print("Chatbot: Hello! I am your Python tutor. Ask me anything!")
    print("(Type 'quit' to exit, 'history' to see past messages, 'clear' to reset)\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Happy coding!")
            break
        
        if user_input.lower() == 'history':
            print("\n=== Conversation History ===")
            for msg in chatbot.get_history():
                role = msg['role'].capitalize()
                content = msg['content']
                print(f"{role}: {content}")
                print("-" * 50)
            print("============================\n")
            continue
        
        if user_input.lower() == 'clear':
            chatbot.clear_history()
            print("Chatbot: Memory cleared! Let's start fresh.\n")
            continue
        
        if not user_input:
            continue
        
        try:
            # Get the chatbot's answer and print it
            response = chatbot.chat(user_input)
            print(f"Chatbot: {response}\n")
        except Exception as e:
            print(f"Code Error: {e}\n")


if __name__ == "__main__":
    main()
        