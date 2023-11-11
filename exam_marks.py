# Function to get input marks for a subject with error handling
def get_subject_marks(subject_name):
    while True:
        try:
            mark = float(input(f"Enter marks of {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to check if a subject mark is a distinction (D)
def is_distinction(mark):
    return mark >= 80

# Function to check if a student passed or failed
def is_pass(subject_marks):
    return all(mark >= 40 for mark in subject_marks)

# Function to determine the number of distinctions
def count_distinctions(subject_marks):
    return sum(is_distinction(mark) for mark in subject_marks)

# Function to calculate and print the result
def calculate_result(subject_marks):
    total = sum(subject_marks)
    subject_names = ["Myanmar", "English", "Mathematics", "Chemistry", "Physics", "Biology"]

    print("\nSubject-wise Marks:")
    for i, mark in enumerate(subject_marks):
        print(f"{subject_names[i]:<12}: {mark}{' *' if is_distinction(mark) else ''}")

    print("Total Marks:", total)

    if is_pass(subject_marks):
        num_distinctions = count_distinctions(subject_marks)
        if num_distinctions == 6:
            print("Pass with 6 D -", ', '.join(subject_names[i] for i in range(len(subject_marks)) if is_distinction(subject_marks[i])))
        elif num_distinctions == 5:
            print("Pass with 5 D -", ', '.join(subject_names[i] for i in range(len(subject_marks)) if is_distinction(subject_marks[i])))
        elif num_distinctions == 4:
            print("Pass with 4 D -", ', '.join(subject_names[i] for i in range(len(subject_marks)) if is_distinction(subject_marks[i])))
        elif num_distinctions == 3:
            print("Pass with 3 D -", ', '.join(subject_names[i] for i in range(len(subject_marks)) if is_distinction(subject_marks[i])))
        elif num_distinctions == 2:
            print("Pass with 2 D -", ', '.join(subject_names[i] for i in range(len(subject_marks)) if is_distinction(subject_marks[i])))
        elif num_distinctions == 1:
            print("Pass with 1 D -", ', '.join(subject_names[i] for i in range(len(subject_marks)) if is_distinction(subject_marks[i])))
    else:
        print("Failed")

# Main program
subject_marks = [get_subject_marks("Myanmar"), get_subject_marks("English"), get_subject_marks("Mathematics"),
                get_subject_marks("Chemistry"), get_subject_marks("Physics"), get_subject_marks("Biology")]

calculate_result(subject_marks)
