#!/usr/bin/env python3

"""
 Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name

    Args:
      mongo_collection (object): pymongo collection object
      name (str): Description of the second parameter.
      topics:  (list of strings) will be the
      list of topics approached in the school

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
