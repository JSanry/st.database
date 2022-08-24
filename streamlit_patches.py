import logging

from sqlitedict import SqliteDict
from streamlit import *

logging.getLogger("sqlitedict").disabled = True


_DB_PATH = ".streamlit/database.sqlite"


class Database:
    def __init__(self, table_name: str = "unnamed") -> None:
        self.table_name = table_name
        self.read_args = {
            "filename": _DB_PATH,
            "tablename": self.table_name,
            "flag": "r",
        }
        self.write_args = {
            "filename": _DB_PATH,
            "tablename": self.table_name,
            "autocommit": True,
        }

    def __getitem__(self, key):
        with SqliteDict(**self.read_args) as db:
            return db[key]

    def __setitem__(self, key, value):
        with SqliteDict(**self.write_args) as db:
            db[key] = value

    def __delitem__(self, key):
        with SqliteDict(**self.write_args) as db:
            del db[key]

    def __iter__(self):
        with SqliteDict(**self.read_args) as db:
            return iter(db)

    def __len__(self):
        with SqliteDict(**self.read_args) as db:
            return len(db)

    def __repr__(self):
        return str(self.read_args)

    def __contains__(self, key):
        with SqliteDict(**self.read_args) as db:
            return key in db

    def items(self):
        with SqliteDict(**self.read_args) as db:
            return list(db.items())

    def keys(self):
        with SqliteDict(**self.read_args) as db:
            return list(db.keys())

    def values(self):
        with SqliteDict(**self.read_args) as db:
            return list(db.values())


database = Database()
