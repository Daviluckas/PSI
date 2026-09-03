from sqlalchemy import DeclarativeBase, Mapped, mapped_column, String
from sqlalchemy import create_engine
from sqlalchemy import validates

engine = create_engine("sqlite:///atividade3.db")

class base(DeclarativeBase):
    pass

class User(base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    idade: Mapped[int] = mapped_column(int)
    nome: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(25), unique=True)

    @validates("email")
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("Is not email, lapão!")
        return address

