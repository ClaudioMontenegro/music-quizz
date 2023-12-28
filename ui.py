from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,  bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.maintext = self.canvas.create_text(150, 125,
                                                width=280,
                                                text="this is the text",
                                                font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR)
        self.score = Label(text=f"Score: 0",
                           bg=THEME_COLOR,
                           fg="white")
        self.score.grid(row=0, column=1)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.false_bt = Button(image=false_img,
                               bg=THEME_COLOR,
                               borderwidth=0,
                               border=0,
                               command=self.check_answer_false)
        self.false_bt.grid(row=2, column=1)
        self.false_bt.config(activebackground=THEME_COLOR)
        self.true_bt = Button(image=true_img,
                              bg=THEME_COLOR,
                              borderwidth=0,
                              border=0,
                              command=self.check_answer_true)
        self.true_bt.grid(row=2, column=0)
        self.true_bt.config(activebackground=THEME_COLOR)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.maintext, text=q_text)
        else:
            self.canvas.itemconfig(self.maintext, text=f"Your final score is: {self.quiz.score}/10")
            self.true_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def check_answer_false(self):
        is_correct = self.quiz.check_answer(False)
        self.score.config(text=f"Score: {self.quiz.score}")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def check_answer_true(self):
        is_correct = self.quiz.check_answer(True)
        self.score.config(text=f"Score: {self.quiz.score}")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


