a = "I am human being"
b = "I am good"
c = "good graders study well"
d = "Humans love graders"
e = "Every human does not study well"
print("ask me a question:")
ques = "Is every human good grader"
print(ques)
p = a.split()
q = b.split()
r = c.split()
s = d.split()
t = e.split()
available_data = set(p+q+r+s+t)

# machine matches the available data with the question and provides knowledge

relating_knowledge = ["every","human","study well","good grader"]
w = relating_knowledge[0]
x = relating_knowledge[1]
y = relating_knowledge[2]
z = relating_knowledge[3]


# All possibilities are checked by the machine

possibilities = [[(w,1),(x,1),(y,0),(z,0)],[(w,1),(x,1),(y,1),(z,1)],[(w,0),(x,1),(y,1),(z,1)],[(w,0),(x,0),(y,0),(z,1)]]

# now we have to find "and" of every and human and their implication to good grader

conclusion1 = not(possibilities[0][0][1] and possibilities[0][1][1]) or possibilities[0][3][1]

flag = 1

for i in range(0,len(possibilities)):
    conclusion2 = not(possibilities[i][0][1] and possibilities[i][1][1]) or possibilities[i][3][1]
    if(conclusion1 == conclusion2):
        continue
    else:
        print("No")
        flag = 0
        break;

if(flag==1):
    print("Yes")



