# Porgramming in Python, by Mohammed Alhamid
#
# Feb 21, 2018.
""" Making a prototype of allowing making an online exam where we have a limit of time answering a given question."""
from datetime import datetime
## The only variables you might need to solve this question are:
# "question" is the exam question variable. 
# "response" is the student response string
# time1 is the first timestamp string of delivering the question to the student.
# time2 is the second timestamp string
# tseconds is a variable that counts the number of seconds differences between time1 and time2. 

###### Only add code below this line ##############################
x = input('Press the return key when you are ready.')
question = "What is the capital city of Hungary?"
prompt1='Question 1: '
prompt2='Enter the response to the question as fast as you can: \n'
print ('\n' + prompt1 + question + '\n') # get colons lined up
# First time stamp...
#time1 = str(datetime.now())
time1 = datetime.now()
response = input(prompt2)
# Second time stamp
time2 = datetime.now()

tseconds = (time2-time1).total_seconds()
# Display the two timestamps...
print ('\n' + str(time1) + '\n' + str(time2))

if response == "Budapest" and tseconds<=10.0:
	print ("Your answer is correct ")
	
elif response != "Budapest": 
	print("Your answer is wrong " )
else:
	print ("You took longer time to answer the question")
	








