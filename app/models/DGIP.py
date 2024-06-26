from pydantic import BaseModel


class DigitalInput(BaseModel):
    id: str
    state: str = "OFF"


DigitalInputs = {
    "DIGIN-1": DigitalInput(id="DIGIN-1"),
    "DIGIN-2": DigitalInput(id="DIGIN-2"),
    "DIGIN-3": DigitalInput(id="DIGIN-3"),
    "DIGIN-4": DigitalInput(id="DIGIN-4"),
    "DIGIN-5": DigitalInput(id="DIGIN-5"),
    "DIGIN-6": DigitalInput(id="DIGIN-6"),
    "DIGIN-7": DigitalInput(id="DIGIN-7"),
    "DIGIN-8": DigitalInput(id="DIGIN-8"),
    "DIGIN-9": DigitalInput(id="DIGIN-9"),
    "DIGIN-10": DigitalInput(id="DIGIN-10"),
}
