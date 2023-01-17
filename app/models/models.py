from pydantic import BaseModel



class ConversionData(BaseModel):
    from_currency: str
    to_currency: str
    original_amount: float
    converted_amount: float



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
