from cgitb import text
from getquestions import Questions
import tkinter as tk
import customtkinter as ctk
from random import shuffle

class App(ctk.CTk):
    def __init__(self, qs, ans, inc_ans):
        super().__init__()
        self.qs = qs
        self.ans = ans
        self.inc_ans = inc_ans
        self.q_num = 1

        self.title("Quiz Game")
        self.geometry("800x500")

        #Set main Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        #Sizing frames
        self.question_frame = ctk.CTkFrame(master=self, height=110)
        self.question_frame.grid(row=0, column=0, sticky="we", padx=10, pady = 5)
        self.ans_frame = ctk.CTkFrame(master=self, height=400)
        self.ans_frame.grid(row=1, column=0, sticky="we", padx=10, pady = 5)
        self.score_frame = ctk.CTkFrame(master=self, height=60)
        self.score_frame.grid(row=2, column=0, sticky="we", padx=10, pady = 5)
        #Insert elements question frame
        self.question = ctk.CTkLabel(master=self.question_frame, text='',text_font=("Roboto Medium", 12))
        self.question.grid(row=0, column=0)
        #Insert elemenst ans frame
        self.ans_frame.grid_rowconfigure(4,minsize=200,weight=1)
        self.ans_frame.grid_rowconfigure(3,weight=1)
        self.ans_frame.grid_columnconfigure(0,weight=1)
        self.opt_1 = ctk.CTkCheckBox(self.ans_frame)
        self.opt_1.grid(row=0, column=0, sticky='w')
        self.opt_2 = ctk.CTkCheckBox(self.ans_frame)
        self.opt_2.grid(row=1, column=0, sticky='w')
        self.opt_3 = ctk.CTkCheckBox(self.ans_frame)
        self.opt_3.grid(row=2, column=0, sticky='w')
        self.opt_4 = ctk.CTkCheckBox(self.ans_frame)
        self.opt_4.grid(row=3, column=0, sticky='w')
        #Insert elements score frame
        self.score_frame.grid_columnconfigure(1, weight=1)
        self.score_label = ctk.CTkLabel(self.score_frame)
        self.score_label.grid(row=0, column=0, sticky='w')
        self.conf_button = ctk.CTkButton(self.score_frame, text='Confirm')
        self.conf_button.grid(row=0, column=2, sticky='e')

        #load first question
        self.load_question()
    def load_question(self):
        self.question.configure(text=self.qs[self.q_num - 1])
        ans_list = [self.ans[self.q_num - 1], self.inc_ans[self.q_num - 1][0],
                    self.inc_ans[self.q_num - 1][1],self.inc_ans[self.q_num - 1][2]]
        shuffle(ans_list)
        self.opt_1.configure(text=ans_list[0])
        self.opt_2.configure(text=ans_list[1])
        self.opt_3.configure(text=ans_list[2])
        self.opt_4.configure(text=ans_list[3])
        n = str(self.q_num)
        self.score_label.configure(text=f'{n}/10')


if __name__== '__main__':

    easy_qs = Questions('5', 'easy')
    medium_qs = Questions('3' , 'medium')
    hard_qs = Questions('2', 'hard')

    all_qs = easy_qs.get_questions()
    all_qs.extend(medium_qs.get_questions())
    all_qs.extend(hard_qs.get_questions())

    all_ans = easy_qs.get_correct_answer()
    all_ans.extend(medium_qs.get_correct_answer())
    all_ans.extend(hard_qs.get_correct_answer())

    all_inc_ans = easy_qs.get_inc_answer()
    all_inc_ans.extend(medium_qs.get_inc_answer())
    all_inc_ans.extend(hard_qs.get_inc_answer())

    
    app = App(all_qs,all_ans,all_inc_ans)
    app.mainloop()

