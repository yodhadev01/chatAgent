from langgraph.graph import StateGraph, START, END

from src.langgraphAgenticAi.state.state import State
from src.langgraphAgenticAi.nodes.basicChatbotNode import BasicChatbotNode
from src.langgraphAgenticAi.tools.searchTools import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphAgenticAi.nodes.chatbotWithWeb import ChatbotWithToolNode

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
    
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        ## Define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools)

        ## Define the LLM
        model=self.model

        ## Define the chatbot node

        obj_chatbot_with_node=ChatbotWithToolNode(model)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        ## Add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        # Define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        return self.graph_builder.compile()

    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case.
        """
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()
        elif usecase == "Chatbot With Web":
            return self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")