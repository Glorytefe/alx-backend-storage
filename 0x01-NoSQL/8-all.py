#!/usr/bin/env python3

"""
 List all documents
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    or returns an empty list if no document in the collection
    """

    return mongo_collection.find()
