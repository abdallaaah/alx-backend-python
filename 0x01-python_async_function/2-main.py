#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 2
max_delay = 3

print(measure_time(n, max_delay))