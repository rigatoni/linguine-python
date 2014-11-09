"""
Database adapter.
Concerned with selecting the correct database, port, etc.

author: peter mikitsh
"""

import os
from pymongo import MongoClient

class DatabaseAdapter:

    @staticmethod
    def getDB():

        if 'PYTHON_ENV' in os.environ:
            # Look for Node environment to determine db name.
            db = 'linguine-' + os.environ['PYTHON_ENV']
        else:
            # NODE_ENV not found, default to development
            db = 'linguine-development'
        return MongoClient()[db]
