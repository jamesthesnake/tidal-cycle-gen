import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

def ask_gpt(question):
    # Define the ChatGPT model
    model = "gpt-3.5-turbo"

    # Generate a response using ChatGPT
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )

    # Extract and print the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    print("Assistant: ", assistant_reply)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        ask_gpt(user_input)
