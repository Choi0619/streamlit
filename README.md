## AI-Powered Animal Description Web App

This project is a simple AI-powered web app that generates detailed descriptions of animals using the **Llama API**. It is built using **Streamlit**, a Python-based framework for creating interactive web applications.

### How It Works

1. The user inputs the name of an animal.
2. The app queries the **Llama API**, asking for a description of the animal, including its features, types, and size.
3. The app displays the information in a user-friendly format, with a **description** and **additional details** (features and size) presented separately.

### Key Technologies

- **Streamlit**: Enables a quick and easy web app interface.
- **Llama API**: Provides AI-driven detailed descriptions of animals.

### Usage

- **Llama API Key**: Users need to obtain their own **Llama API key** and add it to the `st.secrets['API_KEY']` configuration in the code.
- **Live URL**: You can access the live version of this project at the following URL:  
  [Live URL](https://app-8tywqga4ja4uvnhvfpsdgj.streamlit.app/)

### Features

- **Animal Descriptions**: Provides a concise description of any animal entered by the user.
- **Detailed Information**: In addition to descriptions, the app displays key features and size details.
