total_score = 0
count = 0
# the while loop 
# while it is true 
while True:
    score_input = input("Enter a grade between 0 and 100: ")
    # if the user enters 'stop'
    # break 
    if score_input.lower() == 'stop':
        break
    # convert the string into integer    
    score = int(score_input)
    
    if score >= 0 and score <= 100:
        # if it is valid grade 
        # add to the total score 
        total_score += score
        # increase the count 
        count += 1

if count>0:
    # calculate the average 
    average_score  = total_score / count
    # print the average
    print("Your average grade is:", average_score)
else:
    print("No grades entered!")


i=lo
while i<=hi:
    result +=i
    i+=1
