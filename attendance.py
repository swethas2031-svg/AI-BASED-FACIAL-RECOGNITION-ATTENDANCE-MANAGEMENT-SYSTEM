import pandas as pd
from datetime import datetime

def mark_attendance(name):
    file_name = "attendance.csv"

    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    if not ((df["Name"] == name) & (df["Date"] == today)).any():
        new_record = {
            "Name": name,
            "Date": today,
            "Time": current_time
        }

        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        df.to_csv(file_name, index=False)
        print(f"Attendance marked for {name}")
