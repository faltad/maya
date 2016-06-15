import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session, sessionmaker

from core_utils.config import Config
from models import Base


# setup the sql connection/engine
sql_url = Config.get_sqlalchemy_url()
engine = sqlalchemy.create_engine(sql_url, echo=True)
Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))