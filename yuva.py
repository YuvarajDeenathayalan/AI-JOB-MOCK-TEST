import tkinter as tk
from tkinter import scrolledtext
import random

class MockInterviewChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Mock Interview Chatbot")
        self.root.geometry("900x650")
        self.root.config(bg="#F0F8FF")

        
        self.categories = {
            "HR": [
                "Tell me about yourself.",
                "What are your strengths?",
                "What are your weaknesses?",
                "Why do you want to work for this company?",
                "Why should we hire you?",
                "Describe a challenging situation you faced and how you handled it.",
                "Where do you see yourself in 5 years?",
                "How do you handle stress and pressure?",
                "Describe a time when you worked in a team.",
                "Tell me about a time you failed and what you learned from it.",
                "Why did you leave your last job?",
                "How do you prioritize tasks?",
                "What motivates you?",
                "Describe your ideal work environment.",
                "How do you handle conflict at work?",
                "Tell me about a time you led a project.",
                "How do you handle criticism?",
                "Give an example of when you went above and beyond.",
                "What do you know about our company?",
                "Why are you interested in this role?",
                "Tell me about a time you disagreed with your manager.",
                "How do you handle multiple deadlines?",
                "Describe a time you solved a difficult problem.",
                "How do you stay organized?",
                "What are your salary expectations?",
                "Do you prefer working alone or in a team?",
                "Tell me about a time you missed a deadline.",
                "How do you handle ambiguity?",
                "What are your hobbies?",
                "Tell me about a time you had to adapt quickly."
            ],
            "Technical": [
                "Explain OOP concepts.",
                "What is polymorphism?",
                "Explain inheritance with an example.",
                "What is database normalization?",
                "Explain the difference between list and tuple in Python.",
                "What is recursion?",
                "Explain the difference between stack and queue.",
                "What is a binary search tree?",
                "Explain the difference between HTTP and HTTPS.",
                "What is a deadlock in operating systems?",
                "Explain the difference between process and thread.",
                "What is a REST API?",
                "Explain the difference between GET and POST requests.",
                "What is multithreading?",
                "Explain bubble sort algorithm.",
                "What is a linked list?",
                "Difference between Python 2 and 3.",
                "What is a hash table?",
                "Explain the difference between TCP and UDP.",
                "What is a memory leak?",
                "Explain MVC architecture.",
                "What is a design pattern?",
                "What is cloud computing?",
                "Explain Agile methodology.",
                "What is a virtual machine?",
                "Explain Docker containers.",
                "What is recursion depth?",
                "Explain Big O notation.",
                "What is a queue implemented with two stacks?",
                "Difference between SQL and NoSQL databases."
            ],
            "Aptitude": [
                "What is 15% of 200?",
                "If 3x + 5 = 20, what is x?",
                "A train travels 60 km in 1.5 hours. Find its speed.",
                "If a + b = 10 and a - b = 4, find a and b.",
                "A shopkeeper gives 10% discount on an item worth 500. Find the selling price.",
                "What is the simple interest on 1000 at 5% for 2 years?",
                "If a box contains 5 red and 3 blue balls, probability of picking red?",
                "The average of 5 numbers is 20. Find their sum.",
                "A car covers 120 km in 2 hours. Find its speed.",
                "If 25% of a number is 50, find the number.",
                "Find the next number: 2, 4, 8, 16, ...",
                "A bag contains 4 white, 5 black, 6 red balls. Probability of black?",
                "If 3 pens cost 45, cost of 7 pens?",
                "The ratio of boys to girls in a class is 3:2. If total 25, find boys.",
                "Find LCM of 12, 15, 20.",
                "A train of 120 m passes a pole in 9 sec. Find speed.",
                "If x/2 + y/3 = 5 and x = 6, find y.",
                "Solve: 2x^2 + 3x - 5 = 0",
                "A person earns 5000 per month. What is yearly income?",
                "A shop sells 200 items per day at 50 each. Find monthly revenue.",
                "The sum of first 10 natural numbers?",
                "If a clock shows 3:15, find angle between hands.",
                "A car travels at 60 km/h for 2 hours and 80 km/h for 3 hours. Find avg speed.",
                "Find percentage increase from 200 to 250.",
                "A bag has 10 coins, 4 are heads. Probability of tails?",
                "If 7x - 3 = 18, find x.",
                "A cube has side 4 cm. Find volume.",
                "A sum of money doubles in 5 years at simple interest. Find rate.",
                "A student scored 80, 85, 90 in 3 subjects. Find average.",
                "A train covers 150 km in 2.5 hours. Find speed."
            ]
        }

        
        self.expected_answers = {}
        for cat in self.categories:
            for q in self.categories[cat]:
                self.expected_answers[q] = "Provide a structured answer highlighting key points."

    
        self.feedback = {q: "Compare your answer with the expected answer and refine if needed."
                         for cat in self.categories.values() for q in cat}

        self.current_index = 0
        self.answers = {}
        self.random_questions = []

        self.create_category_selection()

    
    def create_category_selection(self):
        self.clear_root()
        tk.Label(self.root, text="Select Interview Category", font=("Helvetica", 24, "bold"),
                 bg="#F0F8FF", fg="#FF4500").pack(pady=40)

        frame = tk.Frame(self.root, bg="#F0F8FF")
        frame.pack(pady=20)
        for category in self.categories.keys():
            tk.Button(frame, text=category, font=("Helvetica", 16, "bold"),
                      bg="#1E90FF", fg="white", width=20, relief="raised", bd=4,
                      command=lambda c=category: self.start_interview(c)).pack(pady=10)

    def start_interview(self, category):
        self.random_questions = random.sample(self.categories[category], len(self.categories[category]))
        self.current_index = 0
        self.answers = {}
        self.create_chat_widgets()
        self.show_question()

    def create_chat_widgets(self):
        self.clear_root()
        self.chat_window = scrolledtext.ScrolledText(self.root, width=90, height=25, font=("Helvetica", 12))
        self.chat_window.pack(pady=10)
        self.chat_window.config(state=tk.DISABLED)

        self.user_input = tk.Entry(self.root, width=70, font=("Helvetica", 14))
        self.user_input.pack(side=tk.LEFT, padx=10, pady=10)
        self.user_input.bind("<Return>", lambda event: self.send_answer())

        tk.Button(self.root, text="Send", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white",
                  command=self.send_answer).pack(side=tk.LEFT, padx=5)

    
    def show_question(self):
        if self.current_index < len(self.random_questions):
            question = self.random_questions[self.current_index]
            self.insert_bot_message(f"Q{self.current_index+1}: {question}")
        else:
            self.finish_interview()

    def send_answer(self):
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        question = self.random_questions[self.current_index]
        self.answers[question] = user_text

        self.insert_user_message(user_text)
        feedback_text = self.feedback.get(question)
        expected_text = self.expected_answers.get(question)
        self.insert_bot_message(f"Feedback: {feedback_text}\nExpected Answer: {expected_text}")

        self.user_input.delete(0, tk.END)
        self.current_index += 1

        if self.current_index < len(self.random_questions):
            self.root.after(500, self.show_question)
        else:
            self.root.after(500, self.finish_interview)

    def insert_bot_message(self, message):
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, f"Bot: {message}\n\n", "bot")
        self.chat_window.tag_config("bot", foreground="#0B3D91", font=("Helvetica", 12, "bold"))
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)

    def insert_user_message(self, message):
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, f"You: {message}\n\n", "user")
        self.chat_window.tag_config("user", foreground="#228B22", font=("Helvetica", 12))
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)

    def finish_interview(self):
        self.insert_bot_message("You've completed the mock interview! Thank you for practicing!")

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MockInterviewChatbot(root)
    root.mainloop()
