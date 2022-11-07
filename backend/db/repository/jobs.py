from sqlalchemy.orm import Session

from backend.db.models.jobs import Job
from backend.schemas.jobs import JobCreate


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object


def retrieve_job(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).first()
    return item
