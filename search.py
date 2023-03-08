from korean_tokenizer import tokenizer
from pathlib import Path

import pickle
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent

# to read bm25 object
with open(BASE_DIR.joinpath('bm25result'), 'rb') as bm25result_file:
    bm25result = pickle.load(bm25result_file)

df = pd.read_pickle(BASE_DIR.joinpath('data/base_datasets.pkl'))

corpus = df['user'].tolist()
system = df['system'].tolist()

print(df.head())


def bm25_search(query, n=5):
    tokenized_query = tokenizer(query)
    topk = bm25result.get_top_n(tokenized_query, corpus, n=n)
    return topk


def bm25_chatbot_response(query, n=5):
    tokenized_query = tokenizer(query)
    scores = bm25result.get_scores(tokenized_query)
    top_idx = np.argmax(scores)
    res = system[top_idx]
    return res


if __name__ == "__main__":
    print(bm25_chatbot_response('나 오늘 여친이랑 헤어졌어 ㅠㅠ'))
