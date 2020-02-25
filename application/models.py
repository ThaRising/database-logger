from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, CheckConstraint, DateTime
from sqlalchemy.orm import validates

Base = declarative_base()


class IP(Base):
    __tablename__ = "ip"
    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    __table_args__ = (
        CheckConstraint("length(address) > 0",
                        name="address_min_length"),
        CheckConstraint("length(address) < 33",
                        name="address_max_length"),
    )

    @validates("address")
    def validate_address(self, key, address: str) -> str:
        if len(address) < 1:
            raise ValueError("Attr address does not satisfy minlength of 1.")
        elif len(address) > 32:
            raise ValueError("Attr address does not satisfy maxlength of 32.")
        return address

    def __repr__(self) -> str:
        """
        :return: Returns a string representation of the object
        """
        return f"{self.__class__.__name__}" \
               f"('id': '{self.id}', 'address': '{self.address}')"

    def __iter__(self) -> None:
        """
        :return: Yields the items attributes as a dictionary
        """
        yield "id", self.id
        yield "address", self.address

    def __len__(self) -> int:
        """
        :return: Returns the total number of the tables SQL columns
        """
        return 2


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)

