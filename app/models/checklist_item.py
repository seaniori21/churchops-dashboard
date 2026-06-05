from sqlmodel import SQLModel, Field

class ChecklistItem(SQLModel, table=True):
    __tablename__ = "checklist_item"
    id : int | None = Field(default=None, primary_key=True)
    name: str 
    description: str | None = Field(default=None)