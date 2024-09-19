from pydantic import BaseModel, Field

class TransactionDomain(BaseModel):
    amount: float = Field(description="The amount needed for the transaction", default=1000,ge=0)
    receiver_or_sender:str = Field(description="The receiver or sender of the transaction", default="CITCO")
    description:str = Field(description="Description of the transaction", default="Payout")
    account_number:str = Field(description="The account number of sender or receiver", default=12345678, ge=9999999, le=99999999)