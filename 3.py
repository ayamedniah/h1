import json
counter=0
with open("Question_file.json","r") as Question_file:
    Question_D = json.load(Question_file)
with open("Answers_file.json","r") as Answers_file:
    Answers_D = json.load(Answers_file)
student_answer=[]
for key,value in Question_D.items():
    print(str(key)+str(value))
    x=input("enter answer")
    student_answer.append(x)

for i in range(0,20):
    if student_answer[i]==Answers_D[i]:
        counter+=1
student_name=input("enter your name: ")
print("your reselt " + str(counter))
with open("mark.json","w") as s_mark:
    mark_D = json.dumps({student_name:counter})
    s_mark.write(mark_D)