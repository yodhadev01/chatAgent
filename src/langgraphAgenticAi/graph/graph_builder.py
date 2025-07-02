from langgraph.graph import StateGraph, START, END

from src.langgraphAgenticAi.state.state import State
from src.langgraphAgenticAi.nodes.basicChatbotNode import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph with the given model.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.model)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge('chatbot',END)

        return self.graph_builder.compile()
    
    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case.
        """
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")