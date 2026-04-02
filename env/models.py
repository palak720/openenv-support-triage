
from pydantic import BaseModel

class Observation(BaseModel):
    ticket_id: str
    message: str
    customer_tier: str
    timestamp: str


class Action(BaseModel):
    category: str
    priority: str
    assigned_team: str
    response: str


class Reward(BaseModel):
    score: float
    feedback: str