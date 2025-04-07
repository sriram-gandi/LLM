# 🧠 WebSummarizer — AI-Powered Web Page Summarizer (Offline with Llama 3.2 + Ollama)

A fast, privacy-friendly app that **scrapes live web content** and **summarizes it using Llama 3.2** — all powered by [Ollama](https://ollama.com) and running completely offline. Comes with a sleek Streamlit UI for easy interaction.

---

## ✨ Features

- 🌍 Extracts content from any public web page
- 🧠 Summarizes using **Llama 3.2** via **Ollama**
- 🖥️ Interactive front-end built with **Streamlit**
- 🔒 100% offline AI model (no API keys or cloud access required)

---

## ⚙️ How It Works

1. User enters a URL.
2. Page content is scraped using `requests` + `BeautifulSoup`.
3. The content is sent to a locally running **Llama 3.2** model via **Ollama**.
4. A summary is returned and displayed in the Streamlit UI.

---

## 📦 Project Structure