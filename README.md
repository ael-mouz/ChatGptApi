# ChatGPT

ChatGPT is a Python-based chatbot that uses OpenAI's GPT-3 API to generate responses to user messages.

## Setup

1. Install the required packages using `pip`:

```bash
  pip install openai
```

2. Set up your OpenAI API key by replacing the `api_key` variable in the code with your actual API key .

```python
  API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
```
3. To get the OpenAI API key key [Visit OpenAI's website](https://platform.openai.com/account/api-keys "OpenAI Website")

## Usage

1. Run the `chatgpt.py` file to start the chatbot by `python3 chatgpt.py`.
2. Enter your messages as a user to simulate a conversation with the chatbot.
3. The chatbot will generate responses using GPT-3 based on the input messages and print them in different colors:
  - User input: Green
  - Bot response: Blue
  - Error message: Red

## Additional Features

- Error Handling: The code includes basic error handling for exceptions that may occur during API calls.

