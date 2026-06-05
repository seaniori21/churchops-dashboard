from datetime import date, time
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel

from .post_service_note import PostServiceNote
from .service_checklist_item import ServiceChecklistItem
from .service_incident import ServiceIncident


class Service_Status(str, Enum):
    pending = "pending"
    active = "active"
    completed = "completed"

class Service(SQLModel, table=True):
    __tablename__ = "service"
    id: int | None = Field(default=None, primary_key=True)
    date: date
    start_time: time
    end_time: time | None
    location: str
    status: Service_Status = Field(default=Service_Status.pending)

    post_service_notes: list["PostServiceNote"] = Relationship(back_populates="service")
    service_checklist_items: list["ServiceChecklistItem"] = Relationship(back_populates="service")
    service_incidents: list["ServiceIncident"] = Relationship(back_populates="service")
 
    


