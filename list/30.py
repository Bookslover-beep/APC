#30.Store patient names and ages using lists.Perform:
#a.Add a patient b.Delete a patient c.Search a patient d.Display all patients e.Count total patients
patient_names = ["John", "Mary", "David"]
patient_ages = [45, 30, 60]
print("patient_names =",patient_names)
print("patient_ages =",patient_ages)
print()

patient_names.append("Sarah")
print("After append name:\npatient_names =",patient_names)

patient_ages.append(25)
print("After append age:\npatient_ages =",patient_ages)
print()

remove_name = "Mary"
if remove_name in patient_names:
    index = patient_names.index(remove_name)
    patient_names.pop(index)
    patient_ages.pop(index)
print("After remove name:\npatient_names =",patient_names)
print("After remove age:\npatient_ages =",patient_ages)
print()

search_name = "David"
if search_name in patient_names:
    idx = patient_names.index(search_name)
    print(f"Found {search_name}, Age: {patient_ages[idx]}")
else:
    print(f"{search_name} not found.")

for name, age in zip(patient_names, patient_ages):
    print(f"Patient: {name}, Age: {age}")
print()

print("Total patients:", len(patient_names))