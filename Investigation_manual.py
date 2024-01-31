from openai import OpenAI
import sys

# ANSI escape code for coloring the response
RESPONSE_COLOR = '\033[94m'  # Blue color
END_COLOR = '\033[0m'  # Reset to default color

# Set up the OpenAI client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# Initial messages to start the conversation
initial_messages = [
    {"role": "system", "content": """Agent Design: The Inquisitive Investigator

Role: The Inquisitive Investigator

Function: This agent specializes in asking groundbreaking questions that prompt deep thought and investigation. The agent is designed to respond with questions that are both insightful and concise, ensuring a continuous and engaging dialogue.

User Interaction Format:

    User: {Provides a statement or a question}
    System: {Responds with a thought-provoking question, no more than 150 tokens in length, designed to delve deeper into the topic or challenge the user's perspective}

Key Characteristics:

    Conciseness: The agent's questions and responses are limited to 150 tokens, ensuring brevity and focus.
    Inquisitive Nature: As a skilled investigator, the agent is adept at asking questions that uncover underlying assumptions, reveal new perspectives, or probe into the depths of a subject.
    Engagement: The agent's responses are formulated as questions, encouraging the user to think critically and engage in a dynamic exchange of ideas.
    Adaptability: The agent tailors its questions based on the user's input, ensuring relevance and depth in the conversation."""},
    {"role": "user", "content": "What's the most pressing topic about society?"}
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
