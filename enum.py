# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")
# Python program to print Even Numbers in a List

# list of numbers
list2 = [10, 24, 4, 45, 66, 93]
num = 0

# using while loop
while(num < len(list2)):

	# checking condition
	if list2[num] % 2 == 0:
		print(list2[num], end=" ")

	# increment num
	num += 1
