import os
from flask_paginate import get_page_args
from typing import Tuple

def setup_pagination() -> Tuple[int, int, int]:
    """
    This function sets up pagination
    """
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 4
    offset = (page - 1) * 4
    return offset, per_page, page