from flask import Flask
from flask_cors import CORS
from flask import make_response
from google.cloud import firestore

import os
import pinecone

import numpy as np
from numpy.linalg import norm

db = firestore.Client(project="lagom-server")
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
"""
Use cases:

User enters word
    - Fetch word from vector DB
    - Fetch word of the day

    - Get similiarity score
    - Get degree away divided by 2 for both directions

    - Fetch less like word
    - Fetch more like word

    - Return word score and direction words
"""


def euclidean(a, b):
    sum = 0
    for i in range(0, len(a)):
        sum += (a[i] - b[i])**2
    return sum


@app.route("/")
def hello_world():
    return "<h1>Lagom Health Check</h1>"


@app.route("/riddle")
def get_riddle():
    doc_ref = db.collection("game")
    document = doc_ref.document("current").get().to_dict()
    riddle = document['riddle']

    return {"riddle": riddle}


@app.route("/giveup")
def give_up():
    doc_ref = db.collection("game")
    document = doc_ref.document("current").get().to_dict()
    word_of_the_day = document['answer']
    return {"guess": word_of_the_day.lower(), "score": 100, "isWinner": True}


@app.route("/game/<word>")
def guess(word):
    isWinner = False
    doc_ref = db.collection("game")
    document = doc_ref.document("current").get().to_dict()
    word_of_the_day = document['answer']
    wotd_idx = document['index']

    if word == word_of_the_day:
        isWinner = True

    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

    pinecone.init(api_key=PINECONE_API_KEY,
                  environment="northamerica-northeast1-gcp")

    index = pinecone.Index("lagom")

    wotd = index.fetch(ids=[wotd_idx])
    wotd_values = wotd["vectors"][wotd_idx]["values"]

    query = index.query(vector=wotd_values, filter={
        "word": {"$eq": word.lower()}}, top_k=1, include_values=True)

    matches = query['matches']
    if len(matches) == 0:
        return make_response("Unable to find word. Please try another!", 500)
    else:
        score = matches[0]['score']
        # 70 is about the average
        score = (score-0.7)/(1-0.7)
        return {"guess": word.lower(), "score": round(score * 100, 2), "isWinner": isWinner}


@app.route("/hint/<int:attempt>")
def hint(attempt):
    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

    pinecone.init(api_key=PINECONE_API_KEY,
                  environment="northamerica-northeast1-gcp")

    index = pinecone.Index("lagom")

    doc_ref = db.collection("game")
    document = doc_ref.document("current").get().to_dict()
    word_of_the_day = document['answer']
    wotd_idx = document['index']

    wotd = index.fetch(ids=[wotd_idx])
    wotd_values = wotd["vectors"][wotd_idx]["values"]

    query = index.query(vector=wotd_values, filter={
        "word": {"$nin": [word_of_the_day, word_of_the_day[0:-2], word_of_the_day[0:-3]]},
    },
        top_k=4,
        include_metadata=True)
    matches = query['matches']
    print(matches)
    match = matches[4-attempt]

    word = match['metadata']['word']
    score = match['score']
    # 70 is about the average
    score = (score-0.7)/(1-0.7)
    return {"guess": word.lower(), "score": round(score * 100, 2), "isWinner": False}


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1",
            port=int(os.environ.get("PORT", 8080)))
