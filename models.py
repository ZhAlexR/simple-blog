from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"

class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(30))
    text: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="posts")


    def __repr__(self):
        return f"Post(id={self.id}, user_id={self.user_id})"

Base.metadata.create_all(engine)
