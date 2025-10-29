# Custom Logger Module

This module provides a standardised logging setup with coloured output for different log levels, using Python's built-in `logging` module and `colorama`.

## Features

- Colour-coded log levels (INFO, WARNING, ERROR, etc.)
- Customisable log format and date format
- Easy integration across internal projects
- No external publishing required

## Usage

```python
from logger import get_logger

log = get_logger(__name__)
log.info("This is an info message.")
log.error("This is an error message.")
