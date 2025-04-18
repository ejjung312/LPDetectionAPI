from pydantic import BaseModel

class LPBase(BaseModel):
    pass

class LPCreate(LPBase):
    pass

class LP(LPBase):
    class Config:
        from_attributes = True