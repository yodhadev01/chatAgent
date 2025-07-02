import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_control_input["GROQ_API_KEY"]
            if not groq_api_key:
                st.error("Groq API Key is required to use Groq models.")
            
            model_name = self.user_control_input["selected_groq_model"]
            llm = ChatGroq(
                model=model_name,
                api_key=groq_api_key,
            )
            return llm
        
        except Exception as e:
            st.error(f"Error initializing Groq LLM: {e}")
            return None