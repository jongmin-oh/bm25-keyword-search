from korean_tokenizer import tokenizer
from pathlib import Path

import pickle
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

# to read bm25 object
with open(BASE_DIR.joinpath('bm25result'), 'rb') as bm25result_file:
    bm25result = pickle.load(bm25result_file)

corpus = pd.read_pickle(BASE_DIR.joinpath(
    'data/base_datasets.pkl'))['user'].tolist()


def bm25_search(query, n=5):
    tokenized_query = tokenizer(query)
    topk = bm25result.get_top_n(tokenized_query, corpus, n=n)
    return topk


if __name__ == "__main__":
    print(bm25_search('나 오늘 여친이랑 헤어졌어 ㅠㅠ', n=5))
