import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

from google.adk.agents import LlmAgent
# Load index
import os
from dotenv import load_dotenv

    # Load environment variables from .env file
load_dotenv()

    # Access environment variables

company_name = os.getenv("presenter_company")
index = faiss.read_index(f"{company_name}/{company_name}.index")

# Load metadata
with open(f"{company_name}/{company_name}.pkl", "rb") as f:
    id_to_doc = pickle.load(f)

# Reload embedder
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Search function (same as before)
def rag_search(query: str, top_k: int = 3):
    query_vec = np.array([embedder.encode(query)], dtype="float32")
    distances, indices = index.search(query_vec, top_k)
    
    results = []
    for dist, idx in zip(distances[0], indices[0]):
        results.append({
            "text": id_to_doc[idx],
            "distance": float(dist),
            "chunk_id": int(idx)
        })
    return results
prompt ="""You are a RAG agent that uses only retrieved context to fill a provided JSON object.

You will receive:
{
  "input_json": {
    "Opportunities": "none",
    "Collaboration": "none",
    "Relationship": "none",
    "offerings": "none"
  },
  "presenter_company_name": "<string>"
  "customer_company_name": "<string>"
}

---

## 🎯 TASK

Your job is to perform `rag_search` using **customer_company_name** to retrieve **the complete contextual section** that contains all relevant information (including success stories) for that customer from the company rag data.

Once you have the context, fill **every field** in `input_json` with facts found **only** in the retrieved passages.

**important**
"If the input JSON contains a mix of filled and unfilled fields (fields with value 'none'), you must preserve all existing filled values and update only the unfilled fields.
Do not modify or overwrite fields that already contain valid data.
Retrieve or infer content strictly for fields with value 'none'.
Return the complete JSON object with the original structure and casing intact, replacing 'none' only with newly filled values."

If a field cannot be filled because it is **absent in the context**, keep it as `"none"`.  
Never invent, infer, or guess.

---

## 🧱 FIELD RULES

- **"Opportunities"** → write 3-4 points on customer's opportunity
  - The customer’s opportunity, goal, or need.
  
- **"Collaboration"** → write 3-4 points on presenter company collaborates
  - How the presenter company collaborates or supports those goals.

- **"Our Relationship"** → 3-4 points on relationship:
  - `years_of_relation`, `current_engagement`, and `primary_service` (if mentioned).
  - If partial data found, write only what’s available.

---

## 🔍 RETRIEVAL INSTRUCTIONS

Perform `rag_search` queries such as:
- `"<customer_company_name> opportunity or relationship or offerings.
- `"Key outcomes, problems solved, or measurable results for <customer_company_name>"`

Retrieve at least **top_k=5** passages to ensure you capture all relevant stories in the same section.

---

## 📦 OUTPUT FORMAT (STRICT)

Return **JSON only**, matching the `input_json` schema **exactly**, with:
- `"none"` replaced by concise factual text.
- No new keys, no removed keys.
- 4-5 points per field, grounded strictly in retrieved context.

🧱 Example:
{
    "Opportunities": "Ray White seeks tailored financial products to support property expansion and digital transformation. Key drivers include rapid onboarding for new projects, embedded mortgage experiences for buyers, and data-driven valuation insights to improve conversion across digital channels.",
    "Collaboration": "CWB can collaborate by providing mortgage APIs for instant eligibility checks, flexible financing structures tied to project milestones, and property valuation tools integrated into Ray White’s buyer journeys. The collaboration emphasizes predictable SLAs, phased rollout across regions, and shared analytics dashboards.",
    "Relationship": "Over 10 years of partnership in real estate financing and digital enablement. Currently engaged in property financing and mortgage pre-approval platform integration.Core services include API-based mortgage tools and valuation workflows.",
    "offerings": "Property Loan Solutions: Long-term financing aligned to project phases,Treasury Services: Digital cash flow and escrow management tools. Digital Property Tools: APIs for mortgage calculation and buyer affordability analysis, ESG Financing: Green funding for sustainable and energy-efficient projects."
  }

yaml
Copy code

---

## 🚫 PROHIBITIONS
- ❌ No prose or explanations outside JSON.  
- ❌ No hallucinated data.  
- ❌ No removal or renaming of keys.  
- ❌ No bullet lists or markdown.  
- ❌ No skipping success stories if they’re present in context (even if customer names differ).

---


✅ Key Improvements Made:

Raises retrieval scope to capture full context section.

Clarifies partial update logic (update only "none" fields).

Explicitly prohibits overwriting filled values.

Guarantees JSON-only structured output.

Adds explicit top_k retrieval and fallback handling."""

# Example search
# print(rag_search("What services does the company provide?", top_k=2))
# from google.adk.models.lite_llm import LiteLlm

model = "gemini-2.5-flash"

rag_agent = LlmAgent(
    name="rag_agent",
    model=model,
    description="you are a rag agent. you retrive the needfull information using the rag_search tool",
    instruction=prompt,
    output_key="rag_output",
    tools=[rag_search]
)
root_agent = rag_agent
