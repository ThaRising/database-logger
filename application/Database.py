from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from typing import Optional
from .models import Base


class Database:
    def __init__(self, uri: str = "sqlite:///:memory:"):
        self.engine = create_engine(uri)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, object_: any) -> Optional[str]:
        session = self.Session()
        try:
            session.add(object_)
            session.commit()
            return str(object_)
        except IntegrityError:
            session.rollback()
            return IntegrityError
