from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import select

class Client:
    metadata = MetaData()

    @classmethod
    def setup(cls, engine, conn):
        cls.engine = engine
        cls.conn = conn
        cls.table =  Table("client", cls.metadata,
                           Column("id", Integer, primary_key=True),
                           Column("ip", String(45)),
                           )
        cls.metadata.create_all(engine)

    @classmethod
    def find_one(cls, ip):
        s = select([cls.table.c.id]).where(cls.table.c.ip == ip)
        result = cls.conn.execute(s)
        row = result.fetchone()
        result.close()
        if row:
            return { "id": row[0]}
        return None
