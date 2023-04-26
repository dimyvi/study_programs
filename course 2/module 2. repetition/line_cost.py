from math import ceil

count = len(input())
print(int((count * 0.6) // 1), 'р.', ceil(float((count * 0.6) % 1) * 100), 'коп.')