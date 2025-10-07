from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session
from fastmcp import FastMCP
from app.schemas import CreateAiColorRequest
from app.models import Color
from app.database import get_db
from pydantic import BaseModel
import httpx
import json

from fastmcp import FastMCP
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent
"i"
router = APIRouter()
mcp = FastMCP()

@mcp.prompt("/chat")
def ask_about_topic(topic: str) -> str:
    return f"can you make a colorscheme of 5 colors and return only the hexcodes based off of {topic}"


mcp_app = mcp.http_app(path='/mcp')
app = APIRouter(lifespan=mcp_app.lifespan)
