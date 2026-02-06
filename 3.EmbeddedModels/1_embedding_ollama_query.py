from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model='llama3.2:latest')

result = embedding.embed_query("Islamabad is the capital of Pakistan")

print(result)
print(f"\n bydefault embedding length is -> {len(result)}")


################################################

# from langchain_ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(model='llama3.2:latest')
# query_result = embeddings.embed_query("What is the capital of Pakistan?")

# # Slice the first 32 values
# short_result = query_result[:32]
# print(short_result)
# print(f"Original length: {len(query_result)}")
# print(f"Sized length: {len(short_result)}")