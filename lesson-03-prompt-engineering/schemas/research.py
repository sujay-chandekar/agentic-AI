from pydantic import BaseModel
from typing import List

class ResearchSchema(BaseModel):
    topic: str
    introduction: str
    core_concept: List[str]
    applications: List[str]
    limitations: List[str]
