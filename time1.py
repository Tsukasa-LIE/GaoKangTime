import datetime

exam_date = datetime.date(2025,6,7)
today = datetime.date.today()
days_left = (exam_date - today).days
print(days_left)