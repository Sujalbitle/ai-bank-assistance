import streamlit as st
import time
from rag_engine import get_rag_chain

st.set_page_config(page_title="AI Banking Assistant", page_icon="🏦")

st.title("🏦 AI Banking Assistant")
st.markdown("Ask me anything about our accounts, loans, or policies!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Get the RAG chain (cached ideally, but re-initializing for simplicity here)
            # In a production app, use @st.cache_resource for the chain setup
            with st.spinner("Thinking..."):
                chain = get_rag_chain()
                result = chain.invoke(prompt)
                answer = result['result']
            
            # Simulate typing effect
            for chunk in answer.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        except Exception as e:
            full_response = f"I encountered an error: {str(e)}"
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
