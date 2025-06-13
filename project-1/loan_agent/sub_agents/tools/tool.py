
from typing import Optional 


def retrieve_policy_tool() -> str:
    return """
Bank Loan Eligibility & Risk Policy Guidelines

1. Credit Score:
- Minimum credit score required: 600
- Scores between 600-699: Eligible with higher interest
- Scores 700+: Eligible with standard interest

2. Salary Requirements:
- Minimum monthly salary: INR 25,000
- Loan amount should not exceed 15x of monthly salary

3. EMI (Existing Monthly Installments):
- Total EMI must be < 50'%' of monthly salary

4. Age Criteria:
- Applicant age must be between 21 to 60 years

5. Employment Type:
- Only salaried or self-employed individuals with IT returns are eligible
- Salaried employees must have at least 1 year of continuous employment

6. Financial Assets:
- Higher financial assets (savings, property, investments) can offset a lower credit score

7. Spending Pattern:
- Customers with > 70'%' discretionary spending will be marked high-risk

8. Loan Tenure:
- Max loan tenure: 7 years
- For age > 50, tenure should not exceed retirement age

9. Guarantor & Collateral:
- Loans above INR 15 lakhs require a guarantor or collateral

10. Documentation:
- PAN Card, Aadhaar, Bank statements (6 months), Salary slips (3 months), Form-16, and IT returns

11. Risk Categorization:
- Low Risk: CIBIL > 750, EMI < 40%, salary > 40K
- Medium Risk: CIBIL 650-749, EMI 40-50%, salary 25K-40K
- High Risk: CIBIL < 650, EMI > 50%, salary < 25K, or missing documentation

These policies are subject to change per RBI and internal bank rules.
"""

    

def say_hello(name: Optional[str] = None) -> str:
    """Provides a simple greeting. If a name is provided, it will be used.

    Args:
        name (str, optional): The name of the person to greet. Defaults to a generic greeting if not provided.

    Returns:
        str: A friendly greeting message.
    """
    if name:
        greeting = f"Hello, {name}!"
        print(f"--- Tool: say_hello called with name: {name} ---")
    else:
        greeting = "Hello there!" # Default greeting if name is None or not explicitly passed
        print(f"--- Tool: say_hello called without a specific name (name_arg_value: {name}) ---")
    return greeting

def say_goodbye() -> str:
    """Provides a simple farewell message to conclude the conversation."""
    print(f"--- Tool: say_goodbye called ---")
    return "Goodbye! Have a great day."




#--fetch_customer_data--

def fetch_customer_data_tool(customer_id: int) -> dict:
    import pandas as pd
    df = pd.read_excel("C:/Users/Sriram/Desktop/project-1/loan_agent/MockDataset/loan_approval_mock_data.xlsx")    
    customer = df[df['ID'] == customer_id]
    if customer.empty:
        return {"error": "Customer not found"}
    return customer.iloc[0].to_dict()

# print(retrieve_policy_tool())