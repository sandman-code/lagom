import os
import openai
import pandas as pd
import pinecone
 

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']


pinecone.init(api_key=PINECONE_API_KEY,
              environment="northamerica-northeast1-gcp")
openai.api_key = OPENAI_API_KEY

index = pinecone.Index("lagom")

df = pd.read_csv("words.txt")
df = df[9786:-1]

def get_embedding(word, model="text-embedding-ada-002"):
      return openai.Embedding.create(input = [word], model=model)['data'][0]['embedding']

for word in df.values:
      embedding = get_embedding(word[0])
      
      try: 
         index.upsert(vectors=[(word[0], embedding)])
         print(f"Upserted: {word[0]}")
      except Exception as e:
         print(e)
         print(f"Failed to upload: {word[0]}")
         break


# upsert null word