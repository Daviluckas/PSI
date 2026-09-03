from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, validates, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    idade: Mapped[int] = mapped_column(Integer)
    nome: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(25), unique=True)

    @validates("email")
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("Is not email, lapão!")
        return address

    def __repr__(self):
        return(f'Id: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}')