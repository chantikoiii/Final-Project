import setup
import random

list = random.sample(range(1,99999),10000)

for i in range(5):
    setup.quickTimer(list)


for i in range(5):
    setup.selectTimer(list)