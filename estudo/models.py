from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__ = 'usuario'

  id: Mapped[int] = mapped_column(primary_key=True)
  nome: Mapped[str] = mapped_column(String(30))
  email: Mapped[str] = mapped_column(String(30), unique=True)
  senha: Mapped[int] = mapped_column(String(30), unique=True)
