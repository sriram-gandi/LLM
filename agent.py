# agent_runner.py
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import os, asyncio
from ppt_generator import build_slides

# Import your prompt and sub-agents
from prompt import prompt
from sub_agents.json_agent import json_agent
from sub_agents.tavily_agent import tavily_agent
from sub_agents.rag_agent import rag_agent

os.environ["GOOGLE_GENAI_USE_VERTEXAI"]="FALSE"
os.environ["GOOGLE_API_KEY"] = "AIzaSyCSf4WyCtG1YOtYrOpHfC84kPfVLtpxCj4"

model = "gemini-2.5-flash"

project_orchestrator_agent = LlmAgent(
    name="Project_Orchestrator_Agent",
    model=model,
    description="Sales pitch agent generating structured JSON for PPT creation",
    instruction=prompt,
    tools=[
        AgentTool(agent=json_agent),
        AgentTool(agent=tavily_agent),
        AgentTool(agent=rag_agent)
    ]
)

session_service = InMemorySessionService()

APP_NAME = "sales_pitch"
USER_ID = "user_1"
SESSION_ID = "session_001"

async def run_agent(query: str):
    """Run orchestrator agent and return final text output."""
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    runner = Runner(
        agent=project_orchestrator_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    content = types.Content(role="user", parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a final response."

    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            break
            
    print(f"<<< Agent Response: {final_response_text}")
    # return(final_response_text)
    return build_slides(str(final_response_text))
