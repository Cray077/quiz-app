from tkinter import *

root = Tk()

root.title = "Quiz App"
root.geometry = "800x600"
root.resizable = False

questionNumberFrame = Frame(root, width=50, height=400)
questionNumberFrame.grid(row=0, column=0, sticky="w", rowspan=2)

questionFrame = Frame(root, pady=20)
questionFrame.grid(row=0, column=1, sticky="n")

answerFrame = Frame(root)
answerFrame.grid(row=1, column=1)


def display_quiz(question, answer):
    # display the question
    questionLabel = Label(questionFrame, text=question)
    questionLabel.grid(row=0, column=0)
    # display the answer
    for (text, answer) in answer.items():
        radioButton = Radiobutton(answerFrame, text=text, value=answer, width=40, indicatoron=0, padx=10)
        radioButton.pack()


question = "Berapakah angka tertinggi dalam 8 bit ?"
answer = {
    "255" : "255",
    "256" : "256",
    "257" : "257",
    "258" : "258",
    "259" : "259"
}

display_quiz(question, answer)

root.mainloop()