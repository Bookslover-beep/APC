#14.Create a project directory containing packages for: 
#a)Patient management  
#b)Doctor management  
#c)Billing  
#d)Medical records  
#Implement simple functions in each module and access them from main.py. 

from patients import info
from doctors import schedule
from billing import invoice
from medical_records import history

print(info.register_patient())
print(schedule.get_doctor_schedule())
print(invoice.generate_bill())
print(history.get_history())