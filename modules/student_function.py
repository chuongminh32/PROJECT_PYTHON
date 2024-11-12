import csv
import tkinter as tk
from tkinter import ttk

class Student:
    def __init__(self, student_id, name, country, total_score):
        self.student_id = student_id
        self.name = name
        self.country = country
        self.total_score = total_score

def stu_filter(students, country):
    return [student for student in students if student.country.lower() == country.lower()]
    def display_students_in_frame(students, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        columns = ('ID', 'Name', 'Country', 'Total Score')
        tree = ttk.Treeview(frame, columns=columns, show='headings')
        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Country', text='Country')
        tree.heading('Total Score', text='Total Score')

        for student in students:
            tree.insert('', tk.END, values=(student.student_id, student.name, student.country, student.total_score))

        tree.pack(fill=tk.BOTH, expand=True)

def stu_top(students):
    return sorted(students, key=lambda student: student.total_score, reverse=True)[:10]

def stu_find(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def read_students_from_csv(file_path):
    students = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_id = int(row['id'])
            name = row['name']
            country = row['nationality']
            total_score = sum(float(row[subject]) for subject in ['english.grade', 'math.grade', 'sciences.grade', 'language.grade'])
            students.append(Student(student_id, name, country, total_score))
    return students
def main():
    file_path = 'data/data_clean.csv'
    students = read_students_from_csv(file_path)

    root = tk.Tk()
    root.title("Student Comparison")

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    # display_students_in_frame(students, frame)

    root.mainloop()

if __name__ == "__main__":
    main()
    # Create an entry widget for country filter
    country_label = ttk.Label(root, text="Country:")
    country_label.pack(side=tk.LEFT, padx=(10, 5))
    
    country_entry = ttk.Entry(root)
    country_entry.pack(side=tk.LEFT, padx=(0, 10))

    def filter_students():
        country = country_entry.get()
        filtered_students = stu_filter(students, country)
        display_students_in_frame(filtered_students, frame)

    filter_button = ttk.Button(root, text="Filter", command=filter_students)
    filter_button.pack(side=tk.LEFT)

    # Create an entry widget for student ID search
    id_label = ttk.Label(root, text="Student ID:")
    id_label.pack(side=tk.LEFT, padx=(10, 5))
    
    id_entry = ttk.Entry(root)
    id_entry.pack(side=tk.LEFT, padx=(0, 10))

    def find_student():
        student_id = int(id_entry.get())
        student = stu_find(students, student_id)
        if student:
            display_students_in_frame([student], frame)
        else:
            display_students_in_frame([], frame)

    find_button = ttk.Button(root, text="Find", command=find_student)
    find_button.pack(side=tk.LEFT)