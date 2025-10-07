from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

class UpdateUserRequest(BaseModel):
    username: str | None = None
    email: str | None = None
    hashed_password: str | None = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class CreateColorRequest(BaseModel):
    hexcode: str

class CreateAiColorRequest(BaseModel):
    prompt: str

class ChatRequest(BaseModel):
    model: str = "gemma3:4b"
    messages: list[dict]  # e.g. [{"role": "user", "content": "Hello"}]
    stream: bool = False
    # you can add extra fields as needed (temperature, max_tokens, etc.)

class ColorRequest(BaseModel):
    style: str = None   # e.g. "pastel", "dark", "vibrant", etc.

class ColorResponse(BaseModel):
    colors: list[str]
