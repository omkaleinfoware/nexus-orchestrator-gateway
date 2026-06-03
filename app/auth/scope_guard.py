from fastapi import HTTPException


def validate_scope(
    token_payload: dict,
    pipeline: str
):

    scopes = token_payload.get(
        "pipeline_scopes",
        []
    )

    if pipeline not in scopes:

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return True