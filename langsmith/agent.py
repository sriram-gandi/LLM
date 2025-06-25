from google.adk.agents import LlmAgent
from langsmith import traceable
import asyncio
import logging
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types # For creating message Content/Parts
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")


logging.basicConfig(level=logging.ERROR)


session_service = InMemorySessionService()

# Define constants for identifying the interaction context
APP_NAME = "super_agent"
USER_ID = "user_1"
SESSION_ID = "session_001" # Using a fixed ID for simplicity

# Create the specific session where the conversation will happen
session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)
print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")



super_agent = LlmAgent(
    name="super_agent",
    model= "gemini-2.5-flash-lite-preview-06-17",
    description= "you are a super agent helps user in diffrent things",
    instruction= "you are a super agent helps user in many things"
                 "greet the user in a polite manner"
                 "give the user required information without any fuss",
)

# --- Runner ---
# Key Concept: Runner orchestrates the agent execution loop.
runner = Runner(
    agent= super_agent, # The agent we want to run
    app_name=APP_NAME,   # Associates runs with our app
    session_service=session_service # Uses our session manager
)
print(f"Runner created for agent '{runner.agent.name}'.")


# @title Define Agent Interaction Function

# For creating message Content/Parts
@traceable
def call_agent_async(query: str, runner, user_id, session_id):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")

  content = types.Content(role='user', parts=[types.Part(text=query)])

  final_response_text = "Agent did not produce a final response." # Default

  # Key Concept: run_async executes the agent logic and yields Events.
  # We iterate through events to find the final answer.
  for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):

      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")

call_agent_async("HI SUPER AGENT. I WANT TO TEST THE AGENT I DEVELOPED.",runner=runner,user_id=USER_ID,session_id=SESSION_ID)  