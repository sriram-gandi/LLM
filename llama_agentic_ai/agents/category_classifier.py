from llama_runner import run_llama

def classify_category(text: str) -> str:
    prompt = f"""Classify the category of the following feedback:
Feedback: "{text}"
Categories: Product, Delivery, Pricing, Support, Other
Answer:"""
    return run_llama(prompt)
