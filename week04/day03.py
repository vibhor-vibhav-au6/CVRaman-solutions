
# Q1.
# Write a Python program to round the numbers of a given list, print the minimum
# and maximum numbers and multiply the numbers by 5. Print the unique numbers
# in ascending order separated by space.
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110


def multiTasks(array):
	array.sort()
	temp = list(map(round, array))
	print ('max is: '+ str(max(temp)) 
		+ '\n' + 'min is: '+ str(min(temp)))

	# def f(a):
	#   return a*5
	# this is equivalant to the lambda function below
	return(list(map(lambda a : a*5,temp)))

# driver
l = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
print(multiTasks(l))




# Q2. Write a Python program to create a list by concatenating a given list which
# range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5'

def concatList(n, string):
	# return [c+str(i) for i in range(1,n+1) for c in string]
	# or
	return ['{}{}'.format(i, j) for j in range(1, n+1) for i in string]

# driver
n = 5
s = ['p', 'q']
print(concatList(n,s))
