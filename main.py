# main.py
\"\"\"
RAG Chatbot using LangChain
Author: Utswarg Malakar
\"\"\"

import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Fake retriever
class DummyRetriever:
    def retrieve(self, question):
        for _, row in df.iterrows():
            if question.lower() in row['question'].lower():
                return row['answer']
        return "Sorry, I don't know that."

retriever = DummyRetriever()

# Chat loop
def chat():
    print("Welcome to the RAG Chatbot! Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        print("Bot:", retriever.retrieve(query))

if __name__ == "__main__":
    chat()
