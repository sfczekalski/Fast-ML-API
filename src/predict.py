"""Predict module."""

from typing import List


def _predict(texts: List[str]) -> List[str]:
    """Dummy predict.

    Args:
        texts (List[str]): Input texts.

    Returns:
        List[str]: Predictions.
    """
    return ["Prediction"] * len(texts)
