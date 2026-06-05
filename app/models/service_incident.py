from sqlmodel import SQLModel, Field, Relationship
from .service import Service
from datetime import datetime
from enum import Enum

# TODO: later on we make this more detailed
class Severity(str,Enum):
    idk = "i dont know"
    low = "low"
    mid = "mid"
    high = "high"

# TODO: later on we make this more detailed and bigger
class IncidentType(str,Enum):
    audio = "audio"
    obs = "obs"
    facebook = "facebook"
    propresenter = "propresenter"
    misc = "I dont know"

class ServiceIncident(SQLModel, table=True):
    __tablename__ = "service_incident"
    id : int | None = Field(default=None, primary_key=True)
    description: str 
    timestamp: datetime
    severity: Severity = Field(default=Severity.idk)
    incident_type: IncidentType = Field(default=IncidentType.misc)

    service_id : int = Field(foreign_key="service.id", nullable=False)
    service : "Service" = Relationship(back_populates="service_incidents")
