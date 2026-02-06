from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Waseem Akram is a Pakistani cricketer known for his aggressive bowling, batting and leadership.",
    "Inzmam is a former Pakistani captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Imran Nazeer is known for his elegant batting and record-breaking double centuries.",
    "Shoaib Akhtar is a former fast bowler known as Rawalpindi Express and yorkers."
]

query = "tell me about Shoaib Akhtar"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index, scores = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] 

print(query)
print(documents[index])
print("similarity score is:", scores)
