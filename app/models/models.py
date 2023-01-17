from pydantic import BaseModel



class ConversionData(BaseModel):
    from_currency: str
    to_currency: str
    original_amount: float
    converted_amount: float



class StudentSchema(BaseModel):
    fullname: str
    email: str
    course_of_study: str 
    year: 
    gpa: float

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }
