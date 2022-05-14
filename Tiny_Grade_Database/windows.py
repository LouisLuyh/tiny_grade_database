# GPA Database
# windows.py
# Official Name: Yiheng Lu
# Nick Name: Louis
# Lab Section: M3
# Login Name: ylu187

from graphics import *
from Final_Project import functions, report


# This function graphs the main page of the database
def graphhome1(win):  # Haven't logged in
    welcome1 = Text(Point(40, 37.5), "Welcome To")  # (OTXT)
    welcome1.setSize(22)
    welcome2 = Text(Point(40, 32.5), "GPA Database")  # (OTXT)
    welcome2.setSize(36)
    welcome2.setStyle("bold")
    welcome2.setTextColor('red')
    welcome1.draw(win)
    welcome2.draw(win)

    # Log-in button
    button1s = Rectangle(Point(15, 19.5), Point(30, 11.5))
    button1s.setFill('cyan3')
    button1s.draw(win)
    button1 = Rectangle(Point(16, 18.5), Point(29, 12.5))
    button1.setFill('cyan')
    button1.draw(win)

    # Sign-up button
    button2s = Rectangle(Point(50, 19.5), Point(65, 11.5))
    button2s.setFill('cyan3')
    button2s.draw(win)
    button2 = Rectangle(Point(51, 18.5), Point(64, 12.5))
    button2.setFill('cyan')
    button2.draw(win)

    login = Text(Point(22.5, 15.5), "Log - in")  # (OTXT)
    login.setSize(22)
    signup = Text(Point(57.5, 15.5), "Sign - up")  # (OTXT)
    signup.setSize(22)
    login.draw(win)
    signup.draw(win)

    # Quit link
    quit = Text(Point(40, 5), "Click here to quit")  # (OTXT)
    quit.setSize(18)
    quit.setStyle("italic")
    quit.setTextColor('blue')
    quit.draw(win)
    directgraphhome1(win)


# This function check the user's mouse click then call each function
def directgraphhome1(win):
    while True:
        point = win.getMouse()  # (IMS)
        if 15 <= point.getX() <= 30 and 19.5 >= point.getY() >= 11.5:
            graphlogin(win)
            break
        elif 50 <= point.getX() <= 65 and 19.5 >= point.getY() >= 11.5:
            graphsignup(win)
            break
        elif 33 <= point.getX() <= 47 and 4.2 <= point.getY() <= 5.8:
            win.close()
            break


# This function graphs the main page after user had logged in
def graphhome2(win, index):  # Logged in
    win.close()
    win = GraphWin("GPA Database", 800, 500)  # (GW)
    win.setBackground('orange')
    win.setCoords(0, 0, 80, 50)

    welcome1 = Text(Point(40, 37.5), "Welcome To")  # (OTXT)
    welcome1.setSize(22)
    welcome2 = Text(Point(40, 32.5), "GPA Database")  # (OTXT)
    welcome2.setSize(36)
    welcome2.setStyle("bold")
    welcome2.setTextColor('red')
    welcome1.draw(win)
    welcome2.draw(win)

    username, password = functions.dataRead()  # (FNC)
    name = username[index]

    text = Text(Point(40, 27), "Hello " + name + "!")  # (OTXT)
    text.setSize(22)
    text.setStyle('bold')
    text.draw(win)
    buttonhome2(win, index)


# This function draws the buttons in the main page
def buttonhome2(win, index):
    # Go to GPA calculator
    button1s = Rectangle(Point(12, 19.5), Point(33, 11.5))
    button1s.setFill('cyan3')
    button1s.draw(win)
    button1 = Rectangle(Point(13, 18.5), Point(32, 12.5))
    button1.setFill('cyan')
    button1.draw(win)

    # Go to ranking board
    button2s = Rectangle(Point(47, 19.5), Point(68, 11.5))
    button2s.setFill('cyan3')
    button2s.draw(win)
    button2 = Rectangle(Point(48, 18.5), Point(67, 12.5))
    button2.setFill('cyan')
    button2.draw(win)

    text1 = Text(Point(22.5, 15.5), "Go to GPA Calculator")  # (OTXT)
    text1.setSize(17)
    text1.setStyle('bold')
    text1.draw(win)
    text2 = Text(Point(57.5, 15.5), "See Ranking Board")  # (OTXT)
    text2.setSize(17)
    text2.setStyle('bold')
    text2.draw(win)

    report = Text(Point(40, 7), "Click here to generate report")  # (OTXT)
    report.setSize(18)
    report.setStyle('bold')
    report.setTextColor('blue')
    report.draw(win)

    text3 = Text(Point(40, 3), "Click here to log-out")  # (OTXT)
    text3.setTextColor('blue')
    text3.setSize(18)
    text3.draw(win)

    directgraphhome2(win, index)


# This function checks user's mouse and call each function
def directgraphhome2(win, index):
    while True:
        point = win.getMouse()  # (IMS)
        if 12 <= point.getX() <= 33 and 11.5 <= point.getY() <= 19.5:
            graphCalculator(win, index)
            break
        elif 47 <= point.getX() <= 68 and 11.5 <= point.getY() <= 19.5:
            subject = enterSubject()
            graphRanking1(win, subject, index)
            break
        elif 28.6 <= point.getX() <= 51.5 and 6.3 <= point.getY() <= 7.8:
            if report.Report(index).checkValid() == False:  # (CLOD)
                graphWarning("You don't have data yet!")  # (OTXT) (LOOD)
            else:
                report.Report(index).display()  # (CLOD) (LOOD)
                graphWarning("Report is in report.txt")  # (OTXT)
        elif 31.8 <= point.getX() <= 48.3 and 2.3 <= point.getY() <= 3.9:
            win.close()
            win = GraphWin("GPA Database", 800, 500)  # (GW)
            win.setCoords(0, 0, 80, 50)
            win.setBackground('orange')
            graphhome1(win)
            break


# This function asks the user to input a subject
def enterSubject():
    sub = GraphWin("Entry", 300, 70)  # (GW)
    sub.setCoords(0, 0, 30, 7)
    sub.setBackground('orange')
    text = Text(Point(6, 5.5), "Enter Subject:")  # (OTXT)
    text.setSize(15)
    text.setStyle('bold')
    text.setTextColor('red')
    text.draw(sub)
    inputbox = Entry(Point(12, 2.5), 30)  # (IEB)
    inputbox.draw(sub)

    buttons = Rectangle(Point(24, 6), Point(29, 1))
    buttons.setFill('cyan3')
    buttons.draw(sub)
    button = Rectangle(Point(24.3, 5.7), Point(28.7, 1.3))
    button.setFill('cyan')
    button.draw(sub)
    text = Text(Point(26.5, 3.5), "GO")  # (OTXT)
    text.setSize(18)
    text.setStyle('bold')
    text.draw(sub)

    while True:
        point = sub.getMouse()  # (IMS)
        if 24 <= point.getX() <= 29 and 1 <= point.getY() <= 6:
            subject = inputbox.getText()
            sub.close()
            return subject


# This function graphs the page for login
def graphlogin(win):
    win.close()
    win = GraphWin("Log-in", 800, 500)  # (GW)
    win.setBackground('orange')
    win.setCoords(0, 0, 80, 50)
    login = Text(Point(40, 35), "Log-in")  # (OTXT)
    login.setSize(36)
    login.setStyle('bold')
    login.setTextColor('red')
    login.draw(win)

    text1 = Text(Point(28, 26), "Username:")  # (OTXT)
    text1.setSize(18)
    text1.setStyle('bold')
    text1.draw(win)

    text2 = Text(Point(28, 20), 'Password:')  # (OTXT)
    text2.setSize(18)
    text2.setStyle('bold')
    text2.draw(win)

    inputbox1 = Entry(Point(45, 26), 30)  # Username  # (IEB)
    inputbox1.draw(win)
    inputbox2 = Entry(Point(45, 20), 30)  # Password  # (IEB)
    inputbox2.draw(win)

    button1 = Rectangle(Point(35, 14), Point(45, 11))
    button1.setFill('cyan')
    button2 = Rectangle(Point(34.5, 14.5), Point(45.5, 10.5))
    button2.setFill('cyan3')
    button2.draw(win)
    button1.draw(win)

    text3 = Text(Point(40, 12.5), "Log-in")  # (OTXT)
    text3.setSize(18)
    text3.setStyle('bold')
    text3.draw(win)

    text4 = Text(Point(40, 5), "Don't have account? Click here to sign-up")  # (OTXT)
    text4.setStyle('italic')
    text4.setSize(15)
    text4.setTextColor('blue')
    text4.draw(win)
    directLogin(win, inputbox1, inputbox2)


# This function check user's mouse click in login page and call functions
def directLogin(win, inputbox1, inputbox2):
    while True:
        point = win.getMouse()  # (IMS)
        if 34.5 <= point.getX() <= 45.5 and 14.5 >= point.getY() >= 10.5:
            name = inputbox1.getText()
            word = inputbox2.getText()
            justification = functions.checkValidL(name, word)  # (FNC)
            if justification == "False1":
                graphWarning("Username is empty!")  # (OTXT)
            elif justification == "False2":
                graphWarning("Password is empty!")  # (OTXT)
            else:
                justification = functions.checkIn(name, word)  # (FNC)
                if not justification:
                    graphWarning("Username or Password incorrect!")  # (OTXT)
                else:
                    index = functions.getIndex(name)  # (FNC)
                    graphhome2(win, index)
                    break
        elif 26.5 <= point.getX() <= 53.7 and 4.3 <= point.getY() <= 5.8:
            graphsignup(win)
            break


# This function graphs the page for sign ups
def graphsignup(win):
    win.close()
    win = GraphWin("Sign-up", 800, 500)  # (GW)
    win.setBackground('orange')
    win.setCoords(0, 0, 80, 50)

    signup = Text(Point(40, 35), "Sign-up")  # (OTXT)
    signup.setTextColor('red')
    signup.setSize(36)
    signup.setStyle('bold')
    signup.draw(win)

    inputbox1 = Entry(Point(45, 27), 30)  # Username  # (IEB)
    inputbox1.draw(win)
    inputbox2 = Entry(Point(45, 22), 30)  # Password  # (IEB)
    inputbox2.draw(win)
    inputbox3 = Entry(Point(45, 17), 30)  # Re-entered Password  # (IEB)
    inputbox3.draw(win)
    buttonSignup(win, inputbox1, inputbox2, inputbox3)


# This function draws the buttons in the signup page
def buttonSignup(win, inputbox1, inputbox2, inputbox3):
    text1 = Text(Point(28, 27), "Username:")  # (OTXT)
    text1.setSize(18)
    text1.setStyle('bold')
    text1.draw(win)
    text2 = Text(Point(28, 22), "Password:")  # (OTXT)
    text2.setSize(18)
    text2.setStyle('bold')
    text2.draw(win)
    text3 = Text(Point(24, 17), "Re-enter Password:")  # (OTXT)
    text3.setSize(18)
    text3.setStyle('bold')
    text3.draw(win)

    button1 = Rectangle(Point(35, 12), Point(45, 9))
    button1.setFill('cyan')
    button2 = Rectangle(Point(34.5, 12.5), Point(45.5, 8.5))
    button2.setFill('cyan3')
    button2.draw(win)
    button1.draw(win)

    text3 = Text(Point(40, 10.5), "Sign-up")  # (OTXT)
    text3.setSize(18)
    text3.setStyle('bold')
    text3.draw(win)

    text4 = Text(Point(40, 5), "Had account? Click here to Log-in")  # (OTXT)
    text4.setStyle('italic')
    text4.setSize(15)
    text4.setTextColor('blue')
    text4.draw(win)
    directSignup(win, inputbox1, inputbox2, inputbox3)


# This function checks the user's mouse click in signup page and call functions
def directSignup(win, inputbox1, inputbox2, inputbox3):
    while True:
        point = win.getMouse()  # (IMS)
        if 34.5 <= point.getX() <= 45.5 and 8.5 <= point.getY() <= 12.5:
            name = inputbox1.getText()
            word1 = inputbox2.getText()
            word2 = inputbox3.getText()
            justification = functions.checkValidS(name, word1, word2)  # (FNC)
            if justification == "True":
                username, password = functions.dataRead()  # (FNC)
                functions.dataStore(name, word1, username, password)  # (FNC)
                index = functions.getIndex(name)  # (FNC)
                graphhome2(win, index)
                break
            elif justification == "False1":
                graphWarning("Username is empty!")  # (OTXT)
            elif justification == "False2":
                graphWarning("Password is empty!")  # (OTXT)
            elif justification == "False4":
                graphWarning("Username already taken!")  # (OTXT)
            else:
                graphWarning("Passwords do not match!")  # (OTXT)
        elif 29 <= point.getX() <= 51.3 and 4 <= point.getY() <= 5.7:
            graphlogin(win)
            break


# This function graphs the page for calculator
def graphCalculator(win, index):
    win.close()
    win = GraphWin("GPA Calculator", 800, 500)  # (GW)
    win.setBackground('orange')
    win.setCoords(0, 0, 80, 50)

    text1 = Text(Point(40, 40), "GPA Calculator")  # (OTXT)
    text1.setSize(36)
    text1.setStyle('bold')
    text1.setTextColor('red')
    text1.draw(win)
    buttonCalculator(win, index)


# This function draws the buttons in the calculator page
def buttonCalculator(win, index):
    inputbox1 = Entry(Point(45, 32), 30)  # Subject  # (IEB)
    inputbox1.draw(win)
    inputbox2 = Entry(Point(45, 27), 30)  # Percentage Grade  # (IEB)
    inputbox2.draw(win)

    text2 = Text(Point(28.5, 32), "Subject:")  # (OTXT)
    text2.setSize(18)
    text2.setStyle('bold')
    text2.draw(win)
    text3 = Text(Point(24, 27), "Percentage Grade:")  # (OTXT)
    text3.setSize(18)
    text3.setStyle('bold')
    text3.draw(win)

    # Process Button
    button1s = Rectangle(Point(62, 29), Point(73, 25))
    button1s.setFill('cyan3')
    button1s.draw(win)
    button1 = Rectangle(Point(62.5, 28.5), Point(72.5, 25.5))
    button1.setFill('cyan')
    button1.draw(win)
    text4 = Text(Point(67.5, 27), "Process")
    text4.setSize(18)
    text4.setStyle('bold')
    text4.draw(win)
    commentboxCalculator(win, index, inputbox1, inputbox2)


# This function draws the comment box in the calculator page
def commentboxCalculator(win, index, inputbox1, inputbox2):
    commentbox = Rectangle(Point(1.5, 23), Point(78.5, 1.5))
    commentbox.setFill('yellow3')
    commentbox.draw(win)

    text5 = Text(Point(5.5, 22), 'Comment:')  # (OTXT)
    text5.setSize(15)
    text5.setStyle('bold')
    text5.draw(win)

    # View Specific Button
    button2s = Rectangle(Point(65, 5), Point(78, 2))
    button2s.setFill('gray')
    button2s.draw(win)
    button2 = Rectangle(Point(65.3, 4.7), Point(77.7, 2.3))
    button2.setFill('white')
    button2.draw(win)

    text6 = Text(Point(71.5, 3.5), "View Specific")  # (OTXT)
    text6.setSize(15)
    text6.setStyle('bold')
    text6.draw(win)
    directCalculator(win, inputbox1, inputbox2, index)


# This function checks the user's mouse click and call functions
def directCalculator(win, inputbox1, inputbox2, index):
    while True:
        point = win.getMouse()  # (IMS)
        if 62 <= point.getX() <= 73 and 25 <= point.getY() <= 29:
            subject = inputbox1.getText()
            pgrade = inputbox2.getText()
            if subject == "":
                graphWarning("Subject is empty!")  # (OTXT)
            if pgrade == "":
                graphWarning("Grade is empty!")  # (OTXT)
            else:
                justification = functions.checkValidG(index, subject)  # (FNC)
                if justification:
                    graphWarning("Subject grade found in database!")  # (OTXT)
                else:
                    break
    cgrade, dgrade = functions.processGPA(float(pgrade))  # (FNC)
    dgrade = str(dgrade)
    functions.gradesStore(float(pgrade), subject, index)  # (FNC)
    comment = functions.getComment(pgrade)  # (FNC)
    text = Text(Point(40, 19), "Your grade for " + subject + " is: " + cgrade + " (" + dgrade + ")")  # (OTXT)
    text.setSize(18)
    text.draw(win)
    text = Text(Point(40, 13), comment)
    text.setSize(25)
    text.setStyle('bold')
    text.draw(win)
    changeButton(win)

    while True:
        point = win.getMouse()  # (IMS)
        if 65 <= point.getX() <= 78 and 2 <= point.getY() <= 5:
            pgrade = float(pgrade)
            graphDetails(win, index, subject, pgrade)
            break


# This function changes the buttons in the calculator page
def changeButton(win):
    button2s = Rectangle(Point(65, 5), Point(78, 2))
    button2s.setFill('cyan3')
    button2s.draw(win)
    button2 = Rectangle(Point(65.3, 4.7), Point(77.7, 2.3))
    button2.setFill('cyan')
    button2.draw(win)
    text6 = Text(Point(71.5, 3.5), "View Specific")  # (OTXT)
    text6.setSize(15)
    text6.setStyle('bold')
    text6.draw(win)

    button1s = Rectangle(Point(62, 29), Point(73, 25))
    button1s.setFill('gray')
    button1s.draw(win)
    button1 = Rectangle(Point(62.5, 28.5), Point(72.5, 25.5))
    button1.setFill('white')
    button1.draw(win)
    text4 = Text(Point(67.5, 27), "Process")  # (OTXT)
    text4.setSize(18)
    text4.setStyle('bold')
    text4.draw(win)


# This function graphs the detail page
def graphDetails(win, index, subject, pgrade):
    win.close()
    win = GraphWin("Details", 800, 500)  # (GW)
    win.setBackground('orange')
    win.setCoords(0, 0, 80, 50)

    text = Text(Point(40, 43), "Details")  # (OTXT)
    text.setSize(36)
    text.setStyle('bold')
    text.setTextColor('red')
    text.draw(win)
    graphDiagram(win, subject, pgrade, index)

    text = Text(Point(23, 37), "Subject: " + subject)  # (OTXT)
    text.setSize(20)
    text.setStyle('bold')
    text.draw(win)

    text = Text(Point(57, 37), "Score: " + str(pgrade))  # (IEB)
    text.setSize(20)
    text.setStyle('bold')
    text.draw(win)
    username, password = functions.dataRead()  # (FNC)
    name = username[index]

    target = functions.getTarget(pgrade)  # (FNC)
    goal = functions.processScore(pgrade, target)  # (FNC)
    if goal == "False":
        comment = ", you are already at A, keep it up!"  # (OTXT)
    elif goal < 100:
        comment = ", you need to get " + str(goal) + " in next exam for next level."  # (OTXT)
    else:
        comment = ", you need a full mark in next exam for better GPA. Good luck!"  # (OTXT)

    text = Text(Point(40, 30), name + comment)  # (OTXT)
    text.setSize(20)
    text.setTextColor('red')
    text.draw(win)
    directDetails(win, index, subject)


# This function graphs the labels in the detail page
def graphDiagram(win, subject, pgrade, index):
    aline = Line(Point(10, 17), Point(70, 17))
    aline.setArrow('both')
    aline.setWidth(3)
    aline.draw(win)

    rank = functions.sortGrade(subject)  # (FNC)
    if len(rank) < 3:
        graphWarning("Data Insufficient!")  # (OTXT)
        warning = Text(Point(40, 18), "Data Insufficient!")  # (OTXT)
        warning.setStyle('bold')
        warning.setTextColor('red')
        warning.setSize(18)
        warning.draw(win)
    else:
        lowest = str(rank[-1][0])
        highest = str(rank[0][0])
        if len(rank) // 2 == 0:
            mid = (float(rank[len(rank) / 2][0]) + float(rank[len(rank) / 2 - 1][0])) / 2
        else:
            mid = (float(rank[int(len(rank) / 2)][0]))
        mid = str(mid)
        graphLabel(win, lowest, highest, mid)

        if rank[-1][1] == index:
            xcoord = 10
        elif rank[0][1] == index:
            xcoord = 70
        elif float(pgrade) == float(mid):
            xcoord = 40
        elif float(pgrade) < float(mid):
            xcoord = float(pgrade) / (float(lowest) + float(highest)) * 60 + 5
        elif float(pgrade) > float(mid):
            xcoord = float(pgrade) / (float(lowest) + float(highest)) * 60 + 10

        graphPosition(win, xcoord)


# This function graphs the position of the user in overall
def graphPosition(win, xcoord):
    position = Text(Point(xcoord, 23), "You")  # (OTXT)
    position.setTextColor('cyan')
    position.setStyle('bold')
    position.setSize(20)
    position.draw(win)
    pointer = Polygon(Point(xcoord, 18), Point(xcoord - 0.7, 21), Point(xcoord + 0.7, 21))
    pointer.setFill('cyan3')
    pointer.draw(win)


# This functions graphs the labels of the diagram
def graphLabel(win, lowest, highest, mid):
    low = Text(Point(10, 15.7), lowest)  # (OTXT)
    low.setTextColor('blue')
    low.setStyle('bold')
    low.setSize(18)
    low.draw(win)
    text = Text(Point(10, 14), "Lowest")  # (OTXT)
    text.setStyle('bold')
    text.setTextColor('blue')
    text.draw(win)

    high = Text(Point(70, 15.7), highest)  # (OTXT)
    high.setTextColor('green')
    high.setStyle('bold')
    high.setSize(18)
    high.draw(win)
    text = Text(Point(70, 14), "Highest")  # (OTXT)
    text.setStyle('bold')
    text.setTextColor('green')
    text.draw(win)

    aCircle = Circle(Point(40, 17), 0.3)
    aCircle.setFill('black')
    aCircle.draw(win)

    median = Text(Point(40, 15.7), mid)  # (OTXT)
    median.setTextColor('yellow')
    median.setStyle('bold')
    median.setSize(18)
    median.draw(win)
    text = Text(Point(40, 14), "Median")  # (OTXT)
    text.setStyle('bold')
    text.setTextColor('yellow')
    text.draw(win)


# This functions checks user's mouse click and call functions
def directDetails(win, index, subject):
    buttons = Rectangle(Point(28, 8), Point(52, 3))
    buttons.setFill('cyan3')
    buttons.draw(win)
    button = Rectangle(Point(28.5, 7.5), Point(51.5, 3.5))
    button.setFill('cyan')
    button.draw(win)
    text = Text(Point(40, 5.5), "Go to Ranking Board")  # (OTXT)
    text.setSize(19)
    text.setStyle('bold')
    text.draw(win)

    while True:
        point = win.getMouse()  # (IMS)
        if 28 <= point.getX() <= 52 and 3 <= point.getY() <= 8:
            graphRanking1(win, subject, index)
            break


# This function graphs the ranking page
def graphRanking1(win, subject, index):
    win.close()
    win = GraphWin("Ranking Board", 800, 500)  # (GW)
    win.setBackground('pink')
    win.setCoords(0, 0, 80, 50)

    text = Text(Point(40, 45), 'Ranking ' + "{" + subject + "}")  # (OTXT)
    text.setSize(36)
    text.setStyle('bold')
    text.setSize(36)
    text.setTextColor('red')
    text.draw(win)
    label = Text(Point(40, 41), "Rank" + "\t\t" + "Name" + "\t\t" + "Score")  # (OTXT)
    label.setSize(15)
    label.setTextColor('red3')
    label.draw(win)
    graphRanking2(win, index, subject)


# This function graphs the users on rank
def graphRanking2(win, index, subject):
    temp = functions.processRanking(subject)  # (FNC)
    if temp == "False":
        graphWarning("Data insufficient")  # (OTXT)
    else:
        drawRank(win, "{1ST}", temp[0][0], temp[0][1], Point(25, 37), Point(40, 37), Point(55, 37), 30, 'gold3')  # (OTXT)
        drawRank(win, "2ND", temp[1][0], temp[1][1], Point(25, 32), Point(40, 32), Point(55, 32), 30, 'silver')  # (OTXT)
        drawRank(win, "3RD", temp[2][0], temp[2][1], Point(25, 27), Point(40, 27), Point(55, 27), 30, 'orange3')  # (OTXT)
        drawRank(win, "4TH", temp[3][0], temp[3][1], Point(25, 22), Point(40, 22), Point(55, 22), 22, 'gray')  # (OTXT)
        drawRank(win, "5TH", temp[4][0], temp[4][1], Point(25, 17), Point(40, 17), Point(55, 17), 22, 'gray')  # (OTXT)
        username, password = functions.dataRead()  # (FNC)
        text = ""
        for i in range(len(temp)):
            if username[index] == temp[i][0]:
                text = "Congratulations! You are at Rank " + str(i + 1)
                break
            else:
                text = "Keep working, you shall see you name on board!"
        comment = Text(Point(40, 11), text)  # (OTXT)
        comment.setSize(18)
        comment.setStyle('bold')
        comment.setTextColor('red3')
        comment.draw(win)
    buttonRanking(win, index)


# This function graph ranks
def buttonRanking(win, index):
    # Go back to calculator
    button1s = Rectangle(Point(15, 7), Point(35, 4))
    button1s.setFill('cyan3')
    button1s.draw(win)
    button1 = Rectangle(Point(15.3, 6.7), Point(34.7, 4.3))
    button1.setFill('cyan')
    button1.draw(win)
    text1 = Text(Point(25, 5.5), "Back to Calculator")  # (OTXT)
    text1.setStyle('bold')
    text1.setSize(15)
    text1.draw(win)

    button2s = Rectangle(Point(45, 7), Point(65, 4))
    button2s.setFill('cyan3')
    button2s.draw(win)
    button2 = Rectangle(Point(45.3, 6.7), Point(64.7, 4.3))
    button2.setFill('cyan')
    button2.draw(win)
    text2 = Text(Point(55, 5.5), "Quit GPA Database")  # (OTXT)
    text2.setStyle('bold')
    text2.setSize(15)
    text2.draw(win)

    while True:
        point = win.getMouse()  # (IMS)
        if 15 <= point.getX() <= 35 and 4 <= point.getY() <= 7:
            graphCalculator(win, index)
            break
        elif 45 <= point.getX() <= 65 and 4 <= point.getY() <= 7:
            win.close()
            break


# text1, point1: ranking and position; text2, point2: name and position; text3 and point3: score and position
def drawRank(win, text1, text2, text3, point1, point2, point3, size, color):
    rank = Text(point1, text1)  # (OTXT)
    name = Text(point2, text2)  # (OTXT)
    score = Text(point3, text3)  # (OTXT)
    rank.setSize(size)
    rank.setTextColor(color)
    rank.setStyle('bold')
    name.setSize(size)
    name.setTextColor(color)
    name.setStyle('bold')
    score.setSize(size)
    score.setTextColor(color)
    score.setStyle('bold')
    rank.draw(win)
    name.draw(win)
    score.draw(win)


# This function graphs the warning page
def graphWarning(text):
    sub = GraphWin("Warning", 300, 50)  # (GW)
    sub.setCoords(0, 0, 30, 5)
    text = Text(Point(15, 2.5), text)
    text.setStyle('bold')
    text.setTextColor('red')
    text.draw(sub)
    sub.getMouse()  # (IMS)
    sub.close()
