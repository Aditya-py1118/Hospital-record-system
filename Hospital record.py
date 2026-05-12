patients=[]
while True:
    print("Enter your choice below.")
    print("1. Add a patient's record")
    print("2. Search for a patient's record")
    print("3. Display all patient's records")
    print("4. Edit a record")
    print("5. Delete a patient's record")
    print("6. Pay fees")
    print("7. Exit")
    
    c=int(input("Enter your choice here:"))
    if c==1:
        name=input("Enter the name of the patient:")   #0(name)
        age=int(input("Enter the age of the patient:"))   #1(age)
        patient_no=int(input("Enter the patient's number:"))   #2(number)
        fees_to_be_paid=int(input("Enter the fees due:"))  #3(due)
        fees_paid=int(input("Enter the fees paid by the patient:"))  #4(paid)
        disease=input("Enter the patient's disease:")   #5(disease)
        doc_assigned=input("Enter the doctor's name, assigned to the patient:")  #6(doctor)
        record=[name,age,patient_no,fees_to_be_paid,fees_paid,disease,doc_assigned]
        patients.append(record) 
        print("Record added successfully")
    elif c==2:
        patient_no=int(input("Enter the patient number to search in the record:"))
        found=False
        for i in range(len(patients)):
            if patients[i][2]==patient_no:
                print("Record Found\n")
                print("Patient Name:",patients[i][0])
                print("Age:",patients[i][1])
                print("Patient number:",patients[i][2])
                print("Fees Due:",patients[i][3])
                print("Fees Paid:",patients[i][4])
                print("Disease:",patients[i][5])
                print("Doctor Assigned:",patients[i][6])
                found=True
                break
        if found==False:
                print("No record was found.\nTry a different patient number.")
    elif c==3:
        if len(patients)==0:
            print("The record is empty.")
        else:
            for i in range(len(patients)):
                print(f"{i+1}.Patient's Name:{patients[i][0]},Patient's Age:{patients[i][1]},Patient Number:{patients[i][2]},Fees Due:{patients[i][3]},Fees Paid:{patients[i][4]},Disease:{patients[i][5]},Doctor assigned:{patients[i][6]}")
    elif c==4:
        num=int(input("Enter the patient number to edit their record:"))
        found=False
        for i in range(len(patients)):
            if num==patients[i][2]:
                print("Enter the same values as before if you don't want to change certain information.")
                new_name=input("Edit the name of the patient:")#0
                new_age=int(input("Edit the patient's age:"))#1
                new_patient_number=int(input("Edit the patient number:"))#2
                new_fees_due=int(input("Enter the due fees:"))#3
                new_fees_paid=int(input("Enter the fees paid:"))#4
                new_disease=input("Edit patient's disease:")#5
                new_doctor=input("Change the assigned doctor to the patient:")#6
                
                patients[i][0]=new_name
                patients[i][1]=new_age
                patients[i][2]=new_patient_number
                patients[i][3]=new_fees_due
                patients[i][4]=new_fees_paid
                patients[i][5]=new_disease
                patients[i][6]=new_doctor
                print("The record has been edited successfully.")
                found=True
                break
        if found==False:
                print("The patient number is wrong.\nTry a different patient number.")
    elif c==5:
        num=int(input("Enter the patient number to delete their record:"))
        found=False
        for i in range(len(patients)):
            if num==patients[i][2]:
                patients.pop(i)
                print("Record deleted successfully.")
                found=True
                break
        if found==False:
            print("No record was found.\nPlease check the patient number again.")
    elif c==6:
        num=int(input("Enter patient number to pay the fees:"))
        found=False
        for i in range(len(patients)):
            if num==patients[i][2]:
                new_fees=int(input("Enter the fees paid:"))
                new_fees_due=int(input("Enter the fees due:"))
                patients[i][3]=new_fees_due
                patients[i][4]=new_fees
                print("Fee paid successfully.")
                found=True
                break
                
        if found==False:
            print("No record was found.\n Kindly check the patient number again.")
    elif c==7:
        print("Program exited successfully.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
        