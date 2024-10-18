---
tags:
  - tafe
  - assessment
---
I would like you to create a program called "Work From Home Tracker" that does the following:

1. Presents a menu interface with options to *enter* **daily hours** worked, *produce* *hours worked report*, and quit the program.
2. Allows *input* of **daily hours** worked for seven employees, including **week number**, **employee ID**, **name**, and **hours worked for each day** (Monday to Friday).
3. Processes the daily hours worked, *displaying* appropriate messages for **insufficient or excessive hours.**
4. *Writes* employee records to a file.
5. Calculates and stores total weekly hours for each employee.
6. *Produces* a weekly **employee report** showing the number of employees in different hour ranges.
7. Reads and displays employee records from the file, sorted by most recent entries.
8. Uses two data structures: one for storing daily hours (e.g., an array) and another for storing weekly totals (e.g., a list).
9. Implements input validation and error handling.
10. Utilizes sequence, selection, and iteration constructs.
11. Makes use of at least two library functions.
12. Employs at least two types of commenting techniques.
13. Performs string manipulation.
14. Reads from and writes to a text file.

The program should follow basic language syntax rules, adhere to relevant programming standards, and meet the client requirements checklist provided in the task sheet.



```python
daily_hours = []

func enter_daily_hours(
   week_num,
   employee_ID,
   name, 
   hours # list of length 5, containing the hours worked for each day
	):
	daily_hours.append({
		"WeekNumber": week_num,
		"EmployeeID": employee_ID,
		"Name": name,
		"hours": hours,
	});
	update_file(daily_hours)

enter_daily_hours(1, 0, "Cooper", [
   8, 8, 8, 8, 8
])

```


![[Pasted image 20240830161451.png]]

Make a class named `Employee`, and have the attributes, hours, which will be of type: `(int: list)[]`


```python
class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.weekly_hours = []

	def add_week(self, hours: l):
		self.weekly_hours.append(hours)

```
