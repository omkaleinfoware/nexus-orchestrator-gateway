from pydantic import BaseModel


class Job(BaseModel):
    id: str
    pipeline: str
    status: str