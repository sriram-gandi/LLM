from agents.category_classifier import classify_category
from agents.sentiment_analyzer import analyze_sentiment
from agents.suggestion_generator import generate_suggestion
import json

def main():
    # Read input
    with open("input.txt", "r", encoding="utf-8") as f:

        feedback = f.read().strip()

    # Run agents
    category = classify_category(feedback)
    sentiment = analyze_sentiment(feedback)
    suggestion = generate_suggestion(feedback, category, sentiment)

    # Output
    result = {
        "feedback": feedback,
        "category": category,
        "sentiment": sentiment,
        "response": suggestion
    }

    with open("output.json", "w", encoding="utf-8") as f:

        json.dump(result, f, indent=2)

    print("Analysis complete! Check output.json")

if __name__ == "__main__":
    main()
