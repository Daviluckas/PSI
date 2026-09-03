from sqlalchemy import create_engine, select
from models import Base, User
from sqlalchemy.orm import Session
from faker import Faker

engine = create_engine("sqlite:///atividade3.db")

Base.metadata.create_all(bind=engine)

faker_ = Faker()

with Session(engine) as session:
    for x in range(10):
        session.add(User(nome=faker_.name(), email=faker_.email(), idade=faker_.random_int(min=10, max=80)))

    session.commit()
print(session.scalars(select(User)).all())