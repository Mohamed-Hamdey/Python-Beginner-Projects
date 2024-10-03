from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=320, height=600)

        self.score_label = Label(text=f"Score: {self.score}", height=3, width=7, bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_clicked)
        self.true_button.grid(row=3, column=0, padx=10, pady=30)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_clicked)
        self.false_button.grid(row=3, column=1, padx=10, pady=30)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
         q_text = self.quiz.next_question()
         self.canvas.itemconfig(self.question_text, text=q_text)
        else:
           self.canvas.itemconfig(self.question_text,text = f"You have reached the end of the quiz and you got {self.score}/10")
           self.true_button.config(state="disabled")
           self.false_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(1000, self.reset_feedback)

    def reset_feedback(self):
        self.canvas.config(bg="white")
        self.get_next_question()

