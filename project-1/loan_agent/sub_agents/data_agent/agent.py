from google.adk.agents import Agent
from tools.tool import fetch_customer_data_tool, retrieve_policy_tool

fetch_customer_data_agent = Agent(
    name="fetch_customer_data_agent",
    model="gemini-2.0-flash",   
    description="Fetch customer data from local Excel based on ID",
    instruction="you are an agent to fetch user data"
                "ask user for the user id "
                "use the tool 'fetch_customer_data_tool' by passing the userid.",
    output_key="customer_data",
    tools=[fetch_customer_data_tool],
   
)

# --- ToolAgent: setup and retrieve policy via RAG ---

policy_retriever_agent = Agent(
    name="policy_retriever_agent",
    model="gemini-2.0-flash",
    description="RAG-based policy document retriever",
    instruction="you are an agent to retrive the policy document"
                "use the tool 'retrieve_policy_tool' to retrive the  policy document",
    output_key="policy_summary",
    tools=[retrieve_policy_tool],
)

