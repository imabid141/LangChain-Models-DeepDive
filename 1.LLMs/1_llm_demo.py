from langchain_ollama import OllamaLLM

llm = OllamaLLM(model='llama3.2:latest')

result = llm.invoke('What is the capital of Pakistan?')

print(result)
