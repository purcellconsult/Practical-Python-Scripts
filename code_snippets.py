x, y = 10, 20
if x < y:
    print("this is printed...")

file_size = 100
if file_size >= 100:
    print("Not enough space")
else:
    print("Enough space")

for x in range(1, 11):
    print(x * 2)

i = 1
while i < 11:
    print(f"i = {i}")
    i += 1


def double_a_number():
    return x * 2


print(double_a_number())  # view the output

data = [5, 20, 100, 17, 55, 93, 201]
print(data[0])  # 5
print(data[-1])  # 201
data.append(100)  # [5, 20, 100, 17, 55, 93, 201, 100]
print(data)  # [5, 20, 100, 17, 55, 93, 201, 100]
