from typing import List

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.orm.properties import ForeignKey


class Base(DeclarativeBase):
    pass


class Animal(Base):
    __tablename__ = "animal"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    language: Mapped[str] = mapped_column(String(30))
    translations: Mapped[List["AnimalSpeech"]] = relationship(cascade="all, delete")


class AnimalSpeech(Base):
    __tablename__ = "animal_speech"

    id: Mapped[int] = mapped_column(primary_key=True)
    origin_animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"))
    translated_animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"))
    text: Mapped[str] = mapped_column(String(512))
    translated_text: Mapped[str] = mapped_column(String(512))
