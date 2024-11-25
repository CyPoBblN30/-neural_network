from pydantic import BaseModel
from typing import List, Dict


class  User(BaseModel):
    user_name: str
    mail: str
    address: str


class Banks(BaseModel):
    bank_name: str
    rating: int
    bank_opened: str


class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    card_opened: str


class Balance(BaseModel):
    name_card: Cards
    amount: int
    currenc: str