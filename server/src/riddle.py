import openai
from google.cloud import firestore
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
db = firestore.Client(project="lagom-server")

answer = "fidget"
query = f"Give me a riddle with the answer: {answer}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": """
            You are a very cryptic wizard. Give riddles with one word answers.
            You give extremely abstract answers and they should be extremely hard to guess. 
            These riddles should be short and try to trick the guesser.
            """,
        },
        {"role": "user", "content": f"{query}"},
    ],
)

riddle = response["choices"][0]["message"]["content"]


doc_ref = db.collection("game")
doc_ref.add(
    document_data={
        "answer": answer,
        "riddle": riddle,
        "solved": False,
        "solves": 0,
    },
    document_id=str(doc_ref.count().get()[0][0].value + 1),
)
