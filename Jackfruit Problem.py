import tkinter as tk
from tkinter import messagebox

print('''Welcome to your Career Test!
Learn more about yourself and find your areas of interest to find the perfect path for you!

Instructions:
You will be given 6 questions. Choose one option for each.''')

questions = [
    "Q1. What has been your favourite subject at school?",
    "Q2. Which of the following would you rather do?",
    "Q3. Which word describes you best?",
    "Q4. Which of the following attributes should your job have?",
    "Q5. What kind of environment would you like to work in?",
    "Q6. Where would you rather work?"
]

choices = [
    ["Math", "Science", "Art", "Social Sciences", "English"],
    ["Build Structures/Buildings", "Research about life and nature",
     "Design Spaces/Graphics", "Help people in need", "Organise Events/Data"],
    ["Handy", "Intelligent", "Creative", "Compassionate", "Organised"],
    ["Mechanical", "Scientific", "Artistic", "Humanitarian", "Systematic"],
    ["Constructive", "Intellectual", "Unstructured", "Cooperative", "Structured"],
    ["In the Outdoors", "In a Lab", "At a Studio", "At a facility for people", "At an Office"]
]
user_responses = []
current_question = 0

# Stores buttons so we can change colors
#option_buttons = []

# To track selected button per question
#selected_button = None  


def display_question():
    global option_buttons, selected_button
    option_buttons = []
    selected_button = None

    for widget in window.winfo_children():
        widget.destroy()

    question_label = tk.Label(window, text=questions[current_question])
    question_label.pack(pady=10)

    for choice in choices[current_question]:
        button = tk.Button(
            window,
            text=choice,
            activebackground="grey",
            command=lambda c=choice, b=None: record_selection(c, b)
        )
        option_buttons.append(button)
        button.pack(pady=5)
        
# Fix lambda reference issue (attach button explicitly)
    for btn in option_buttons:
        btn.config(command=lambda b=btn, c=btn["text"]: record_selection(c, b))

    next_button = tk.Button(window, text="Next", command=next_question)
    next_button.pack(pady=5)


def record_selection(choice, button):
    global selected_button

    # Reset all buttons to default style
    for btn in option_buttons:
        btn.config(bg="SystemButtonFace")

    # Highlight selected button
    button.config(bg="lightgreen")

    selected_button = button
    record_response(choice)


def record_response(choice):
    # Replace last if user re-selects in same question
    if len(user_responses) > current_question:
        user_responses[current_question] = choice
    else:
        user_responses.append(choice)
def next_question():
    global current_question
    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_results()
        
def show_results():
    if len(user_responses) != len(questions):
        messagebox.showerror(
            "Incomplete Test",
            "Incorrect number of responses.\nPlease answer all questions."
    )
        return
    result_message = (
        f"Your recommended career based on your answers: {get_recommendation()}"
    )
    messagebox.showinfo("Career Test Result", result_message)
    window.destroy()

def get_recommendation():
    score1 = score2 = score3 = score4 = score5 = 0
    for i in user_responses:
        if i == "Math" or i == "Build Structures/Buildings" or i == "Handy" or \
           i == "Mechanical" or i == "Constructive" or i == "In the Outdoors":
            score1 += 1
        elif i == "Science" or i == "Research about life and nature" or \
             i == "Intelligent" or i == "Scientific" or i == "Intellectual" or i == "In a Lab":
            score2 += 1
        elif i == "Art" or i == "Design Spaces/Graphics" or i == "Creative" or \
             i == "Artistic" or i == "Unstructured" or i == "At a Studio":
            score3 += 1
        elif i == "Social Sciences" or i == "Help people in need" or \
             i == "Compassionate" or i == "Humanitarian" or i == "Cooperative" or \
             i == "At a facility for people":
            score4 += 1
        elif i == "English" or i == "Organise Events/Data" or i == "Organised" or \
             i == "Systematic" or i == "Structured" or i == "At an Office":
            score5 += 1

    list_of_scores = [score1, score2, score3, score4, score5]
    listed_it = sorted(list_of_scores)

    if score1 == listed_it[4]:
        return '''Your main area of interest is: BUILDING
Building jobs involve the use of tools, machines, or physical skill.
Recommended Professions: Engineer, Architect, Industrialist'''
    elif score2 == listed_it[4]:
        return '''Your main area of interest is: THINKING
Thinking jobs involve theory, research, and intellectual inquiry.
Recommended Professions: Scientist, Professor, Astronomer'''
    elif score3 == listed_it[4]:
        return '''Your main area of interest is: CREATING
Creating jobs involve art, design, language, and self-expression.
Recommended Professions: Interior Designer, Graphic Designer, Editor, Art Historian'''
    elif score4 == listed_it[4]:
        return '''Your main area of interest is: HELPING
Helping jobs involve serving, assisting, teaching, or coaching.
Recommended Professions: Doctor, Teacher, Public Service'''
    elif score5 == listed_it[4]:
        return '''Your main area of interest is: ORGANISING
Organising jobs involve data, processes, management, and structure.
Recommended Professions: Data Scientist, Event Organizer, Administration jobs'''


window = tk.Tk()
window.title("Career Test")
window.configure(bg="white")

display_question()
window.mainloop()
