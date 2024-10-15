# 0x01. Python - Async

Setup environment

1. Python environment (Virtual environment)
    - python3.7 -m venv ./py37async
    -source bin/activate 
2. aiohttp and aiofiles packages (Optional: aiodns)
    - pip install --upgrade pip aiohttp aiofiles (aiodns)


## the asyncio Package

    - It has two keywords async and await
    - At the heart of async IO are coroutines
    - A coroutine is a specialized version of a Python generator function
    - A coroutine is a function that suspends its execution before reaching **return** and can indirectly pass control to another function for some time
