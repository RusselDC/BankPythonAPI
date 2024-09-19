from pydantic import BaseModel, Field

class ServiceResponse(BaseModel):
    status:str = Field(description="status of your response", default="success")
    code:int = Field(description="Status code of your response", default=200, ge=99, le=999)
    data:str = Field(description="The data included in your response", default="Hello World")
    message:str = Field(description="Dev message", default="Default Message")
