from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from typing import Optional
from .models import Base


class Database:
    def __init__(self, uri: str = ":memory:"):
        self.uri = "sqlite:///{}".format(uri)
        self.engine = create_engine(self.uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, objects: any) -> Optional[Exception]:
        session = self.Session()
        try:
            session.bulk_save_objects(objects)
            session.commit()
            return
        except IntegrityError:
            session.rollback()
            return IntegrityError
