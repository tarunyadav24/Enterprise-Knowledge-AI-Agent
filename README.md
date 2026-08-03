<p align="center">
  <img src="screenshots/banner.png" alt="Enterprise Knowledge AI Agent"/>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Azure AI Foundry](https://img.shields.io/badge/Azure%20AI-Foundry-0078D4?style=for-the-badge&logo=microsoftazure)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-412991?style=for-the-badge)
![Azure AI Search](https://img.shields.io/badge/Azure-AI%20Search-0078D4?style=for-the-badge)
![FastMCP](https://img.shields.io/badge/FastMCP-3.4.5-green?style=for-the-badge)
![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-MCP-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

# 🚀 Enterprise Knowledge AI Agent

An enterprise-grade AI assistant built using **Microsoft Azure AI Foundry**, **Azure OpenAI**, **Azure AI Search**, and **FastMCP**.

This project demonstrates how to build a grounded AI agent capable of answering enterprise questions using Azure AI Search and invoking custom tools through the Model Context Protocol (MCP).

---

## ✨ Features

- Azure AI Foundry Agent
- Azure OpenAI GPT-5
- Azure AI Search Knowledge Base
- FastMCP Server
- Enterprise Search Tool
- Company Policy Tool
- Holiday Calendar Tool
- Retrieval-Augmented Generation (RAG)
- Grounded Responses
- Tool Calling

---

## 🏗️ Architecture

> Architecture diagram will be added.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Azure AI Foundry | AI Agent |
| Azure OpenAI | LLM |
| Azure AI Search | Knowledge Retrieval |
| FastMCP | MCP Server |
| JSON | Enterprise Data |
| GitHub | Version Control |

---

## 📁 Project Structure

```text
Enterprise-Knowledge-AI-Agent/
│
├── mcp_server/
│   ├── config.py
│   ├── search.py
│   ├── server.py
│   ├── tools.py
│   └── data/
│       ├── company_policy.json
│       └── holiday_calendar.json
│
├── requirements.txt
├── README.md
├── test_search.py
└── test_tools.py
```

---

## ⚙️ Setup

```bash
git clone https://github.com/tarunyadav24/Enterprise-Knowledge-AI-Agent.git

cd Enterprise-Knowledge-AI-Agent

pip install -r requirements.txt

python mcp_server/server.py
```

---

## 📌 Future Enhancements

- Planner
- Memory
- Observability
- Evaluations
- Tracing
- Multi-Agent Support
- Microsoft Teams Integration
- SharePoint Integration

---

## 👨‍💻 Author

**Tarun Yadav**

- Azure AI Foundry
- Azure OpenAI
- Azure AI Search
- FastMCP
- Agentic AI
