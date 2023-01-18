from pydantic import BaseModel



class Currency(BaseModel):
    currency_dict: dict[str,str]




class Convert(BaseModel):
    converted_amount: float
    rate: float
    metadata: dict 


    class Config:
        schema_extra = {
            "example": {"converted_amount":81.91,
            "rate":0.82,
            "metadata":{"time_of_conversion":"2023-01-17T00:00:00Z",
                        "from_currency":"USD","to_currency":"GBP"}}
            } 



class History(BaseModel):
    history: list



class Error(BaseModel):
    Status: str 
    Error: str