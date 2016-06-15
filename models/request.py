from sqlalchemy import Table, Column, Integer, String, MetaData, Text, DateTime
from sqlalchemy import select


class Request:
    metadata = MetaData()

    @classmethod
    def setup(cls, engine, conn):
        cls.engine = engine
        cls.conn = conn
        cls.table =  Table("request", cls.metadata,
                           Column("id", Integer, primary_key=True),
                           Column("route", Text),
                           Column("time", DateTime),
                           Column("post_data", Text),
                           Column("headers", Text),
                           Column("client_id", Integer)
                           )
        cls.metadata.create_all(engine)
