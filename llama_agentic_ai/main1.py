from agents.category_classifier import classify_category
from agents.sentiment_analyzer import analyze_sentiment
from agents.suggestion_generator import generate_suggestion
import json
import streamlit as st
from datetime import datetime
import time


def log_trace(agent_name, input_text, output_text, step_description,latency_ms = 100):
    trace = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent_name,
        "step": step_description,
        "input": input_text,
        "output": output_text,
        "latency": latency_ms
    }
    with open("trace_logs.jsonl", "a") as f:
        f.write(json.dumps(trace) + "\n")

def main(user_input):
    

    feedback = user_input

    # Run agents
    start_time = time.time()
    category = classify_category(feedback)
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000 
    log_trace("classify_category", feedback, category, "checks for the category of the feedback",latency_ms)



    start_time = time.time()
    sentiment = analyze_sentiment(feedback)
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000 
    log_trace("analyze_sentiment", feedback, sentiment, "checks for the sentiment of the feedback",latency_ms)



    start_time = time.time()
    suggestion = generate_suggestion(feedback, category, sentiment)
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000 
    log_trace("generate_suggestion", feedback, suggestion , "polite response for the feedback",latency_ms)

    # Output
    result = {
        "feedback": feedback,
        "category": category,
        "sentiment": sentiment,
        "response": suggestion
    }

    with open("output.json", "w", encoding="utf-8") as f:

        json.dump(result, f, indent=2)
    return(result)

    print("Analysis complete! Check output.json")

if __name__ == "__main__":
    st.set_page_config(page_title="Agentic AI Monitor", layout="wide")
    st.title("🤖 Agentic AI Control Panel")

# User input for the task
    user_input = st.text_input("Enter your task:", placeholder="e.g., Generate a research summary on Agentic AI")

# Placeholder for status
    status_placeholder = st.empty()

# Button to run the agentic workflow
    if st.button("Run Agent"):
        if not user_input.strip():
            st.warning("Please enter a task.")
        else:
            with st.spinner("Agent is thinking..."):
        
                result = main(user_input)

        st.success("✅ Agent finished the task!")
        st.subheader("📄 Final Output")
        st.text_area("Result", result, height=200)
