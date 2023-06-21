import os
import openai
import pandas as pd
import pinecone


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]


pinecone.init(api_key=PINECONE_API_KEY, environment="northamerica-northeast1-gcp")
openai.api_key = OPENAI_API_KEY

index = pinecone.Index("lagom")

df = pd.read_csv("unigram_freq.csv")
df = df.iloc[83839:100000]["word"]


def get_embedding(word, model="text-embedding-ada-002"):
    return openai.Embedding.create(input=[word], model=model)["data"][0]["embedding"]


count = 0
for word in df.values:
    embedding = get_embedding(word[0])

    try:
        index.upsert(vectors=[(word[0], embedding)])
        print(f"Upserted: {word}")
    except Exception as e:
        print(e)
        print(f"Failed to upload: {word} on index - {count}")

    count = count + 1

# upsert null word
