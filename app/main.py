from app.router.dispatcher import dispatch
from app.router.pipeline_registry import get_pipeline
from app.auth.scope_guard import validate_scope
from fastapi import FastAPI
from app.router.job_manager import (
    create_job,
    get_job,
    update_job_status
)

from app.auth.jwt_handler import (
    create_token,
    verify_token
)

app = FastAPI(
    title="Nexus Gateway",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "Nexus Gateway Running"
    }


@app.get("/token")
def generate_token():

    payload = {
        "sub": "sales-app",
        "pipeline_scopes": ["salesos"]
    }

    token = create_token(payload)

    return {
        "token": token
    }


@app.get("/verify")
def verify():

    payload = {
        "sub": "sales-app",
        "pipeline_scopes": ["salesos"]
    }

    token = create_token(payload)

    decoded = verify_token(token)

    return decoded

@app.get("/salesos")
def salesos():

    payload = {
        "sub": "sales-app",
        "pipeline_scopes": ["salesos"]
    }

    validate_scope(
        payload,
        "salesos"
    )

    return {
        "message": "SalesOS Access Granted"
    }

@app.get("/auditos")
def auditos():

    payload = {
        "sub": "sales-app",
        "pipeline_scopes": ["salesos"]
    }

    validate_scope(
        payload,
        "auditos"
    )

    return {
        "message": "AuditOS Access Granted"
    }

@app.get("/pipeline/{slug}")
def pipeline(slug: str):

    result = get_pipeline(slug)

    return result


@app.get("/dispatch/{slug}")
def dispatch_request(slug: str):

    return dispatch(slug)


@app.post("/jobs/{pipeline}")
def create_new_job(pipeline: str):

    return create_job(pipeline)


@app.get("/jobs/{job_id}")
def get_job_status(job_id: str):

    return get_job(job_id)

@app.put("/jobs/{job_id}/{status}")
def update_status(
    job_id: str,
    status: str
):

    return update_job_status(
        job_id,
        status
    )