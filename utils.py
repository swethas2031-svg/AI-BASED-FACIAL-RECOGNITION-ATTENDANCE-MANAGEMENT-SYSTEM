from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def welcome_message():
    print("AI-Based Facial Recognition Attendance Management System")
