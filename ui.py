from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, q_in:QuizBrain):
        self.quiz = q_in
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=("Arial", 10, "normal"), fg="white", justify="center")
        self.score.grid(row=0, column=1, columnspan=1, pady = 10)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 30)
        self.current_question = self.canvas.create_text(150, 125, text="", font=("Ariel", 12,"italic"), width=280,
                                                        fill=THEME_COLOR, justify="center")
        self.next_q()
        tru = PhotoImage(file="./images/true.png")
        self.true_button = Button(image = tru, highlightthickness=0, command=self.true_click)
        self.true_button.grid(row=2, column=0, columnspan=1, pady = 10)
        fls = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=fls, highlightthickness=0, command=self.false_click)
        self.false_button.grid(row=2, column=1, columnspan=1, pady = 10)
        self.window.mainloop()

    def next_q(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.current_question, text = self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.current_question, text="End of quiz", font=("Ariel", 20,"italic"))
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.gib_feedbk(self.quiz.check_answer("True"))

    def false_click(self):
        self.gib_feedbk(self.quiz.check_answer("False"))

    def gib_feedbk(self, is_correct):
        if is_correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.next_q)
