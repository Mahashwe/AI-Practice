import streamlit as st
import requests
import json
from datetime import datetime

# Page config
st.set_page_config(page_title="Gemini Chat", layout="wide", initial_sidebar_state="expanded")

# Styling
st.markdown("""
    <style>
    .chat-message {
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 10px;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #1f77b4;
        color: white;
        align-items: flex-end;
    }
    .assistant-message {
        background-color: #e8e8e8;
        color: black;
        align-items: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# API configuration
API_URL = "http://localhost:8000/api/query/"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("🤖 Gemini Chat Interface")
st.markdown("Chat with Gemini Flash 2.0 AI powered by Django API")

# Sidebar
with st.sidebar:
    st.subheader("⚙️ Settings")
    api_endpoint = st.text_input("API Endpoint", API_URL, help="Your Django API endpoint")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.subheader("📊 Chat Stats")
    st.metric("Total Messages", len(st.session_state.messages))
    
    st.divider()
    st.subheader("ℹ️ Info")
    st.info("""
    **Model:** Gemini Flash 2.0
    
    **Features:**
    - Real-time chat
    - Message history
    - Django backend integration
    """)

# Main chat display
st.subheader("💬 Chat")
chat_container = st.container(height=400, border=True)

with chat_container:
    if len(st.session_state.messages) == 0:
        st.markdown("### Welcome! 👋")
        st.markdown("Start chatting with Gemini. Your messages will appear here.")
    else:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>You:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message assistant-message">
                    <strong>Gemini:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)

# Input area
st.divider()
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input("Type your message...", placeholder="Ask me anything...", label_visibility="collapsed")

with col2:
    send_button = st.button("Send", use_container_width=True, type="primary")

# Handle message sending
if send_button and user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Show loading indicator
    with st.spinner("Getting response from Gemini..."):
        try:
            # Send to API
            payload = {"prompt": user_input}
            response = requests.post(api_endpoint, json=payload, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            assistant_response = data.get("response", "No response received")
            
            # Add assistant response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_response,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            })
            
            st.success("✅ Response received!")
            st.rerun()
            
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to Django API. Make sure the server is running at " + api_endpoint)
        except requests.exceptions.Timeout:
            st.error("❌ Request timeout. The API took too long to respond.")
        except requests.exceptions.HTTPError as e:
            st.error(f"❌ API Error: {e.response.status_code} - {e.response.text}")
        except json.JSONDecodeError:
            st.error("❌ Invalid JSON response from API")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Footer
st.divider()
st.caption("💡 Tip: Make sure your Django server is running on localhost:8000")
