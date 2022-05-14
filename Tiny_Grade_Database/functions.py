# GPA Database
# functions.py
# Official Name: Yiheng Lu
# Nick Name: Louis
# Lab Section: M3
# Login Name: ylu187

from random import randrange
import ast


# This function reads the user data from the file
def dataRead():
    infile = open("userdata.txt", "r")  # (IFL)
    username = []
    password = []
    for line in infile:
        line = line.split()
        username.append(line[0])
        password.append(line[1])
    infile.close()
    return username, password


# This function stores the user data into the file
def dataStore(name, word, username, password):
    outfile = open("userdata.txt", "w")  # (OPF)
    username.append(name)
    password.append(word)
    for i in range(len(username)):
        print(username[i], end=" ", file=outfile)
        print(password[i], file=outfile)
    outfile.close()


# This function check whether the user is in the database
def checkIn(name, word):
    username, password = dataRead()
    for i in range(len(username)):
        if username[i] == name:
            if password[i] == word:
                return True


# This function gets the index of a user
def getIndex(name):
    username, password = dataRead()
    index = username.index(name)
    return index


# This function reads the grades in the file
def gradesRead():
    infile = open('usergrade.txt', 'r')  # (IPF)
    grades = []
    for line in infile:
        grades.append(line)
    infile.close()
    return grades


# This function stores the grade into the file
def gradesStore(grade, subject, index):
    grades = gradesRead()
    outfile = open('usergrade.txt', 'w')  # (OPF)
    aList = []
    aList.append(index)
    aList.append(subject)
    aList.append(grade)
    grades.append(aList)
    print(grades[0], end="/", file=outfile)
    print(grades[1], end="", file=outfile)
    outfile.close()


# This function return a list that stores all the grades of one user
def findGrade(index):
    grades = gradesRead()
    grades = grades[0].split("/")
    temp = []
    aList = []
    for i in range(len(grades)):
        a = ast.literal_eval(grades[i])
        temp.append(a)
    for i in range(len(temp)):
        if temp[i][0] == index:
            aList.append(temp[i])
    return aList


# This function checks the validity of input in login page
def checkValidL(name, word):
    if name == "":
        return "False1"
    elif word == "":
        return "False2"
    else:
        return "True"


# This function checks the validity of input in signup page
def checkValidS(name, word1, word2):
    username, password = dataRead()
    if name == "":
        return "False1"
    if word1 == "" or word2 == "":
        return "False2"
    for i in range(len(username)):
        if name == username[i]:
            return "False4"
    if word1 == word2:
        return "True"
    else:
        return "False3"


# This function checks whether the user had entered the subject in to database before
def checkValidG(index, subject):
    grades = gradesRead()
    grades = grades[0].split("/")
    aList = []
    for i in range(len(grades)):
        item = ast.literal_eval(grades[i])
        aList.append(item)
    exist = False
    for i in range(len(aList)):
        if aList[i][0] == index:
            if aList[i][1] == subject:
                exist = True
                break
    if exist:
        return True
    else:
        return False


# This function changes user's percentage grade into GPA grade
def processGPA(pGrade):
    pGrade = float(pGrade)
    if pGrade >= 93:
        cgpa = "A"
    elif pGrade >= 90:
        cgpa = "A-"
    elif pGrade >= 87:
        cgpa = "B+"
    elif pGrade >= 83:
        cgpa = "B"
    elif pGrade >= 80:
        cgpa = "B-"
    elif pGrade >= 77:
        cgpa = "C+"
    elif pGrade >= 73:
        cgpa = "C"
    elif pGrade >= 70:
        cgpa = "C-"
    elif pGrade >= 60:
        cgpa = "D"
    else:
        cgpa = "F"
    dgpa = (pGrade / 100) * 4
    dgpa = round(dgpa, 2)
    return cgpa, dgpa


# This function computes and returns the next exam score required for the user to achieve better GPA
def processScore(pGrade, target):
    if target == "False":
        return "False"
    else:
        exam = (target - pGrade * 0.85) / 0.15
        exam = round(exam, 2)
        return exam


# This function checks the targeted next level of GPA of the user
def getTarget(pGrade):
    cgpa, dgpa = processGPA(pGrade)
    if cgpa == "A":
        return "False"
    elif cgpa == "A-":
        dgpa = 93
        return dgpa
    elif cgpa == "B+":
        dgpa = 90
        return dgpa
    elif cgpa == "B":
        dgpa = 87
        return dgpa
    elif cgpa == "B-":
        dgpa = 83
        return dgpa
    elif cgpa == "C+":
        dgpa = 80
        return dgpa
    elif cgpa == "C":
        dgpa = 77
        return dgpa
    elif cgpa == "C-":
        dgpa = 73
        return dgpa
    elif cgpa == "D":
        dgpa = 70
        return dgpa
    else:
        dgpa = 60
        return dgpa


# This function returns the first element of a list
def takeFirst(aList):
    return float(aList[0])


# This function processes the ranking by sorting the list
def processRanking(subject):
    grades = gradesRead()
    grades = grades[0].split("/")
    rank = []
    temp = []
    for i in range(len(grades)):
        a = ast.literal_eval(grades[i])
        temp.append(a)
    for i in range(len(temp)):
        if temp[i][1] == subject:
            aList = (temp[i][2], temp[i][0])
            rank.append(aList)
    rank.sort(key=takeFirst, reverse=True)
    if len(rank) < 5:
        return "False"
    else:
        username, password = dataRead()
        first = username[int(rank[0][1])], rank[0][0]
        second = username[int(rank[1][1])], rank[1][0]
        third = username[int(rank[2][1])], rank[2][0]
        forth = username[int(rank[3][1])], rank[3][0]
        fifth = username[int(rank[4][1])], rank[4][0]
        aList = [first, second, third, forth, fifth]
        return aList


# This function sorts the grade in descending order
def sortGrade(subject):
    grades = gradesRead()
    grades = grades[0].split("/")
    rank = []
    temp = []
    for i in range(len(grades)):
        a = ast.literal_eval(grades[i])
        temp.append(a)
    for i in range(len(temp)):
        if temp[i][1] == subject:
            aList = (temp[i][2], temp[i][0])
            rank.append(aList)
    rank.sort(key=takeFirst, reverse=True)
    return rank


# This function uses random to generate comment for users with different grade level
def getComment(pGrade):
    commentA1 = "Nice work! Wish you keep it up."
    commentA2 = "You've done a great job!"
    commentA3 = "You are a top student!"
    commentB1 = "Keep working, you can get better!"
    commentB2 = "It's good, but you can be better."
    commentB3 = "Give yourself a higher goal!"
    commentO1 = "Don't give up!"
    commentO2 = "Things will get better if you keep working."
    commentO3 = "Grade is never the main thing to judge a person."

    commentA = [commentA1, commentA2, commentA3]
    commentB = [commentB1, commentB2, commentB3]
    commentO = [commentO1, commentO2, commentO3]

    a = randrange(0, 3)  # (RND)

    pGrade = float(pGrade)
    if pGrade >= 90:
        return commentA[a]
    elif 80 <= pGrade < 90:
        return commentB[a]
    else:
        return commentO[a]
