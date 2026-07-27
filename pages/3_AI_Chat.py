import streamlit as st
import plotly.express as px
from utils.helpers import load_css, render_header, get_current_dataset
from utils.chatbot import LocalAIAssistant

st.set_page_config(page_title="Keyless AI Assistant", layout="wide")
load_css()

render_header("Keyless AI Assistant", "Ask questions about your data locally without requiring any API keys.")

df = get_current_dataset()

if df is None:
    st.warning("Please upload a dataset on the Dataset page first.")
else:
    assistant = LocalAIAssistant(df)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "code" in message:
                st.code(message["code"], language="python")

    # Accept user input
    if prompt := st.chat_input("Ask something (e.g., 'What is the average price?', 'Find missing values', 'Which category has highest sales?')"):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response using local logic
        response = assistant.parse_query(prompt)

        with st.chat_message("assistant"):
            st.markdown(response["text"])
            if response.get("code"):
                st.code(response["code"], language="python")

            if response.get("chart_type") == "bar":
                fig = px.bar(response["data"], x=response["x"], y=response["y"], template="plotly_dark", color_discrete_sequence=["#7C3AED"])
                st.plotly_chart(fig, use_container_width=True)

        st.session_state.messages.append({
            "role": "assistant", 
            "content": response["text"],
            "code": response.get("code")
        })
