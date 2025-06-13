
from google.adk.agents import Agent 
from tools.tool import say_hello, say_goodbye




greeting_agent = Agent(
        # Using a potentially different/cheaper model for a simple task
        model = "gemini-2.0-flash",
        # model=LiteLlm(model=MODEL_GPT_4O), # If you would like to experiment with other models
        name="greeting_agent",
        instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user by using the 'say_hello'tool only. "
                    "don't reply by your own use the 'say_hello'tool only."
                    "give a politereply to generate the greeting by using the 'say_hello' tool only. "
                    "If the user provides their name, make sure to pass it to the 'say_hello' tool. "
                    "Do not engage in any other conversation or tasks.",
        description="Handles simple greetings and hellos using the 'say_hello' tool.",
         tool =  [say_hello], # Crucial for delegation
       
    )
farewell_agent = Agent(
        model = "gemini-2.0-flash",
        name="farewell_agent",  
        description="Handles simple farewells using the 'say_goodbye' tool.",
        instruction="Handle simple  farewells using the 'say_goodbye' tool. "
                    "Do not engage in any other conversation or tasks.",
        tools=[say_goodbye],
    )


