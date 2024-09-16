import streamlit as st
import requests
import time

# Set up your Llama API key
llama_api_key = st.secrets['API_KEY']

# Function to call the Llama API and get a detailed description
def get_animal_details(animal_name):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {llama_api_key}",
        "Content-Type": "application/json"
    }
    
    # Asking for detailed information: description, features, types, size
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "user", "content": f"Describe the animal {animal_name} including its features, types, and size."}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        
        # Extracting detailed information
        details = result['choices'][0]['message']['content'] if 'choices' in result and len(result['choices']) > 0 else "Details not available."
        
        return details
    else:
        return "Sorry, I couldn't retrieve the details."

# Streamlit app setup
st.title('Detailed Animal Information')

# Get input from the user
xyz = st.text_input("Enter the name of an animal")

# Button to search
if st.button('Search'):
    # Show a spinner while generating the description
    with st.spinner('Fetching details...'):
        # Simulate delay for buffering effect
        time.sleep(2)  
        
        # Get the animal details from the Llama API
        details = get_animal_details(xyz)
        
        # Display the detailed information in a well-formatted way
        st.subheader(f"Details of {xyz.capitalize()}:")
        st.markdown(f"**Description:** {details[:200]}")  # First 200 characters for the description
        
        # Display additional information
        st.markdown(f"**Features and Size:**\n{details[200:]}")  # Remaining text for other details
