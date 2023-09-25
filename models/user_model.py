from sqlalchemy import Column, Integer, String, Sequence
from ..config.db_config import Base


class User(Base):
    __tablename__ = "users"
    seq = Column(Integer, Sequence("user_seq"), primary_key=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))
    nickname = Column(String(50))

    def __init__(self, email, password, nickname):
        self.email = email
        self.password = password
        self.nickname = nickname

    def to_dict(self):
        return {"email": self.email, "password": self.password, "nickname": self.nickname}
