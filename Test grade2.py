total =0
count = 0
while True:
    score = input("Enter grade(0-100): ")
    if (0<= score, score<=100):
        total += float(score)
        count += 1
    elif score == 'stop':
        break
print("Average score is", total / count)



#    if score == 'stop':
#        break
#    else:
#        total += float(score)
#        count += 1
#print("Average score is", total / count)#

#initializing average as 0
#average=0
#initializing count as 0
#count=0
#accepting grade
#grade=input()
#looping till stop is encoundered
#while(grade!="stop"):
#    average+=float(grade)#adding grade to average
#    count+=1 #incrementing count
#    grade=input()#accepting grade
#printing Average
#print("Average is",average/count)


grades = input()
counter = 0
sum = 0

while grades != 'stop':
    sum += int(grades)
    counter += 1
    grades = input()

print(sum / counter)
