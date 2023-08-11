from tkinter import *  
from tkinter import messagebox as mb  
import json  
guiWindow = Tk()  
guiWindow.geometry("1000x430")
guiWindow.title("Ghanashyam  - Quiz Portal")  
class myQuiz:  

    def __init__(self):       
        self.quesNumber = 0  
        self.displayTitle()  
        self.displayQuestion()  
        self.optSelected = IntVar()  
        self.options = self.radioButtons()  
        self.displayOptions()  
        self.buttons()  
        self.dataSize = len(question)
        x=  len(question)
        self.rightAnswer = 0  

    def displayResult(self):  
        wrongCount = self.dataSize - self.rightAnswer  
        rightAnswer = f"Correct: {self.rightAnswer}"  
        wrongAnswer = f"Wrong: {wrongCount}"  
        the_score = int(self.rightAnswer / self.dataSize * 100)  
        the_result = f"Score: {the_score}%"  
        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")  
    def checkAnswer(self, quesNumber):  
        if self.optSelected.get() == answer[quesNumber]:
            return True  
  
    def nextButton(self):  
        if self.checkAnswer(self.quesNumber):  
            self.rightAnswer += 1
            self.quesNumber += 1
            if self.quesNumber == self.dataSize:
                self.displayResult()
                guiWindow.destroy()
            else:
                self.displayQuestion()
                self.displayOptions()  

    def buttons(self):
        next_button = Button( guiWindow,text = "Next",command = self.nextButton,width = 10,bg = "blue",fg = "white",font = ("ariel", 16, "bold"))  
        next_button.place(x = 350, y = 380)
        quit_button = Button( guiWindow,text = "Quit",command = guiWindow.destroy,width = 10,bg = "red",fg = "white",font = ("ariel", 16, " bold"))  
        quit_button.place(x = 500, y = 380)

    def displayOptions(self):
        val = 0
        self.optSelected.set(0)  
        for opt in opts[self.quesNumber]:
            self.options[val]['text'] = opt
            val += 1  
  
    def displayQuestion(self):
        quesNumber = Label(guiWindow,text = question[self.quesNumber],width = 60,font = ('ariel', 16, 'bold'),anchor = 'w')  
        quesNumber.place(x = 70, y = 100)
    def displayTitle(self):
        myTitle = Label(guiWindow,text = "JITHON Quiz Portal",width = 50,bg = "red",fg = "white",font = ("ariel", 20, "bold"))
        myTitle.place(x = 0, y = 2)  

    def radioButtons(self):  
        qList = []  
        y_pos = 150  
        while len(qList) < 4:
            radio_button = Radiobutton(guiWindow,text = " ",variable = self.optSelected,value = len(qList) + 1,font = ("ariel", 14))  
            qList.append(radio_button)  
            radio_button.place(x = 100, y = y_pos)  
            y_pos += 40
        return qList  
with open('data.json') as json_file:  
    data = json.load(json_file)  
question = (data['ques'])  
opts = (data['choices'])  
answer = (data[ 'ans'])
quiz = myQuiz()   
guiWindow.mainloop()