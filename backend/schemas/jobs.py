from typing import Optional

from pydantic import BaseModel

from datetime import date, datetime


class JobBase(BaseModel):
    """
    Shared properties
    """
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


class JobCreate(JobBase):
    """
    Used to validate data while creating a Job
    """
    title: str
    company: str
    location: str
    description: str


class ShowJob(JobBase):
    """
    Used to format the response to not to have id, owner_id etc
    """
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    class Config():
        """
        To convert non dict obj to json
        """
        orm_mode = True

