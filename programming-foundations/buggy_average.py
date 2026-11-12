count = 1
total = 0
while count <= 3:
    score = float(input("Enter score: "))
    count += 1
    total = total + score
average = total / 3
if average >= 75:
    print("PASSED")
else:
    print("FAILED")
print(f"Average: {average:.2f}")