#19. Store names of students present in class. Display:
#a.Total students b.Search a student's attendance c.Add a new student d.Remove an absent student

attendance = ["Amruta", "Sakshi", "Ragini", "Prajakta"]
print("attendance =",attendance)
print()
print("Total students:", len(attendance))

search_student = "Prajakta"
if search_student in attendance:
    print(f"{search_student} is present.")
else:
    print(f"{search_student} is absent.")
print()
attendance.append("Vaishanvi")
print("After appending:\nattendance list=", attendance)
print()

attendance.remove("Sakshi")
print("After removing:\nattendance list=", attendance)
print("Updated attendance list:", attendance)