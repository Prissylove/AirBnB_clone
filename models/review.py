#!/usr/bin/env python3
"""
    Module containing the review details
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review model inherits the base model
    """
    place_id = ""
    user_id = ""
    text = ""
