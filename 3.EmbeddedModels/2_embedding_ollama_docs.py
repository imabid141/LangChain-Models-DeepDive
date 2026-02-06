from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model='llama3.2:latest')

documents = [
    "Islamabad is the capital of Pakistan",
    "Karachi is the capital of Sindh",
    "Paris is the capital of France"
]
result = embedding.embed_documents(documents)

print(str(result))
