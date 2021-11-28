"""API for model serving."""

from typing import Any, Dict, Union

from fastapi import FastAPI, status

app = FastAPI(
    title="Model serving API",
    description="Model serving API developed using FastAPI framework",
    version="0.1",
)


@app.get("/health/")
def health() -> Dict[str, Union[str, Dict[str, Any]]]:
    """Health check.

    Returns:
        Dict[str, Union[str, Dict[str, Any]]]: Health check response.
    """
    response = {
        "message": "Healthy",
        "status-code": status.HTTP_200_OK,
        "data": {},
    }

    return response
