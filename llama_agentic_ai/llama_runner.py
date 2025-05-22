import subprocess

def run_llama(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", "dolphin3"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8"  # Avoid UnicodeDecodeError
        )

        if result.returncode != 0:
            print("Error:", result.stderr)
            return "ERROR: Model execution failed."

        return result.stdout.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"
