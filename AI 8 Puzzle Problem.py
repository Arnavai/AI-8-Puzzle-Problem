import math
import numpy as np

#Taking Initial State as input
l=list(map(int,input("Enter the Intitial State as a a space separated list : ").split())) 
Initial = np.array(l).reshape(3,3) 

#Standard Final State we want to achieve
l2=list(map(int,input("Enter the Final State you want to achieve as space separated list : ").split()))
Final = np.array(l2).reshape(3,3) 

#Function to Create the 4 possible next states
def moves_array(array):
	Final = np.array(l2).reshape(3,3)
	possible_moves = []
	possible_arrays = {}
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i][j] == 0:

				#Creating 'up' state if possible by swapping the 0 and the upper element
				if i > 0:
					up_array = array.copy()
					up_array[i][j], up_array[i-1][j] = up_array[i-1][j], up_array[i][j]
					if not np.array_equal(up_array, Initial):
						possible_arrays["Up"] = up_array 

				#Creating 'Down' state if possible by swapping the 0 and the lower element
				if i < len(array) - 1:
					down_array = array.copy()
					down_array[i][j], down_array[i+1][j] = down_array[i+1][j], down_array[i][j]
					if not np.array_equal(down_array, Initial):
						possible_arrays["Down"] = down_array

				#Creating 'Right' state if possible by swapping the zero and the right element
				if j < len(array) - 1:
					right_array = array.copy()
					right_array[i][j], right_array[i][j+1] = right_array[i][j+1], right_array[i][j]
					if not np.array_equal(right_array, Initial):
						possible_arrays["Right"] = right_array

				#Creating 'Left' state if possible by swapping the zero and the left element 
				if j > 0 :
					left_array = array.copy()
					left_array[i][j], left_array[i][j-1] = left_array[i][j-1], left_array[i][j]
					if not np.array_equal(left_array, Initial):
						possible_arrays["Left"] = left_array

	return possible_arrays

#displacement_value by calculating number of misplaced tiles for each of the possible arrays
def disp_value(array):
	s = sum(abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3)
        for i, val in enumerate(array.reshape(1,9)[0]) if val)
	
	return s

def main():
	previously_moved = []
	array = Initial.copy()
	temp = None
	count = 0

	while True:
		h={}
		if temp is not None:
			array = temp

		act = moves_array(array)

		for keys, values in act.items():
			h[keys]=disp_value(values)
			

		#find the smallest h value and its key in the dict
		new_dic =  dict(sorted(h.items(), key=lambda item: item[1]))
		res = list(new_dic.items())[0]
		r, v = res[0], res[1]

		if not previously_moved:
			previously_moved.append(['Initial_array', array])

		else:
			for i in range(len(previously_moved)):
					if np.array_equal(act[r], previously_moved[i][1]):
					#Checking if the 2nd value in dictionary is the lowest or not
					#We take only the two smallest ones
						new_h = list(new_dic.items())[1]
						r, v = new_h[0], new_h[1]

		#To check  if the number of steps is under 100 else breaking out of the loop
		if(count>1000):
			print("Unsolvable in under 100 steps!")
			break

		#To check if the current state is equal to the final state
		if np.array_equal(act[r], Final):
			print("\n")
			#if number of steps is less than 50 then printing each intermediate state
			if(count<50):
				print('''Problem can be solved in under 50 steps and the steps included are : \n''')
				previously_moved.append([res[0], act[r]])
				for i in previously_moved:
					print("Move "+str(i[0]))
					print(i[1])
					print("\n")
			#If number of steps is greater than or equal to 50 then just printing the number of steps
			print("Total Number of Steps Taken to Solve are : ", count)
			break

		#To move on to the next state if final state is not achieved
		else:
			previously_moved.append([r, act[r]])
			temp = act[r]
			count=count+1
main()
