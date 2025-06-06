import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="YOUR_API_KEY_HERE"  # Replace this with your actual API key
)

def generate_code_with_chatbot(input_message):
    # Send a request to the Mistral AI model
    completion = client.chat.completions.create(
        model="mistralai/mistral-large",
        messages=[{"role": "user", "content": input_message}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )

    # Collect the generated Python code
    generated_code = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            generated_code += chunk.choices[0].delta.content

    return generated_code

# Streamlit app
def main():
    st.title("Kiki Code Generator")
    st.write("This chatbot generates Python code based on your input.")

    # Text input for user messages
    user_input = st.text_input("Type here:", "")

    # Button to send user message and generate code
    if st.button("Send"):
        with st.spinner("Generating code..."):
            generated_code = generate_code_with_chatbot(user_input)

        # Display the generated Python code
        st.code(generated_code, language='python')

if __name__ == "__main__":
    main()
