import streamlit as st
import openai

# Initialize OpenAI API key from secrets
openai.api_key = st.secrets["openai_key"]

# Set Title
st.title("📝 File Q&A with ChatGPT")

# Upload the file
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))

# Text input
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file
)

if uploaded_file and question:
    # Parsing the text
    article = uploaded_file.read().decode()

    # Prompting
    my_prompt = f"Here's an article: {article}\n\n{question}"

    # ChatGPT Connection and API call
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": my_prompt}
            ]
        )

        # Display the response
        st.write("### Answer")
        st.write(response.choices[0]["message"]["content"])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
