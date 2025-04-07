import ollama
def generate_response(prompt):
    model_name = "llama3.2:latest"

    response = ollama.chat(
        model=model_name, messages=[{"role": "user", "content": prompt}]
    )
    return response.message.content