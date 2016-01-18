#Initialization
credits = []
credits_flo = []
letters = []
points = []

#read txt file
f = open('data.txt','r')
lines = f.readlines()
for line in lines:
    words = line.split()
    credits.append(words[1])
    letters.append(words[2])

f.close()

# convert letters to points
for letter in letters:
    if letter == 'A+':
        points.append(4.0)
    elif letter == 'A':
    	points.append(4.0)
    elif letter == 'A-':
        points.append(3.7)
    elif letter == 'B+':
        points.append(3.3)
    elif letter == 'B':
    	points.append(3.0)
    elif letter == 'B-':
    	points.append(2.7)
    elif letter == 'C+':
    	points.append(2.3)
    elif letter == 'C':
    	points.append(2.0)
    else: #D
    	points.append(1.0)

# convert credits to credits_flo
for credit in credits:
	credits_flo.append(float(credit))

# calculate GPA
gpa = 0.0
for i in range(len(credits)):
    gpa = gpa + credits_flo[i] * points[i]

gpa = gpa / sum(credits_flo)

#output
print('The GPA is ' + '%.3g'%gpa)
