from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represents the state of the LangGraph AgenticAI application.
    This state is used to manage the conversation history and other relevant data.
    """
    messages: Annotated[list, add_messages]  # List of messages in the conversation
    user_input: str       # User input message
    model: str            # Model used for generating responses
    usecase: str          # Selected use case for the application
    page_description: str # Description of the page
    page_title: str       # Title of the page