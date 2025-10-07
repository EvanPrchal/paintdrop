from sqlmodel import Field, Relationship, SQLModel

class ColorSchemeLink(SQLModel, table=True):
    scheme_name: str = Field(foreign_key="colorscheme.name", primary_key=True)
    hexcode: str = Field(foreign_key="color.hexcode", primary_key=True)

class UserSchemeLink(SQLModel, table=True):
    user_name: int = Field(foreign_key="user.username", primary_key=True)
    scheme_name: str = Field(foreign_key="colorscheme.name", primary_key=True)

class User(SQLModel, table=True):
    username: str = Field(primary_key=True)
    email: str
    hashed_password: str
    token: str | None = None
    schemes: list["ColorScheme"] = Relationship(back_populates="users", link_model=UserSchemeLink)

class Color(SQLModel, table=True):
    hexcode: str = Field(primary_key=True)
    schemes: list["ColorScheme"] = Relationship(back_populates="colors", link_model=ColorSchemeLink)

class RGBA(SQLModel, table=True):
    id: int = Field(primary_key=True)
    red: int
    green: int
    blue: int
    alpha: float | None = None

class HSLA(SQLModel, table=True):
    id: int = Field(primary_key=True)
    hue: int
    saturation: float
    light: float
    alpha: float | None = None

class ColorScheme(SQLModel, table=True):
    name: str = Field(primary_key = True)
    temperature: str
    palette_type: str
    colors: list[Color] = Relationship(back_populates="schemes", link_model=ColorSchemeLink)
    users: list[User] = Relationship(back_populates="schemes", link_model=UserSchemeLink)

