# chainlit-llm-api

On **April 14th, 2025**, OpenAI released the **GPT-4.1 model**, currently **available only via API**. 

This repo introduces `chainlit-llm-api` — a private, production-grade interface for GPT-4.1 inference, built with [Chainlit](https://github.com/Chainlit/chainlit), now fully capable of **processing images via vision inputs**.

---

## Why this Chainlit version is better (today and tomorrow)

| Feature                            | Playground         | `chainlit-llm-api`              |
|------------------------------------|--------------------|-----------------------------|
| GPT-4.1 support                    | No (UI unsupported) | Yes (API-native)            |
| System prompt persistence          | No                  | Yes                         |
| Session memory                     | No                  | Yes (per-session)           |
| Image input support                | No                  | Yes, via base64 encoding    |
| Developer extensibility            | No                  | Yes, Python-native hooks    |
| Integration-ready (RAG, FastAPI)   | No                  | Yes, built for modularity   |
| Self-hosted                        | No                  | Yes, via Cloudflare tunnel  |

---

## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- OpenAI API key

### One-Line Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chainlit-llm-api.git
   cd chainlit-llm-api
   ```

2. Create a `.env` file with your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

3. Run with a single Docker command:
   ```bash
   docker-compose up -d
   ```

4. Access the UI at http://localhost:8000

That's it! The application is now running and ready to use.

### Development Mode
For a hot-reload development environment:
```bash
pip install -r requirements.txt
chainlit run app.py -w
```

---

## MVP Status

- [x] Fully working inference via OpenAI GPT-4.1  
- [x] Image input support using base64 encoding  
- [x] Hot-reload dev loop with `chainlit run app.py -w`  

Planned for next iterations:

- [ ] Vector search over uploaded documents  
- [ ] FastAPI endpoints for file ingestion  
- [ ] Multi-model backend switching  
- [ ] Hardware integration for local inference (LLM Hub)  
- [ ] Fine-grained session filtering in UI  
