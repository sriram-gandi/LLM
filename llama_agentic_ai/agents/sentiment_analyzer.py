from llama_runner import run_llama

def analyze_sentiment(text: str) -> str:
    prompt = f"""Analyze the sentiment of the customer feedback below:
"{text}"
Sentiment: Positive, Neutral, Negative
Answer:"""
    return run_llama(prompt)
