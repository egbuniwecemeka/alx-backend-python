#!/usr/bin/env python3

import math


floor = __import__('2-floor').floor

ans = floor(3.14)
print(ans == floor(3.14))
print(floor.__annotations__)
print(f" floor(3.14) returns {ans}, which is a {type(ans)}")