from llama_runner import run_llama

def generate_suggestion(text: str, category: str, sentiment: str) -> str:
    prompt = f"""You are a helpful assistant. The customer gave the following feedback:
"{text}"
Category: {category}
Sentiment: {sentiment}

Write a polite and professional response to address the feedback:"""
    return run_llama(prompt)
