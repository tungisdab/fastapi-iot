from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
        
class ParkingEntry(BaseModel):
    entry_time: datetime
    is_parked: bool = None