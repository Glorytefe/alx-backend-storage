#!/usr/bin/env python3

"""
 Insert a document
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwarg
    """

    inserted_docs = mongo_collection.insert_one(kwargs)
    return inserted_docs.inserted_id
