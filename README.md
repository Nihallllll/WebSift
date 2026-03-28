<div align="center">
  <img src="./public/aossie-logo.svg" alt="AOSSIE Logo" height="60" />
</div>

<div align="center">

[![Static Badge](https://img.shields.io/badge/aossie.org/WebIntelligence-228B22?style=for-the-badge&labelColor=FFC517)](https://github.com/AOSSIE-Org/WebSift)

[![Telegram Badge](https://img.shields.io/badge/Telegram-black?style=flat&logo=telegram&logoColor=white&logoSize=auto&color=24A1DE)](https://t.me/StabilityNexus)
[![X Badge](https://img.shields.io/twitter/follow/aossie_org)](https://x.com/aossie_org)
[![Discord Badge](https://img.shields.io/discord/1022871757289422898?style=flat&logo=discord&logoColor=white&logoSize=auto&label=Discord&labelColor=5865F2&color=5F2887)](https://discord.gg/hjUhu33uAn)
[![Medium Badge](https://img.shields.io/badge/Medium-black?style=flat&logo=medium&logoColor=black&logoSize=auto&color=white)](https://news.stability.nexus/)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-black?style=flat&logo=LinkedIn&logoColor=white&logoSize=auto&color=0A66C2)](https://www.linkedin.com/company/aossie/)
[![Youtube Badge](https://img.shields.io/youtube/channel/subscribers/UCKVVLbawY7Gej_3o2WKsoiA?style=flat&logo=youtube&logoColor=white%20&logoSize=auto&labelColor=FF0000&color=FF0000)](https://www.youtube.com/@AOSSIE-Org)

</div>

---

# Web Intelligence

**Fetch the internet, serve it to any AI.**

Web Intelligence is a Python library that crawls websites (or searches the web for you), extracts useful text, and turns it into clean, formatted context any LLM can read — OpenAI, Ollama, Groq, Anthropic, LangChain, or your own code. No API key is required for core indexing and retrieval.

```
You give it a URL                        You ask a question
┌──────────────────────────┐             ┌──────────────────────────────┐
│  pipeline.index_url(url) │──crawl────>│  pipeline.retrieve(question) │
│                          │  extract   │                              │
│  or search the web:      │  chunk     │  → ctx.context_text          │
│  pipeline.search_web(q)  │  embed     │  → ctx.sources               │
│                          │  store     │  → ctx.as_messages()         │
└──────────────────────────┘             └──────────────────────────────┘
   One line of code.                       LLM-ready context, any provider.
   No API key required for core.           OpenAI / Ollama / Groq / Anthropic.
```

---

## 🚀 Features

- **Zero API key required** — core indexing/retrieval works out of the box. Optional extras are available for GPU embeddings, ChromaDB, and web search.
- **One-line web search** — `search_web("your question")` searches DuckDuckGo, crawls the top results, indexes them, and returns LLM-ready context automatically.
- **Pluggable everything** — swap embedders, vector stores, and search providers without changing your pipeline code.
- **Framework agnostic** — works with OpenAI, Groq, Ollama, Anthropic, LangChain, or plain Python. Returns a `RetrievedContext` object with `.context_text`, `.sources`, and `.as_messages()`.
- **Production-grade crawler** — HTTP/2, retry logic, rate limiting, and robots.txt compliance built in.
- **REST API + CLI included** — `web-intelligence serve` spins up a full FastAPI server. CLI available for indexing and retrieval without writing code.

---

## 💻 Tech Stack

- **Python 3.10+**
- **HTTP/2 crawler** with retry, rate limiting, and robots.txt support
- **Pluggable embedders** — SentenceTransformer, FastEmbed, OpenAI, Ollama
- **Pluggable vector stores** — ChromaDB, NumPy
- **Web search via `ddgs`** — no API key required
- **FastAPI** for the optional REST server

---

## ✅ Project Checklist

- **The AI/ML components:**
  - [x] Embedding models are pluggable — swap without changing pipeline code
  - [x] Vector store backends are pluggable — ChromaDB or NumPy out of the box
    - [x] Web search is privacy-respecting — ddgs backend, no API key required
  - [x] Output is LLM-agnostic — works with any provider via `.as_messages()`
  - [x] Caching layer for URLs, content, and embeddings to avoid redundant compute

---

## 🔗 Repository Links

1. [Main Repository](https://github.com/AOSSIE-Org/WebSift)
2. [Core pipeline source](https://github.com/AOSSIE-Org/WebSift/blob/main/web_intelligence/optimized_pipeline.py)
3. [Embedders](https://github.com/AOSSIE-Org/WebSift/tree/main/web_intelligence/embedders)
4. [Vector stores](https://github.com/AOSSIE-Org/WebSift/tree/main/web_intelligence/vector_stores)

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Your Code                                   │
│                                                                     │
│  pipeline.index_url(url)          pipeline.search_web(question)    │
│         │                                    │                      │
│         └──────────────┬───────────────────--┘                      │
└──────────────────────--|────────────────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      FastPipeline (Core)                            │
│                                                                     │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌───────────┐  │
│  │  Crawler   │──>│ Extractor  │──>│  Chunker   │──>│ Embedder  │  │
│  │ HTTP/2     │   │ HTML→text  │   │ ~400 words │   │ pluggable │  │
│  │ retry/rate │   │ clean text │   │ overlapping│   │           │  │
│  └────────────┘   └────────────┘   └────────────┘   └─────┬─────┘  │
│                                                            │        │
│  ┌─────────────────────────────────────────────────────────▼─────┐  │
│  │                    Vector Store (pluggable)                   │  │
│  │              ChromaDB  ·  NumpyVectorStore                    │  │
│  └───────────────────────────────────┬───────────────────────────┘  │
│                                      │                              │
│                                      ▼                              │
│                          ┌────────────────────┐                     │
│                          │  Context Formatter │                     │
│                          │  → context_text    │                     │
│                          │  → sources         │                     │
│                          │  → as_messages()   │                     │
│                          └────────────────────┘                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow

```
index_url(url)
    │
    ▼
Crawler fetches page (HTTP/2, retry, robots.txt)
    │
    ▼
Extractor strips HTML → clean article text
    │
    ▼
Chunker splits into overlapping ~400-word pieces
    │
    ▼
Embedder converts each chunk → vector
    │
    ▼
Vector store saves vectors for fast search
    │
    └──────────────────────────────────────────┐
                                               │
retrieve(question)                             │
    │                                          │
    ▼                                          │
Embed the question → vector                   │
    │                                          │
    ▼                                          │
Vector store finds most similar chunks ───────┘
    │
    ▼
Context Formatter packages results
    │
    ▼
RetrievedContext returned
    ├── .context_text   → clean text for any LLM
    ├── .sources        → source URLs
    └── .as_messages()  → OpenAI-compatible format
```

---

## 🍀 Getting Started

### Prerequisites

- Python 3.10+, pip

### Installation

```bash
pip install web-intelligence
```

Pick optional extras based on what you need:

`web-intelligence` (core) supports local indexing/retrieval without API keys.

```bash
# Lightweight embeddings (recommended to start)
pip install web-intelligence[fastembed]

# GPU-accelerated embeddings (heavier, ~2 GB)
pip install web-intelligence[gpu]

# Web search backend (ddgs, no API key)
pip install web-intelligence[search]

# ChromaDB vector store (production-grade persistence)
pip install web-intelligence[chromadb]

# REST API server
pip install web-intelligence[server]

# Everything at once
pip install web-intelligence[all]
```

---

### Quick Start

#### Index a website and ask questions

```python
from web_intelligence import FastPipeline

pipeline = FastPipeline()

# Crawl and index a page
pipeline.index_url("https://en.wikipedia.org/wiki/Python_(programming_language)")

# Ask a question — get formatted context for any LLM
ctx = pipeline.retrieve("what is python used for?")
print(ctx.context_text)      # clean text, ready for any LLM
print(ctx.sources)           # source URLs
messages = ctx.as_messages() # OpenAI-compatible message format
```

#### Search the web (no URL needed)

```python
from web_intelligence import FastPipeline

pipeline = FastPipeline()

# One line: searches DuckDuckGo → crawls top results → indexes → retrieves
ctx = pipeline.search_web("latest features in Python 3.12")
print(ctx.context_text)
```

#### Use with any LLM (Groq + LangChain example)

This example is optional and requires a Groq API key.

```bash
pip install langchain-groq python-dotenv
```

```python
from web_intelligence import FastPipeline
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
# Requires GROQ_API_KEY in your environment

pipeline = FastPipeline()
ctx = pipeline.search_web("what is FastAPI framework")

llm = ChatGroq(model="llama-3.3-70b-versatile")
response = llm.invoke(ctx.as_messages())
print(response.content)
```

#### Index multiple pages at once

```python
urls = [
    "https://docs.python.org/3/tutorial/index.html",
    "https://fastapi.tiangolo.com/",
    "https://docs.pydantic.dev/latest/",
]
results = pipeline.index_batch(urls)
```

---

## ⚙️ Configuration

```python
from web_intelligence import FastPipeline, Config

config = Config()
config.chunker.chunk_size = 500            # words per chunk
config.chunker.chunk_overlap = 75          # overlap between chunks
config.embedding.model_name = "all-mpnet-base-v2"  # better accuracy
config.crawler.max_retries = 5             # more retries

pipeline = FastPipeline(config=config)
```

Or use environment variables in a `.env` file:

```env
WI_CHUNK_SIZE=500
WI_EMBEDDING_MODEL=all-mpnet-base-v2
WI_CRAWLER_MAX_RETRIES=5
WI_SERVER_PORT=9000
```

---

## 🔌 Pluggable Components

Swap out any component without changing the rest of your pipeline:

```python
from web_intelligence import FastPipeline
from web_intelligence.embedders import FastEmbedEmbedder
from web_intelligence.vector_stores import NumpyVectorStore

pipeline = FastPipeline(
    embedder=FastEmbedEmbedder(),   # lightweight, no GPU
    vector_store=NumpyVectorStore() # no ChromaDB needed
)
```

| Component | Available Options |
|---|---|
| **Embedders** | `SentenceTransformerEmbedder`, `FastEmbedEmbedder`, `OpenAIEmbedder`, `OllamaEmbedder` |
| **Vector stores** | `ChromaVectorStore`, `NumpyVectorStore` |
| **Search providers** | `DuckDuckGoSearchProvider` |

---

## 🖥️ REST API

```bash
web-intelligence serve
```

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/index` | Index a single URL |
| `POST` | `/index/batch` | Index multiple URLs |
| `POST` | `/retrieve` | Get LLM-ready context for a question |
| `POST` | `/search-web` | Web search → context in one call |
| `GET` | `/documents` | List all indexed documents |
| `GET` | `/stats` | Pipeline statistics |
| `GET` | `/health` | Health check |

---

## 🖱️ CLI

```bash
web-intelligence index https://example.com
web-intelligence search "what is python"
web-intelligence retrieve "explain decorators"
web-intelligence documents
web-intelligence stats
web-intelligence serve
```

---

## 📁 Project Structure

```text
web_intelligence/
├── __init__.py              # Public API exports
├── optimized_pipeline.py    # Core pipeline (crawl → embed → store → retrieve)
├── config.py                # Configuration with env var support
├── async_crawler.py         # HTTP/2 crawler with retry + rate limiting
├── crawler.py               # Crawl result data class
├── extractor.py             # HTML → clean text extraction
├── chunker.py               # Text splitting into overlapping chunks
├── context_formatter.py     # Formats search results for LLMs
├── cache.py                 # URL + content + embedding caches
├── server.py                # FastAPI REST server
├── exceptions.py            # Custom exception types
├── _logging.py              # Logging setup
├── embedders/               # Pluggable embedding backends
│   ├── sentence_transformer.py
│   ├── fastembed_embedder.py
│   ├── openai_embedder.py
│   └── ollama_embedder.py
├── vector_stores/           # Pluggable vector store backends
│   ├── chroma_store.py
│   └── numpy_store.py
└── search_providers/        # Pluggable web search backends
    └── duckduckgo_provider.py
```

---

## 🙌 Contributing

⭐ Don't forget to star this repository if you find it useful! ⭐

Thank you for considering contributing to this project! Contributions are highly appreciated and welcomed. To ensure smooth collaboration, please refer to our [Contribution Guidelines](./CONTRIBUTING.md).

---

## ✨ Maintainers

- [Bruno](https://github.com/Zahnentferner)
- [Nihal](https://github.com/Nihallllll)

---

## 📍 License

This project is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for details.

---

## 💪 Thanks To All Contributors

Thanks a lot for spending your time helping Web Intelligence grow. Keep rocking 🥂

[![Contributors](https://contrib.rocks/image?repo=AOSSIE-Org/WebSift)](https://github.com/AOSSIE-Org/WebSift/graphs/contributors)

© 2026 AOSSIE