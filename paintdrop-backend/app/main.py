from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import ai, auth, colors, users
from fastmcp import FastMCP

app = FastAPI(title="Paintdrop")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(ai.router, prefix="/ai", tags=["ai"])
app.include_router(colors.router, prefix="/colors", tags=["colors"])


mcp = FastMCP.from_fastapi(app=app)
