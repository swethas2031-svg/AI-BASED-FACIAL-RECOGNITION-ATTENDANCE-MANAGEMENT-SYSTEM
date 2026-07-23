import csv
import os

FILE_NAME = "attendance.csv"

def create_database():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Time"])

def save_attendance(name, date, time):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, time])

if __name__ == "__main__":
    create_database()
    print("Attendance database created.")
