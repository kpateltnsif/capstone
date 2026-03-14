from pydantic import BaseModel

class StudentData(BaseModel):

    hours_studied: float
    previous_scores: float
    extracurricular_activities: int
    sleep_hours: float
    sample_papers_practiced: float