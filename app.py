from flask import Flask, request
from voice import speech_to_text, text_to_speech
from langchain_community.llms import Ollama

app = Flask(__name__)

# Ollama LLM (light model you installed)
llm = Ollama(model="llama3.2:1b")

# Search function (simple RAG)
def search(query):
    try:
        with open("doc.txt", "r", encoding="utf-8") as f:
            data = f.read()

        # simple keyword match (you can improve later with vector DB)
        if query.lower() in data.lower():
            return data
        else:
            return None

    except Exception as e:
        print("Search error:", e)
        return None


# Response generator (FIXED)

def generate_response(query, docs):
    if docs:
        prompt = f"""
You are a helpful assistant.
Use the context only if relevant.

Context:
{docs}

User Question:
{query}

Give a clear and helpful answer.
"""
    else:
        prompt = f"""
You are a helpful assistant.
Answer the user question directly.

User Question:
{query}
"""

    return llm.invoke(prompt)



# Voice endpoint

@app.route("/voice", methods=["POST"])
def voice():
    try:
        file = request.files["audio"]
        file.save("input.wav")

        # 1. Speech → Text
        query = speech_to_text("input.wav")
        print("User said:", query)

        # 2. Search docs
        docs = search(query)

        # 3. Generate response (FIXED LOGIC)
        response = generate_response(query, docs)

        # 4. Text → Speech
        text_to_speech(response)

        return {"query": query, "response": response}

    except Exception as e:
        return {"error": str(e)}



# Run app

if __name__ == "__main__":
    app.run(debug=True)