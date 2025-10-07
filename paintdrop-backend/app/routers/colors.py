from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_db
from app.models import Color
from app.schemas import CreateColorRequest

router = APIRouter()

### GET ###

@router.get("")
def get_colors(db: Session = Depends(get_db)) -> list[Color]:
    return db.exec(select(Color)).all()

@router.get("/{hexcode}")
def get_color_by_hex(hexcode: str, db: Session = Depends(get_db)) -> Color:
    color: Color | None = db.get(Color, hexcode)
    if not color:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid hexcode")
    return color

### POST ###

@router.post("")
def create_color(create_color_request: CreateColorRequest, db: Session = Depends(get_db)) -> str:
    exists: Color | None = db.get(Color.hexcode)
    if not exists: 
        color: Color = Color(**create_color_request.model_dump())
        db.add(color)
        db.commit()
        db.refresh(color)
        return color.hexcode
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Color with hexcode {create_color_request.hexcode} already exists")
