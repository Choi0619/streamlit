import streamlit as st
import requests

# Set up your Llama API key
llama_api_key = st.secrets['API_KEY']

# Function to call the Llama API and get a description
def get_animal_description(animal_name):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {llama_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "user", "content": f"Describe the animal {animal_name} in under 100 characters."}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "Sorry, I couldn't find a description."

# Streamlit app setup
st.title('Animal Description')

# Get input from the user
xyz = st.text_input("Enter the name of an animal")

# Button to search
if st.button('Search'):
    # Get the animal description from the Llama API
    description = get_animal_description(xyz)
    st.write(f"Description of {xyz}: {description}")
