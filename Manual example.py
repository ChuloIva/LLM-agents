from openai import OpenAI
import sys

# ANSI escape code for coloring the response
RESPONSE_COLOR = '\033[94m'  # Blue color
END_COLOR = '\033[0m'  # Reset to default color

# Set up the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# Initial messages to start the conversation
initial_messages = [
    {"role": "system", "content": "Respond concisely, within 150 tokens. After each answer, include a question to facilitate ongoing dialogue."},
    {"role": "user", "content": "What's elon Musk famous for?"}
]


# Function to create and get a completion from the OpenAI API
def get_completion(messages):
    completion = client.chat.completions.create(
        model="local-model",
        messages=messages,
        temperature=0.7,
        max_tokens=250,
    )
    return completion.choices[0].message.content  # Accessing the content directly

# Main loop
try:
    current_messages = initial_messages
    while True:
        # Get response from the model
        response = get_completion(current_messages)
        formatted_response = response.replace("\\n", "\n")
        print(RESPONSE_COLOR + formatted_response + END_COLOR)

        # Check for user input to continue or break
        user_input = input("Press 'C' to stop or any other key to continue: ")
        if user_input.lower() == 'c':
            break

        # Update the messages for the next iteration
        current_messages.append({"role": "user", "content": response})
except KeyboardInterrupt:
    print("\nProcess interrupted by the user.")
except Exception as e:
    print(f"An error occurred: {e}")
