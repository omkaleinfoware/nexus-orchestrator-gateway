PIPELINES = {
    "salesos": {
        "name": "SalesOS",
        "url": "http://localhost:9001"
    },
    "auditos": {
        "name": "AuditOS",
        "url": "http://localhost:9002"
    },
    "healthos": {
        "name": "HealthOS",
        "url": "http://localhost:9003"
    }
}


def get_pipeline(slug: str):
    return PIPELINES.get(slug)