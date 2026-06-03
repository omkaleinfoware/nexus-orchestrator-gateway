import uuid

jobs = {}


def create_job(pipeline: str):

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "id": job_id,
        "pipeline": pipeline,
        "status": "queued"
    }

    return jobs[job_id]


def get_job(job_id: str):

    return jobs.get(job_id)


def update_job_status(
    job_id: str,
    status: str
):

    if job_id not in jobs:
        return None

    jobs[job_id]["status"] = status

    return jobs[job_id]