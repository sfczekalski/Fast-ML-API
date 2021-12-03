"""Definitions of the schemas."""

from typing import List

from fastapi import Query
from pydantic import BaseModel, validator


class Text(BaseModel):
    """Schema of a correct text field."""

    text: str = Query(..., min_length=1)


class PredictPayload(BaseModel):
    """Schema of a correct predict payload."""

    texts: List[Text]

    @validator("texts")
    def texts_length_validator(cls, input: List[str]) -> List[str]:
        """Validate length of provided texts list.

        Args:
            input (List[str]): Provided texts list.

        Raises:
            ValueError: Raised if empty list was provided.

        Returns:
            List[str]: Texts list after validation.
        """
        if len(input) == 0:
            raise ValueError("Texts list cannot be empty")

        return input

    class Config:
        """Example of a correct payload."""

        schema_extra = {
            "example": {
                "texts": [
                    {"text": "Some nice example of text."},
                    {"text": "Oh, even nicer one!"},
                ]
            }
        }
