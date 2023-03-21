from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quiz App")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="quiz_app/images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, command=lambda: self.check_answer("True"))
        self.true.grid(column=0, row=2)

        false_image = PhotoImage(file="quiz_app/images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, command=lambda: self.check_answer("False"))
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.root.mainloop()
    

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_answer(self, answer):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
        