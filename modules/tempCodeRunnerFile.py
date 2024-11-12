
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