#!/usr/bin/env python3
# Author: Tanishq Kedare
# Author ID: tskedare
# Date Created: 2024/09/19

import sys

timer = int(sys.argv[1])  # Get the timer value from command line argument

while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')

