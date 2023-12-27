from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./contacts.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birth_date = Column(Date)
    additional_info = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

@app.post("/contacts/")
def create_contact():
    pass

@app.get("/contacts/")
def get_all_contacts():
    pass

@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    pass

@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int):
    pass

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
