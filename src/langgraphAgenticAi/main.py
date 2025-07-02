import streamlit as st

from src.langgraphAgenticAi.ui.loadUi import LoadStreamlitUI
from src.langgraphAgenticAi.llms.groqllm import GroqLLM
from src.langgraphAgenticAi.graph.graph_builder import GraphBuilder
from src.langgraphAgenticAi.ui.displayResult import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """
    try:
        # Initialize the Streamlit UI
        ui = LoadStreamlitUI()
        user_input = ui.load_streamlit_ui()

        if not user_input:
            st.error("Failed to load user controls. Please check your configuration.")
            return
        
        user_message = st.chat_input("Enter your message here...")

        if user_message:
            try:
                # Configure the LLM model
                obj_llm_config = GroqLLM(user_control_input=user_input)
                model = obj_llm_config.get_llm_model()

                if not model:
                    st.error("Failed to initialize the LLM model. Please check your API key and model selection.")
                    return
                
                usecase = user_input.get("selected_usecase")

                if not usecase:
                    st.error("No use case selected. Please select a use case to proceed.")
                    return
                
                graph_builder = GraphBuilder(model)

                try:
                    
                    graph = graph_builder.setup_graph(usecase)
                    print(user_message)
                    DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()

                except ValueError as ve:
                    st.error(f"Error setting up the graph: {ve}")
                    return

            except Exception as e:
                st.error(f"Failed to configure the LLM model: {e}")
                return
    except Exception as e:
        st.error(f"An error occurred: {e}")