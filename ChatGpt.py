import openai
from openai_key import API_KEY

openai.api_key = API_KEY

def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def handle_message(message):
    prompt = f"User: {message}\nBot:"
    response = generate_text(prompt)
    return response

print("\033[36mWelcome to ChatGPT!\033[0m")
while True:
    try:
        user_input = input("\033[32mUser:\033[0m ")
        bot_response = handle_message(user_input)
        print("\033[34mBot:\033[0m", bot_response)
    except KeyboardInterrupt:
        print("\033[31m\nExiting...\033[0m")
        break
    except Exception as e:
        print("\033[31mError:\033[0m", str(e))
