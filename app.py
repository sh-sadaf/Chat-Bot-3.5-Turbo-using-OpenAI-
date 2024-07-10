import streamlit as st
import openai
import toml

# Load secrets from the secrets.toml file
# secrets = toml.load("streamlit/secrets.toml")
openai.api_key = secrets["OPENAI_API_KEY"]

st.title("ChatGPT-like Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}]
    )
    message = response['choices'][0]['message']['content'].strip()
    return message

st.header("Chat with the bot")
user_input = st.text_input("You: ", "")

if user_input:
    st.session_state.messages.append(f"You: {user_input}")
    bot_response = generate_response(user_input)
    st.session_state.messages.append(f"Bot: {bot_response}")

for message in st.session_state.messages:
    st.write(message)
