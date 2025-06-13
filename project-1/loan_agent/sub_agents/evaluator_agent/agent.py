from google.adk.agents import Agent


# --- LlmAgent: Evaluate risk based on user data and policy ---
evaluation_prompt = """
You are a risk evaluation assistant. You will be given a customer's financial data and a summary of loan policies. 
Analyze the details and return a decision in this format:
{{"status": "Approved/Rejected", "reason": "reason if rejected", "interest": "Low/Normal/High"}}

Customer Data:
{customer_data}

Loan Policy:
{policy_summary}

Evaluate:
"""

evaluation_agent = Agent(
    name="evaluation_agent",
    model="gemini-2.0-flash",
    description="Evaluates customer loan eligibility and risk",
    prompt=evaluation_prompt,
    output_key="decision",
)

# --- LlmAgent: Summarize decision ---
summary_prompt = """
You will be given the loan decision output. Summarize it for the user in a clear sentence.

Decision:
{decision}

Summary:
"""

summary_agent = Agent(
    name="summary_agent",
    model="gemini-2.0-flash",
    description="Summarizes final loan decision",
    instruction=summary_prompt,
)
