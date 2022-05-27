print([i**3 for i in range(6)])  # simple list comprehension
print({i:i**2 for i in range(4)})  # simple dictionary comprehension
print([i if i%2==0 else i*2 for i in range(6)])  # comprehension with ternary operator
print([(i,j) for i in range(3) for j in range(4)])  # nested loop
print([num for num in range(51) if num%2==0 if num%5==0])  # validation at end
nums = [2,6,7,12,14,18,20,23,30]
print(["small" if num < 20 else "large" for num in nums if num%2==0 if num%3==0])
# ternary at beginning is one part, for followed by 2 conditions is another which is executed first
