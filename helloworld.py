import random
import statistics

print('Emerson Pfeiffer')

x = random.randint(0, 100)
y = random.randint(0, 100)
data = [x, y]

print(x)
print(y)
print('Sum = ' + str(x + y))
print('Average = ' + str(statistics.mean(data)))
