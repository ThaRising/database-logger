from sqlalchemy import create_engine


class Database:
    def __init__(self, uri: str = "sqlite:///:memory:"):
        self.engine = create_engine(uri)