# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:
	
	# checking condition
	if num % 2 != 0:
	print(num, end = " ")
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
i = 0

# using while loop		
while(i < len(list1)):
	
	# checking condition
	if list1[i] % 2 != 0:
		print(list1[i], end = " ")
	
	# increment i
	i += 1
	
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

only_odd = [num for num in list1 if num % 2 == 1]

print(only_odd)
