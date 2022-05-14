# GPA Database
# report.py
# Official Name: Yiheng Lu
# Nick Name: Louis
# Lab Section: M3
# Login Name: ylu187

from Final_Project import functions


# This class prints a report into report.txt
class Report:  # (CLOD)
    def __init__(self, index):
        username, password = functions.dataRead()  # (FNC)
        grade = functions.findGrade(index)  # (FNC)
        aList = []
        for i in range(len(grade)):
            temp = grade[i][1], grade[i][2]
            aList.append(temp)
        self.name = username[index]
        self.grades = aList

    def checkValid(self):
        grades = self.grades
        if len(grades) == 0:
            return False
        else:
            return True

    def display(self):
        outfile = open("report.txt", "w")  # (OPF)
        print("Username: " + self.name, file=outfile)
        print("Subjects in database:", len(self.grades), file=outfile)
        print("\n", file=outfile)
        grades = self.grades
        for i in range(len(grades)):
            subject = grades[i][0]
            print("Subject: " + subject, file=outfile)
            grade = grades[i][1]
            print("Grade: " + str(grade), file=outfile)
            comment = functions.getComment(float(grade))  # (FNC)
            print("Comment: " + comment, file=outfile)
            print("\n", file= outfile)
        outfile.close()
