from app.router.pipeline_registry import get_pipeline


def dispatch(slug: str):

    pipeline = get_pipeline(slug)

    if not pipeline:
        return {
            "error": "Pipeline not found"
        }

    return {
        "pipeline": pipeline["name"],
        "target_url": pipeline["url"],
        "status": "ready_to_dispatch"
    }