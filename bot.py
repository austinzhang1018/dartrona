#!/usr/bin/env python
# coding: utf-8


from haystack import Finder
from haystack.indexing.utils import convert_files_to_dicts, fetch_archive_from_http
from haystack.reader.farm import FARMReader
from haystack.reader.transformers import TransformersReader
from haystack.utils import print_answers
import json

# Connect to Elasticsearch

# from haystack.database.elasticsearch import ElasticsearchDocumentStore

# don't use elasticsearch for now
# document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")

from haystack.database.memory import InMemoryDocumentStore
document_store = InMemoryDocumentStore()

def build_dataset():
    with open('data.json') as f:
        data = json.load(f)
    for article in data:
        filename = article['url'].split('/')[-1]
        with open('articles/%s.txt' % filename, 'w') as f:
            print(article['text'], file=f)
    

# Convert files to dicts
# You can optionally supply a cleaning function that is applied to each doc (e.g. to remove footers)
# It must take a str as input, and return a str.

doc_dir = 'articles'

def write_storage():
    dicts = convert_files_to_dicts(dir_path=doc_dir, split_paragraphs=True)
    document_store.write_documents(dicts)

write_storage()

from haystack.retriever.sparse import TfidfRetriever# ElasticsearchRetriever
# retriever = ElasticsearchRetriever(document_store=document_store)
retriever = TfidfRetriever(document_store=document_store)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)

finder = Finder(reader, retriever)

def get_prediction(question, num_retreive, num_read):
    return finder.get_answers(question=question, top_k_retriever=num_retreive, top_k_reader=num_read)
