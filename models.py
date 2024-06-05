from pydantic import BaseModel
from datetime import datetime
class Stage(BaseModel):
    id: int
    name: str
    status: str
    product_id: int
    updated_at: datetime
class StageTransition(BaseModel):
    product_id: int
    from_stage: int
    to_stage: int
    notes: str = None
