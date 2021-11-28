"""API for model serving."""

from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict, Union

from fastapi import FastAPI, Request, status

from eloquent_matsumoto import predict as predict_module

app = FastAPI(
    title="Model serving API",
    description="Model serving API developed using FastAPI framework",
    version="0.1",
)


def add_response_metadata(function: Callable) -> Callable:
    """Add metadata (method, timestamp, url) to the response.

    Args:
        function (Callable): Function implementing a given API endpoint.

    Returns:
        Callable: Function enriched with the metadata.
    """

    @wraps(function)
    def wrapper(request: Request, *args, **kwargs) -> Dict[str, Union[str, Any]]:
        """Wrapper that adds the metadata to the original response.

        Args:
            request (Request): The request object.

        Returns:
            Dict[str, Union[str, Any]]: Endpoint function's response, with the metadata added.
        """
        # Get the reponse from the original function
        response = function(request, *args, **kwargs)

        # Construct the final response out of original response and the metadata
        response = {
            **response,
            "method": request.method,
            "url": request.url._url,
            "timestamp": datetime.now().isoformat(),
        }

        return response

    return wrapper


@app.get("/health/")
@add_response_metadata
def health(request: Request) -> Dict[str, Union[str, Any]]:
    """Health check.

    Args:
        request (Request): The request object.

    Returns:
        Dict[str, Union[str, Any]]: Health check response.
    """
    response = {
        "message": "OK",
        "status-code": status.HTTP_200_OK,
        "data": {},
    }

    return response


@app.post("/predict/")
@add_response_metadata
def predict(request: Request, payload: Any) -> Dict[str, Union[str, Any]]:
    """Predict endpoint.

    Args:
        request (Request): The request object.

    Returns:
        Dict[str, Union[str, Any]]: Prediction response.
    """
    texts = [item.text for item in payload["texts"]]

    predictions = predict_module._predict(texts)

    response = {
        "message": "OK",
        "status-code": status.HTTP_200_OK,
        "data": {
            "predictions": predictions,
        },
    }

    return response
