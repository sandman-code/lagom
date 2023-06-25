import openai
from google.cloud import firestore
import os
import random
import pinecone
from flask import Flask

openai.api_key = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
pinecone.init(api_key=PINECONE_API_KEY,
              environment="northamerica-northeast1-gcp")

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
db = firestore.Client(project="lagom-server")

index = pinecone.Index("lagom")

app = Flask(__name__)


def create_query():
    answer_idx = str(random.randint(0, 1000))
    response = index.fetch([answer_idx])
    answer = response['vectors'][str(answer_idx)]['metadata']['word']
    print(answer)
    query = f"Give me a riddle with the answer: {answer}"
    return answer, query, answer_idx


@app.route("/")
def create_riddle():

    answer, query, answer_idx = create_query()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """
                You give extremely abstract and clever riddles.
                Always end the riddle with 'What am I?'.
                Never say the answer
                """,
            },
            {"role": "user", "content": f"{query}"},
        ],
    )

    riddle = response["choices"][0]["message"]["content"]
    riddle = riddle.replace('\n', '\\n')
    document_data = {
        "answer": answer,
        "riddle": riddle,
        "solved": False,
        "solves": 0,
        "index": answer_idx
    }

    doc_ref = db.collection("game")
    doc_ref.document("current").set(document_data)

    return "Successfully updated riddle"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
