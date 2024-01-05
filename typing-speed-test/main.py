from words import words
import random 
import tkinter as tk
import threading
import time


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.words = words
        self.current_word_index = random.randint(0, len(self.words))
        self.correct_words = 0
        self.words_typed = 0
        
        self.timer_running = False
        self.start_time = None
        self.remaining_time = 60
        
        self.create_ui()
        
        
    def create_ui(self):
        self.word_label = tk.Label(self.root, text=self.words[self.current_word_index], font=("Arial", 18))
        self.word_label.pack(pady=20)
        
        self.entry = tk.Entry(self.root, width=30, font=('Arial', 14))
        self.entry.pack()
        
        self.entry.bind('<Return>', self.check_input)
        self.entry.bind('<space>', self.check_input)
        
        self.entry.bind('<Key>', self.start_timer)
        
        
    def check_input(self, event):        
        user_input = self.entry.get().strip().lower()
        current_word = self.words[self.current_word_index].lower()
        
        if user_input == current_word:
            self.correct_words += 1    
        
        self.words_typed += 1
        self.current_word_index = random.randint(0, len(self.words))
        self.update_word()
        
        self.entry.delete(0, tk.END)
        
        
    def start_timer(self, event):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            threading.Thread(target=self.timer).start()
    
    
    def timer(self):
        while self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer_label)
            time.sleep(1) 
        
        self.root.after(0, self.show_score)
        
            
    def update_timer_label(self):
        if self.remaining_time >= 0:
            timer_label.config(text=f'Time: {self.remaining_time} s')
        
        
    def update_word(self):
        if self.current_word_index >= len(self.words):
            self.word_label.config(text='End Game!')
        else:
            self.word_label.config(text=self.words[self.current_word_index])
            
        
    def show_score(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        self.wpm = (self.correct_words / elapsed_time) * 60
        self.accuracy = (self.correct_words / self.words_typed) * 100
        
        self.word_label.config(text=f"WPM: {round(self.wpm, 0)}, Accuracy: {round(self.accuracy, 0)}%")
        self.entry.pack_forget()
        timer_label.pack_forget()
        
        
if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    timer_label = tk.Label(root, text='Time: 60 s', font=('Arial', 12))
    timer_label.pack()
    root.mainloop()
