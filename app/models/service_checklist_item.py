from sqlmodel import SQLModel, Field, Relationship
from .service import Service
from .checklist_item import ChecklistItem


class ServiceChecklistItem(SQLModel, table=True):
    __tablename__ = "service_checklist_item"
    service_id : int = Field(primary_key=True, foreign_key="service.id", nullable=False)
    checklist_item_id : int = Field(primary_key=True, foreign_key="checklist_item.id", nullable=False)
    checked: bool = Field(default=False)
    note: str | None = Field(default=None)

    service : "Service" = Relationship(back_populates="service_checklist_items")
    

