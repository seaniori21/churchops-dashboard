from sqlmodel import SQLModel, Field, Relationship
from .service import Service

class PostServiceNote(SQLModel, table=True):
    __tablename__ = "post_service_note"
    id : int | None = Field(default=None, primary_key=True)
    title: str 
    description: str 

    service_id : int = Field(foreign_key="service.id", nullable=False)
    service : "Service" = Relationship(back_populates="post_service_notes")
