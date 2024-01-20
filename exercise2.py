

#print the task for this exercise
print("Printing current and previous number sum in a range(10)")

#store a 0 value first to the previous number
prev_num = 0

#create a for loop with a range 10 numbers 
for current in range(10):
    sum = current + prev_num #add a variable that stores the sum of the iterated current and previous number
    print("Current number is" , current , "and" , "Previous Number", prev_num,  "Sum:" , sum) #print the output 
    prev_num = current #then change the value of previous number to the iteration of current number 





