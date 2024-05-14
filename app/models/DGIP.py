from pydantic import BaseModel


class DegitalInput(BaseModel):
    id: str
    state: str = "OFF"


DegitalInputs = {
    "DIGIN-1": DegitalInput(id="DIGIN-1"),
    "DIGIN-2": DegitalInput(id="DIGIN-2"),
    "DIGIN-3": DegitalInput(id="DIGIN-3"),
    "DIGIN-4": DegitalInput(id="DIGIN-4"),
    "DIGIN-5": DegitalInput(id="DIGIN-5"),
    "DIGIN-6": DegitalInput(id="DIGIN-6"),
    "DIGIN-7": DegitalInput(id="DIGIN-7"),
    "DIGIN-8": DegitalInput(id="DIGIN-8"),
    "DIGIN-9": DegitalInput(id="DIGIN-9"),
    "DIGIN-10": DegitalInput(id="DIGIN-10"),
}