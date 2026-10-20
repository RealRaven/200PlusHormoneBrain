from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    stream: bool = True