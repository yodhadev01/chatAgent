import streamlit as st
import os

from src.langgraphAgenticAi.ui.uiConfigFile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title=self.config.get_page_title(),
            layout='wide',
        )
        st.header(self.config.get_page_title())

        with st.sidebar:
            st.subheader("User Controls")
            self.user_controls['selected_llm'] = st.selectbox(
                "Select LLM",
                options=self.config.get_llm_options(),
            )

            if self.user_controls['selected_llm'] == 'Groq':

                self.user_controls['selected_groq_model'] = st.selectbox(
                    "Select Groq Model",
                    options=self.config.get_groq_model_options(),
                )
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "Enter Groq API Key",
                    type="password",
                )
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to use Groq models. Don't have? refer : https://console.groq.com/keys ")

            self.user_controls['selected_usecase'] = st.selectbox(
                "Select Use Case",
                options=self.config.get_usecase_options(),
            )
            
            if self.user_controls['selected_usecase'] == 'Chatbot With Web':
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input(
                    "Enter TAVILY API Key",
                    type="password",
                )
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY API Key to use Web Search. Don't have? refer : https://tavily.com/")

        return self.user_controls