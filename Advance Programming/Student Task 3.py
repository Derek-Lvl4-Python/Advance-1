import os
import tkinter as tk
from tkinter import messagebox, ttk

class Student:
    def __init__(self, student_id, name, marks, exam_mark):
        self.student_id = student_id
        self.name = name
        self.coursework_marks = marks
        self.exam_mark = exam_mark
        self.total_coursework = sum(marks)
        self.total_score = self.total_coursework + self.exam_mark
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()

    def calculate_percentage(self):
        return (self.total_score / 160) * 100

    def calculate_grade(self):
        if self.percentage >= 70:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

    def display_record(self):
        return f"Name: {self.name}\nStudent ID: {self.student_id}\nTotal Coursework Marks: {self.total_coursework}\nExam Marks: {self.exam_mark}\nOverall Percentage: {self.percentage:.2f}%\nGrade: {self.grade}"

def load_students(filename):
    students = []
    current_directory = os.getcwd()  
    print(f"Current working directory: {current_directory}") 

    if os.path.exists(filename):  
        try:
            with open(filename, 'r') as file: 
                number_of_students = int(file.readline().strip())  
                for line in file:
                    parts = line.strip().split(',')  
                    student_id = int(parts[0].strip())  
                    name = parts[1].strip()  
                    coursework_marks = list(map(int, parts[2:5]))  
                    exam_mark = int(parts[5].strip())  
                    students.append(Student(student_id, name, coursework_marks, exam_mark))
        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print(f"Error: File '{filename}' not found.") 
    return students

def view_all_students(students, text_widget):
    if not students:
        messagebox.showinfo("No Data", "No student data available.")
        return
    display_text = ""
    for student in students:
        display_text += student.display_record() + "\n" + "-" * 40 + "\n"
  
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, display_text)

def view_individual_student(students, student_id, text_widget):
    student_id = student_id.strip().lower()  

    for student in students:
        if str(student.student_id).strip() == student_id or student.name.strip().lower() == student_id:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, student.display_record())
            return

    messagebox.showerror("Student Not Found", "Student not found.")

def show_highest_score(students, text_widget):
    if not students:
        messagebox.showinfo("No Data", "No student data available.")
        return
    highest_score_student = max(students, key=lambda s: s.total_score)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, "Student with the highest total score:\n")
    text_widget.insert(tk.END, highest_score_student.display_record())

def show_lowest_score(students, text_widget):
    if not students:
        messagebox.showinfo("No Data", "No student data available.")
        return
    lowest_score_student = min(students, key=lambda s: s.total_score)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, "Student with the lowest total score:\n")
    text_widget.insert(tk.END, lowest_score_student.display_record())

class StudentManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")

        self.filename = 'studentmarks.txt' 
        self.students = load_students(self.filename)

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Student Manager", font=("Arial", 18))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.view_all_btn = tk.Button(self.root, text="View All Students", command=self.view_all_students)
        self.view_all_btn.grid(row=1, column=0, pady=5)

        self.view_individual_btn = tk.Button(self.root, text="View Individual Student", command=self.view_individual_student)
        self.view_individual_btn.grid(row=1, column=1, pady=5)

        self.highest_score_btn = tk.Button(self.root, text="Highest Total Score", command=self.show_highest_score)
        self.highest_score_btn.grid(row=2, column=0, pady=5)

        self.lowest_score_btn = tk.Button(self.root, text="Lowest Total Score", command=self.show_lowest_score)
        self.lowest_score_btn.grid(row=2, column=1, pady=5)

        self.text_display = tk.Text(self.root, width=80, height=20)
        self.text_display.grid(row=3, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(self.root, text="Enter Student ID or Name:")
        self.search_label.grid(row=4, column=0, pady=5)

        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.grid(row=4, column=1, pady=5)

    def view_all_students(self):
        view_all_students(self.students, self.text_display)

    def view_individual_student(self):
        student_id = self.search_entry.get()
        view_individual_student(self.students, student_id, self.text_display)

    def show_highest_score(self):
        show_highest_score(self.students, self.text_display)

    def show_lowest_score(self):
        show_lowest_score(self.students, self.text_display)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()
