# Temperature Threshold Counter
# Goal: Use a value-based loop to iterate through a list and count specific values.

temps = [71, 65, 80, 74, 59]
count = 0
for temp in temps:
    if temp >= 75:
        count += 1
print("Hot days:", count)
