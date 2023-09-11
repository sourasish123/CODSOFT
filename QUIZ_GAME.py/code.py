import tkinter as tk
from tkinter import messagebox
from random import shuffle
class QuizGame:
    def __init__(self,root):
        self.root=root
        self.root.title("QUIZ  GAME")
        
        self.question=[
            {
                "question":"Which is the largest planet in our solar system ?",
                "options":["jupiter","saturn","neptune","mars"],
                "answer":"jupiter"
            },
            {
                "question":"Which planet is known as red planet ?",
                "options":["jupiter","saturn","neptune","mars"],
                "answer":"mars"                
            },
            {
                "question":"Which is the largest continent in the world ?",
                "options":["asia","Africa","North America","Europe"],
                "answer":"asia"                
            },
            {
                "question":"Which is the capital city of tamil nadu ?",
                "options":["chenai","madurai","kolkata","mijoram"],
                "answer":"chenai"                
            },
            {
                "question":"Which festival is widely celebrate in west bengal ?",
                "options":["durga puja","janmastami","deepavali","pongal"],
                "answer":"durga puja"                
            },
            {
                "question":"What is the capital of India ?",
                "options":["kolkata","Delhi","mumbai","Rachi"],
                "answer":"Delhi"                 
            },
            
        ]
        self.score=0
        self.current_question=0
        
        self.question_label=tk.Label(self.root,text="",font=("Arial",14),wraplength=400)
        self.question_label.pack(pady=20)
        
        self.option_button=[]
        for i in range(4):
            button=tk.Button(self.root,text="",font=("Arial",14),width=30,command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_button.append(button)
            
        self.score_label=tk.Label(self.root,text="Score: 0",font=("Arial",12))
        self.score_label.pack(pady=20)            
        
        self.next_question()
        
    def next_question(self):
        if self.current_question < len(self.question):
            question=self.question[self.current_question]
            self.question_label.config(text=question["question"])
            option=question["options"]
            shuffle(option)
            for i in range(4):
                self.option_button[i].config(text=option[i])
            self.score_label.config(text="score: {}".format(self.score))
        else:
            self.end_game()
            
    def check_answer(self,selected_option):
        question=self.question[self.current_question]
        selected_answer=question["options"][selected_option]
        correct_answer=question["answer"]
        if selected_answer==correct_answer:
            self.score+=1
        self.current_question += 1
        self.next_question()
        
    def end_game(self):
        messagebox.showinfo("Game over","Quiz has ended!\n Your Score: {}".format(self.score))
        self.root.destroy()
root=tk.Tk()
    
quiz_game=QuizGame(root)
root.mainloop()                               