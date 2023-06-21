from flask import Flask
from flask_cors import CORS
from flask import make_response

import os
import pinecone

import numpy as np
from numpy.linalg import norm

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


@app.route("/")
def hello_world():
    return "<h1>Lagom Health Check</h1>"


@app.route("/game/<int:game>/<word>")
def guess(game, word):
    word_of_the_day = "miyuki"

    if word == word_of_the_day:
        return {"guess": word.lower(), "score": 1, "isWinner": True}

    PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

    pinecone.init(api_key=PINECONE_API_KEY, environment="northamerica-northeast1-gcp")

    index = pinecone.Index("lagom")

    wotd = index.fetch([word_of_the_day])

    wotd_values = wotd["vectors"][word_of_the_day]["values"]

    guess = index.fetch([word.lower()])

    try:
        guess_values = guess["vectors"][word.lower()]["values"]
    except:
        res = make_response(
            "Unable to find word. Currently Lagom is running on a small dataset. Improvements coming soon!",
            500,
        )
        return res

    # magic fucking numbers
    cos = (
        np.dot(wotd_values, guess_values) / (norm(wotd_values) * norm(guess_values))
        - 0.5
    ) * 2

    return {"guess": word.lower(), "score": round(cos, 2), "isWinner": False}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
