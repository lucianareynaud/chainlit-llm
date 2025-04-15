# chainlit-llm

On **April 14th, 2025**, OpenAI released the **GPT-4.1 model**, currently **available only via API**. There is no native support in ChatGPT or the Playground UI at launch.

This repo introduces `chainlit-llm` — a private, production-grade interface for GPT-4.1 inference, built with [Chainlit](https://github.com/Chainlit/chainlit).

---

## Why not just use the Playground?

OpenAI's Playground is limited in several ways:

- No persistent system prompt across sessions  
- No message memory or context chaining  
- No customization of interface, logging, or DX  
- No support for additional tools (e.g., RAG, vector search, file uploads)

---

## Why this Chainlit version is better (today and tomorrow)

| Feature                            | Playground         | `chainlit-llm`              |
|------------------------------------|--------------------|-----------------------------|
| GPT-4.1 support                    | No (UI unsupported) | Yes (API-native)            |
| System prompt persistence         | No                  | Yes                         |
| Session memory (MVP)              | No                  | Yes, via file or DB         |
| Developer extensibility           | No                  | Yes, Python-native hooks    |
| Integration-ready (RAG, FastAPI)  | No                  | Yes, built for modularity   |
| Self-hosted / offline-first       | No                  | Yes, via Cloudflare tunnel  |

---

## MVP Status

- [x] Fully working inference via OpenAI GPT-4.1  
- [x] Local session memory with optional persistence  
- [x] Hot-reload dev loop with `chainlit run app.py -w`  
- [x] Vim-first development environment

Planned for next iterations:

- [ ] Vector search over uploaded documents  
- [ ] FastAPI endpoints for file ingestion  
- [ ] Multi-model backend switching  
- [ ] PostgreSQL for scalable persistence

---
