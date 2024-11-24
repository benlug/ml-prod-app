"""
This module defines the database models for the Rent Apartments application using SQLAlchemy ORM.
Classes:
    Base: A base class for all declarative models.
    RentApartments: A model representing the rent apartments table in the database.
"""

from sqlalchemy import REAL, INTEGER, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from config import db_settings


class Base(DeclarativeBase):
    """
    A base class for all declarative models.
    """

    pass


class RentApartments(Base):
    """
    A model representing the rent apartments table in the database.
    Attributes:
        address (str): The address of the apartment, primary key.
        area (float): The area of the apartment in square meters.
        constraction_year (int): The year the apartment was constructed.
        rooms (int): The number of rooms in the apartment.
        bedrooms (int): The number of bedrooms in the apartment.
        bathrooms (int): The number of bathrooms in the apartment.
        balcony (str): Indicates if the apartment has a balcony.
        storage (str): Indicates if the apartment has storage space.
        parking (str): Indicates if the apartment has parking space.
        furnished (str): Indicates if the apartment is furnished.
        garage (str): Indicates if the apartment has a garage.
        garden (str): Indicates if the apartment has a garden.
        energy (str): The energy rating of the apartment.
        facilities (str): The facilities available in the apartment.
        zip (int): The ZIP code of the apartment's location.
        neighborhood (int): The neighborhood code of the apartment's location.
        rent (int): The rent amount for the apartment.
    """

    __tablename__ = db_settings.rent_apart_table_name

    address: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[int] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR())
    storage: Mapped[str] = mapped_column(VARCHAR())
    parking: Mapped[str] = mapped_column(VARCHAR())
    furnished: Mapped[str] = mapped_column(VARCHAR())
    garage: Mapped[str] = mapped_column(VARCHAR())
    garden: Mapped[str] = mapped_column(VARCHAR())
    energy: Mapped[str] = mapped_column(VARCHAR())
    facilities: Mapped[str] = mapped_column(VARCHAR())
    zip: Mapped[int] = mapped_column(VARCHAR())
    neighborhood: Mapped[int] = mapped_column(VARCHAR())
    rent: Mapped[int] = mapped_column(INTEGER())
