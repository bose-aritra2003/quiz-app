from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)
        self.score = Label(text=f"Score: {self.quiz.score}", font=FONT, bg=THEME_COLOR)
        self.my_canvas = Canvas(width=300, height=250, bg="white", highlightbackground="yellow")
        self.question_text = self.my_canvas.create_text(150, 125, width=280,  fill=THEME_COLOR, font=FONT)
        my_cross_img = PhotoImage(file="images/false.png")
        my_check_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=my_cross_img, highlightbackground="yellow", command=self.falsePressed)
        self.true_button = Button(image=my_check_img, highlightbackground="yellow", command=self.truePressed)

        self.my_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.score.grid(row=0, column=1, padx=20, pady=20)
        self.getNextQuestion()
        self.window.mainloop()

    def getNextQuestion(self):
        self.my_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.my_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.my_canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz !")
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)

    def truePressed(self):
        is_right = self.quiz.check_answer("True")
        self.giveFeedback(is_right)

    def falsePressed(self):
        is_right = self.quiz.check_answer("False")
        self.giveFeedback(is_right)

    def giveFeedback(self, is_right: bool):
        if is_right:
            self.quiz.score += 1
            self.score.config(text=f"Score: {self.quiz.score}")
            self.my_canvas.config(bg="green")
        else:
            self.my_canvas.config(bg="red")
        self.window.after(1000, func=self.getNextQuestion)
