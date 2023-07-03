import os
import openai
import pandas as pd
import pinecone
import json

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]


pinecone.init(api_key=PINECONE_API_KEY,
              environment="northamerica-northeast1-gcp")
openai.api_key = OPENAI_API_KEY

index = pinecone.Index("lagom")

'''
df = pd.read_csv("./unigram_freq.csv")
df = df.dropna()
print(len(df))
'''


def get_embedding(words, model="text-embedding-ada-002"):
    return openai.Embedding.create(input=words, model=model)["data"]


def make_df():
    all_words = []
    all_embeddings = []
    for i in range(0, 50000, 500):
        batch_words = df.iloc[i:i+500]["word"].tolist()
        all_words = all_words + batch_words

        print(f'Obtaining embeddings for batch: {i}')
        batch_embeddings = get_embedding(batch_words)
        for embedding in batch_embeddings:
            all_embeddings.append(embedding["embedding"])

    metadata_list = []
    for word in all_words:
        metadata_list.append({"word": word})

    embedding_dict = {"id": list(range(0, 50000)),
                      "vector": all_embeddings,
                      "metadata": metadata_list
                      }

    final_df = pd.DataFrame(data=embedding_dict)
    final_df.to_csv('./pinecone_embeddings')


def chunker(seq, size):
    'Yields a series of slices of the original iterable, up to the limit of what size is.'
    for pos in range(0, len(seq), size):
        yield seq.iloc[pos:pos + size]


def convert_data(chunk):
    'Converts a pandas dataframe to be a simple list of tuples, formatted how the `upsert()` method in the Pinecone Python client expects.'
    data = []
    for i in chunk.to_dict('records'):
        try:
            meta_dict = json.loads(str(i['metadata']))
            value = meta_dict['word']

            value_str = i['values']
            value_str = value_str[1:]
            value_str = value_str[:-1]

            res = [float(idx) for idx in value_str.split(', ')]
            if 'metadata' in i:
                data.append((str(i['id']), res, {"word": value}))
            else:
                data.append((str(i['id']), i['values']))
        except:
            print(f"Unable to upload word: {str(i['metadata'])}")
    return data


def pinecone_upsert():
    embed_df = pd.read_csv("./pinecone_embeddings.csv")
    # print(embed_df.to_dict()['id'])
    count = 0
    for chunk in chunker(embed_df, 100):
        print(count)
        index.upsert(vectors=convert_data(chunk), show_progress=True)
        count = count + 1


if __name__ == "__main__":
    pinecone_upsert()
