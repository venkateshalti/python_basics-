input_list = []
while True:
    current_value = input("enter value to be listed:")
    if current_value:
        input_list.append(current_value)
    else:
        break
print(input_list)

# implementing for loop with an optional else
for i in range(1, 5):
    if i % 5 == 0:
        break
else:  # else executes because the loop failed to break
    print("couldn't find even one number divisible by 5")
