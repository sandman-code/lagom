import os
import openai
import pandas as pd
import pinecone
import json
from tenacity import retry, wait_random_exponential, stop_after_attempt

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]


pinecone.init(api_key=PINECONE_API_KEY,
              environment="northamerica-northeast1-gcp")
openai.api_key = OPENAI_API_KEY

index = pinecone.Index("lagom")


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

            value_str = i['vector']
            value_str = value_str[1:]
            value_str = value_str[:-1]

            res = [float(idx) for idx in value_str.split(', ')]
            if 'metadata' in i:
                data.append((str(i['id']), res, {"word": value}))
            else:
                data.append((str(i['id']), i['vector']))
        except Exception as e:
            print(f"Unable to upload word: {str(i['metadata'])}")
            print(e)
    return data


def pinecone_upsert(embed_df):
    count = 0
    for chunk in chunker(embed_df, 100):
        print(count)
        data = convert_data(chunk)
        index.upsert(vectors=data, show_progress=True)
        count = count + 1


if __name__ == "__main__":
    '''
    df = pd.read_csv("./nounlist.csv")
    df.columns = ['word']
    df2 = pd.read_csv("./bad-words.csv")
    df2.columns = ['word']
    df = df.dropna()
    print(len(df))

    cond = df['word'].isin(df2['word'])
    df.drop(df[cond].index, inplace=True)

    print(df)
    print(len(df))

    # Retry up to 6 times with exponential backoff, starting at 1 second and maxing out at 20 seconds delay
    @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
    def get_embedding(text: str, model="text-embedding-ada-002") -> list[float]:
        return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]

    count = 0
    metadata_list = []
    all_embeddings = []
    for r in df.iterrows():
        word = r[1].iloc[0]
        metadata_list.append({"word": word})
        embedding = get_embedding(text=str(word))
        all_embeddings.append(embedding)
        print(embedding)
        count += 1

    embedding_dict = {"id": list(range(0, count)),
                      "vector": all_embeddings,
                      "metadata": metadata_list
                      }
    new_df = pd.DataFrame(data=embedding_dict)
    new_df.to_csv('./raw_embeddings.csv')
    '''
    new_df = pd.read_csv('./raw_embeddings.csv')
    pinecone_upsert(embed_df=new_df)
