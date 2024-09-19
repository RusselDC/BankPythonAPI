from pydantic import BaseModel, Field

class RegisterDetails(BaseModel) :
    card_number: int = Field(desription="The number for your bank account"c)
    name: str = Field(description="Name of the account holder", default="Juan Dela Cruz")
    pin_code : int = Field(description="Pin code for your account", default=0000, ge=999, le=9999)