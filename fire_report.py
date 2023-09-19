#Fire extinguisher report 
#create the file name and use file.write to write that data over to the text file

with open("inspection_checklist.txt", "w") as file:
    name = str(input("Inspector name: "))
    file.write(f"Inspector name: {name}\n")
    print("Mechanic Workshop checklist")

#each ticket number will have it's own variable as well as the two questions needed for this report
#the ticket numbers are all inputs set to catch numbers only
#the questions are set as strings designed for yes or no answers 
    ticket_number1 = int(input("Fire suppression ticket number:"   )) 
    q1 = str(input("Is the dial within the green?: "))
    q2 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Fire suppression ticket number: {ticket_number1}\n")
    file.write(f"Is the dial within the green?: {q1}\n")
    file.write(f"Is the extinguisher clear of debris?: {q2}\n")

    ticket_number2 = int(input("Garage bay 1 ticket number:"  ))
    q3 = str(input("Is the dial within the green?: "))
    q4 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 1 ticket number: {ticket_number2}\n")
    file.write(f"Is the dial within the green?: {q3}\n")
    file.write(f"Is the extinguisher clear of debris?: {q4}\n")

    ticket_number3 = int(input("Welding bench ticket number:"  ))
    q5 = str(input("Is the dial within the green?: "))
    q6 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Welding bench ticket number: {ticket_number3}\n")
    file.write(f"Is the dial within the green?: {q5}\n")
    file.write(f"Is the extinguisher clear of debris?: {q6}\n")

    
    ticket_number4 = int(input("Vehicle lift post 2 ticket number:"  ))
    q7 = str(input("Is the dial within the green?: "))
    q8 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Welding bench ticket number: {ticket_number4}\n")
    file.write(f"Is the dial within the green?: {q7}\n")
    file.write(f"Is the extinguisher clear of debris?: {q8}\n")

    ticket_number5 = int(input("Vehicle lift post 1 ticket number:"  ))
    q9 = str(input("Is the dial within the green?: "))
    q10 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Vehicle lift post 1 ticket number: {ticket_number5}\n")
    file.write(f"Is the dial within the green?: {q9}\n")
    file.write(f"Is the extinguisher clear of debris?: {q10}\n")

    ticket_number6 = int(input("Parts room ticket number:"  ))
    q11 = str(input("Is the dial within the green?: "))
    q12 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Parts room ticket number: {ticket_number6}\n")
    file.write(f"Is the dial within the green?: {q11}\n")
    file.write(f"Is the extinguisher clear of debris?: {q12}\n")

    ticket_number7 = int(input("Fluid room ticket number:"  ))
    q13 = str(input("Is the dial within the green?: "))
    q14 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Fluid room ticket number: {ticket_number7}\n")
    file.write(f"Is the dial within the green?: {q13}\n")
    file.write(f"Is the extinguisher clear of debris?: {q14}\n")

    ticket_number8 = int(input("Staircase ticket number:"  ))
    q15 = str(input("Is the dial within the green?: "))
    q16 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 12 ticket number: {ticket_number8}\n")
    file.write(f"Is the dial within the green?: {q15}\n")
    file.write(f"Is the extinguisher clear of debris?: {q16}\n")


    ticket_number9 = int(input("Second floor ticket number:"  ))
    q17 = str(input("Is the dial within the green?: "))
    q18 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Second floor ticket number: {ticket_number9}\n")
    file.write(f"Is the dial within the green?: {q17}\n")
    file.write(f"Is the extinguisher clear of debris?: {q18}\n")


    print("Shared shop/Parks room checklist")

    ticket_number10 = int(input("Garage bay 12 ticket number:"  ))
    q19 = str(input("Is the dial within the green?: "))
    q20 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 12 ticket number: {ticket_number10}\n")
    file.write(f"Is the dial within the green?: {q19}\n")
    file.write(f"Is the extinguisher clear of debris?: {q20}\n")


    ticket_number11 = int(input("Parks workbench ticket number:"  ))
    q21 = str(input("Is the dial within the green?: "))
    q22 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Parks workbench ticket number: {ticket_number11}\n")
    file.write(f"Is the dial within the green?: {q21}\n")
    file.write(f"Is the extinguisher clear of debris?: {q22}\n")

    ticket_number12= int(input("Garage bay 4 ticket number:"  ))
    q23 = str(input("Is the dial within the green?: "))
    q24= str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 4 ticket number: {ticket_number12}\n")
    file.write(f"Is the dial within the green?: {q23}\n")
    file.write(f"Is the extinguisher clear of debris?: {q24}\n")

    print("Main garage checklist")

    ticket_number13 = int(input("Garage bay 5 ticket number:"  ))
    q25 = str(input("Is the dial within the green?: "))
    q26 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 5 ticket number: {ticket_number13}\n")
    file.write(f"Is the dial within the green?: {q25}\n")
    file.write(f"Is the extinguisher clear of debris?: {q26}\n")


    ticket_number14 = int(input("Garage bay 8 ticket number:"  ))
    q27 = str(input("Is the dial within the green?: "))
    q28 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 8 ticket number: {ticket_number14}\n")
    file.write(f"Is the dial within the green?: {q27}\n")
    file.write(f"Is the extinguisher clear of debris?: {q28}\n")


    ticket_number15 = int(input("Garage bay 11 ticket number:"  ))
    q29 = str(input("Is the dial within the green?: "))
    q30 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Garage bay 11 ticket number: {ticket_number15}\n")
    file.write(f"Is the dial within the green?: {q29}\n")
    file.write(f"Is the extinguisher clear of debris?: {q30}\n")

    ticket_number16 = int(input("Fire suppression ticket number:"  ))
    q31 = str(input("Is the dial within the green?: "))
    q32 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Fire suppression ticket number: {ticket_number16}\n")
    file.write(f"Is the dial within the green?: {q31}\n")
    file.write(f"Is the extinguisher clear of debris?: {q32}\n")

    print("Fueling stations checklist")

    ticket_number17 = int(input("Gas fuel station ticket number:"  ))
    q33 = str(input("Is the dial within the green?: "))
    q34 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Gas fuel station ticket number: {ticket_number17}\n")
    file.write(f"Is the dial within the green?: {q33}\n")
    file.write(f"Is the extinguisher clear of debris?: {q34}\n")

    ticket_number18 = int(input("Diesel fuel station ticket number:"  ))
    q35= str(input("Is the dial within the green?: "))
    q36 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Diesel fuel station ticket number: {ticket_number18}\n")
    file.write(f"Is the dial within the green?: {q35}\n")
    file.write(f"Is the extinguisher clear of debris?: {q36}\n")


    print("Office floor Checklist:")


    ticket_number19 = int(input("Mezzanine ticket number:"  ))
    q37 = str(input("Is the dial within the green?: "))
    q38 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Mezzanine ticket number: {ticket_number19}\n")
    file.write(f"Is the dial within the green?: {q37}\n")
    file.write(f"Is the extinguisher clear of debris?: {q38}\n")


    ticket_number20 = int(input("Lunchroom hallway ticket number:"  ))
    q39 = str(input("Is the dial within the green?: "))
    q40 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Lunchroom hallway ticket number: {ticket_number20}\n")
    file.write(f"Is the dial within the green?: {q39}\n")
    file.write(f"Is the extinguisher clear of debris?: {q40}\n")

    ticket_number21 = int(input("Locker room ticket number:"  ))
    q41 = str(input("Is the dial within the green?: "))
    q42 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Locker room ticket number: {ticket_number21}\n")
    file.write(f"Is the dial within the green?: {q41}\n")
    file.write(f"Is the extinguisher clear of debris?: {q42}\n")


    ticket_number22 = int(input("Office ticket number:"  ))
    q43 = str(input("Is the dial within the green?: "))
    q44 = str(input("Is the extinguisher clear of debris?: "))
    file.write(f"Office ticket number: {ticket_number22}\n")
    file.write(f"Is the dial within the green?: {q43}\n")
    file.write(f"Is the extinguisher clear of debris?: {q44}\n")

print("Data has been saved to inspection_checklist.txt")
