
# 🤖 AI Research Agent

An autonomous AI-powered research agent that searches the web, queries Wikipedia, and compiles structured research reports — all from a single text prompt.

Built with **LangChain**, **Groq (Qwen 32B)**, and custom tools for web search, Wikipedia lookup, and file saving.

---

## 📌 What It Does

Instead of manually Googling a topic, reading through articles, and writing summaries yourself — just type your query and the agent does it all automatically.

- Searches the web in real time using DuckDuckGo
- Pulls relevant information from Wikipedia
- Uses an LLM to reason, plan, and compile results
- Optionally saves the output to a `.txt` file with a timestamp
- Returns structured output with topic, summary, sources, and tools used

---

## 🗂️ Project Structure

```
ai-research-agent/
│
├── main.py                # Core agent logic
├── tools.py               # Custom tools (search, wikipedia, save)
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed to git)
├── .gitignore             # Ignores .env and output files
└── research_output.txt    # Auto-generated output file (git ignored)
```

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| [LangChain](https://www.langchain.com/) | Agent orchestration framework |
| [Groq](https://groq.com/) | Fast LLM inference (Qwen 32B model) |
| [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) | Real-time web search |
| [Wikipedia API](https://pypi.org/project/wikipedia/) | Structured knowledge lookup |
| [Pydantic](https://docs.pydantic.dev/) | Structured output parsing |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Secure API key management |

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-research-agent.git
cd ai-research-agent
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free Groq API key at [console.groq.com](https://console.groq.com)

---

## 🚀 Usage

Run the agent:

```bash
python main.py
```

You'll be prompted to enter your research query:

```
What can I help you with today? (add 'save to file' if you want to save the results)
```

**Example queries:**

```
Artificial Intelligence trends in 2026
```
```
What is quantum computing? save to file
```
```
Latest developments in renewable energy save to file
```

Adding **"save to file"** to your query will automatically save the structured output to `research_output.txt`.

---

## 📄 Example Output

```json
{
  "topic": "Artificial Intelligence trends in 2026",
  "summary": "AI in 2026 is seeing rapid growth in multimodal models, autonomous agents, and edge AI deployment...",
  "sources": [
    "https://example.com/ai-trends-2026",
    "https://en.wikipedia.org/wiki/Artificial_intelligence"
  ],
  "tools_used": ["search_tool", "wiki_tool", "save_tool"]
}
```

---

## 🔒 .gitignore

Make sure your `.env` and output files are not pushed to GitHub. Create a `.gitignore` file:

```
.env
research_output.txt
venv/
__pycache__/
*.pyc
```

---

## 💡 Business Use Cases

- **Marketing teams** — automate daily competitor or trend research
- **Content creators** — generate research briefs before writing articles
- **Startups** — quickly analyze any new market or technology
- **Students** — get structured summaries on any academic topic

---

## 🧩 How It Works (Architecture)

```
User Query
    │
    ▼
LangChain Agent (Qwen 32B via Groq)
    │
    ├──▶ search_tool (DuckDuckGo) ──▶ Web Results
    │
    ├──▶ wiki_tool (Wikipedia API) ──▶ Encyclopedia Data
    │
    └──▶ save_tool (Custom) ──▶ research_output.txt
    │
    ▼
Pydantic Parser
    │
    ▼
Structured Research Report
```

---

## 📋 Requirements

- Python 3.9+
- Groq API key (free tier available)
- Internet connection (for web search and Wikipedia)

---
