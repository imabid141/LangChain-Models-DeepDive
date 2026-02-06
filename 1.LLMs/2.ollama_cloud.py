import ollama 

response = ollama.generate(
    model="deepseek-v3.1:671b-cloud",
    prompt="What is the capital of Pakistan?"
)
print(response["response"])