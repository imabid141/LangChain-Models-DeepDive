<div align="center">

# 🦜🔗 LangChain Models & Embeddings Lab

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-FFD21E?style=for-the-badge)

### Developed by **[Ghulam Muhammad]**
*Building the foundation for Agentic AI in 2026*

---
</div>

A comprehensive hands-on guide to mastering Language Models (LLMs), Chat Models, and Text Embeddings using **LangChain**, **Ollama**, and **Hugging Face**. This repository serves as a step-by-step roadmap for building the foundation of Agentic AI.

## 📂 Project Structure

The lab is divided into three core pillars:

### 1. LLMs (Large Language Models)
Focuses on basic text-in, text-out completion models.
* `1_llm_demo.py`: Basic invocation using local Llama 3.2 via Ollama.
* `2.ollama_cloud.py`: Connecting to massive cloud models (DeepSeek-V3) using the Ollama library.

### 2. Chat Models
Explores models optimized for conversation and message-based interaction.
* `1_chatmodel_ollama.py`: Running chat-tuned models locally.
* `2_chatmodel_hf_api.py`: Accessing high-performance models (Qwen-Coder) via Hugging Face Inference API.
* `3_chatmodel_hf_local.py`: Running Hugging Face models (TinyLlama) entirely on local hardware using Pipelines.

### 3. Embedding Models
The "math" behind AI memory. Turning text into vectors for search and similarity.
* `1_embedding_ollama_query.py`: Generating vectors for single queries.
* `2_embedding_ollama_docs.py`: Batch embedding multiple documents.
* `3_embedding_hf_local.py`: Using local Sentence-Transformers for efficient embedding.
* **🏆 Mini-Project: `4_Document_similarity.py`**: A real-world application using Cosine Similarity to find the most relevant document (Cricket legends) based on a user query.

---

## 🛠️ Tech Stack

- **Framework:** LangChain / LangChain-Community / LangChain-HuggingFace
- **Local LLM Provider:** Ollama (Llama 3.2)
- **Local Embedding Provider:** Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`)
- **Cloud Providers:** Hugging Face API (Qwen), DeepSeek Ollama Cloud
- **Environment:** Kali Linux / Python 3.13

## ⚙️ Setup Instructions

1. **Install Ollama:** Download from [ollama.com](https://ollama.com) and pull required models:

   ```bash
   ollama pull llama3.2
   ollama pull nomic-embed-text
2. **Environment Setup:**

   ```bash
   python -m venv langchain-env
   source langchain-env/bin/activate
   pip install -r requirements.txt
   ```

3. **API Keys:**
Create a `.env` file for Hugging Face API access:

   ```env
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```

---

## 🧠 Key Takeaways

* **LLM vs ChatModel:** Learned the difference between raw completion and message-based `invoke()` calls.
* **Local vs Cloud:** Balanced the privacy/cost of local models (Ollama) with the power of cloud APIs.
* **Vector Math:** Implemented `cosine_similarity` to understand how RAG (Retrieval Augmented Generation) actually finds information.
