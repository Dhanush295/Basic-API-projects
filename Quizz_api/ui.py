THEME_COLOR = "#375362"

from tkinter import *

class Design:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questions appear here!", fill=THEME_COLOR, font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.W_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.W_img, highlightthickness=0, command=self.wrong_ans)
        self.wrong_button.grid(column=0, row=2)

        self.R_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.R_img, highlightthickness=0, command=self.correct_ans)
        self.right_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def wrong_ans(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def correct_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


