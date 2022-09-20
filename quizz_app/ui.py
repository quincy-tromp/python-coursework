import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label
        self.score_lbl = tk.Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lbl.grid(column=2, row=1)
        # Canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Some question text.", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        # Buttons
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(
            image=true_img, 
            highlightthickness=0, 
            highlightbackground=THEME_COLOR,
            command=self.true_pressed
            )
        self.true_btn.grid(column=1, row=3)
        
        false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(
            image=false_img, 
            highlightthickness=0, 
            highlightbackground=THEME_COLOR,
            command=self.false_pressed
        )
        self.false_btn.grid(column=2, row=3)
        # Commands
        self.get_next_question()
        # Mainloop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
    
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
