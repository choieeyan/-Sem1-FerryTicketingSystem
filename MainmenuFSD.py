def MainMenu():
    print("\n")
    print("FERRY TICKETING SYSTEM")
    print("P-to Purchase Ticket")
    print("V-to View Seating Arrangment")
    print("Q-to Quit the system")
    option=input("Choose One Option(eg:V):")
    if (option=="P"):
        P()
    elif (option=="V"):
        V()
    elif (option=="Q"):
        Q()
    else:
        print ("Invalid entry.")
        MainMenu()

def P():
    while True:
        print("\n")
        print("DESTINATION OF TRIP")
        print("1 = Penang to Langkawi")
        print("2 = Langkawi to Penang")
        print("3 = return to Main Menu")
        print("The duration of the trip is 3 hours.")
        place = input("Please choose your destination(eg:1):")
        if(place=="1"):
            destination="Penang"
            PtL(destination)
            break
        elif(place=="2"):
            destination="Langkawi"
            LtP(destination)
            break
        elif(place=="3"):
            break
            MainMenu()
        else:
            print("Invalid entry.")
            continue

def PtL(destination):
    print("\n")
    print ("DEPARTURE TIME:")
    print ("F001 - 10am")
    print ("F002 - 11am")
    print ("F003 - 12pm")
    print ("F004 - 01pm")
    print ("F005 - 02pm")
    print ("F006 - 03pm")
    print ("F007 - 04pm")
    print ("F008 - 05pm")
    FerryID = input("Please select your time of departure(eg.F001): ")
    textfile= open("PtL"+FerryID+".txt", "r+")
    textfile.seek(0)
    if "0" in textfile.read():
            classtype(textfile,FerryID, destination)
    else:
        print ("This trip is fully booked. Next triip leaves in 1 hour.")
        repeat = input ("Do you want to select another time?(yes/no)")
        if (repeat == "yes"):
            PtL()
        else:
            MainMenu()
 
def LtP(destination):
    print("\n")
    print ("DEPARTURE TIME:")
    print ("F005 - 10am")
    print ("F006 - 11am")
    print ("F007 - 12pm")
    print ("F008 - 01pm")
    print ("F001 - 02pm")
    print ("F002 - 03pm")
    print ("F003 - 04pm")
    print ("F004 - 05pm")
    FerryID = input("Please select your time of departure(eg.F001): ")
    textfile= open("LtP"+FerryID+".txt", "r+")
    textfile.seek(0)
    if "0" in textfile.read():
        classtype(textfile, FerryID, destination)
    else:
        print("This trip is fully booked. Next trip leaves in 1 hour.")
        repeat = input ("Do you want to select another time?(yes/no)")
        if (repeat == "yes"):
            PtL()
        else:
            MainMenu()
 
                   
def classtype(textfile, FerryID, destination):
    print("\n")
    print("PURCHASING MODULE")
    print("B-to purchase ticket for Business class")
    print("E-to purchase ticket for Economy class")
    print("M-to return to Previous Menu")
    classchoice = input("Select your class(eg.B): ")
    if(classchoice=="B"):
        textfile.seek(0)
        if "0" in textfile.read(10):
            business(textfile, FerryID, destination)
        else:
            bte = input("Business class is full, would you like to purchaase economy class?")
            if (bte == "yes"):
                economy(textfile, FerryID, destination)  
            else:
                MainMenu() 
    elif(classchoice=="E"):
        economy(textfile, FerryID, destination)
    elif(classchoice=="M"):
        Time()


def business(textfile, FerryID, destination):
    fare = "Rm 120"
    typeofclass = "Business"
    textfile.seek(0)
    seat = list(textfile.read())
    print("\n")
    print("*************************************************************************")
    print("   *   BUSINESS CLASS                                                   *")
    print("*************************************************************************")
    print("   *      1      *      2      *      3      *      4      *     5      *") 
    print("*************************************************************************")
    print(" A *     ",seat[0],"     *     ",seat[1],"     *     ",seat[2],"     *     ",seat[3],"     *    ",seat[4],"     *"),
    print("*************************************************************************")
    print(" B *     ",seat[5],"     *     ",seat[6],"     *     ",seat[7],"     *     ",seat[8],"     *    ",seat[9],"     *"),
    print("*************************************************************************")
    print("\n")
    print ("1 = seat is taken, 0 = empty seat")
    selectseat = input("Please choose your seat (eg. A1):")
    y = int(selectseat[1])      
    if (y>=1) and (y<=5):
        if (selectseat[0]== "A"):
            x = y -1       
        elif (selectseat[0] == "B"):
            x = y + 4      
    else:
        print ("Invalid seat. Enter a correct seat")
        business(textfile, FerryID, destination)

    while True:
        if (seat[x] == "1"):
            print ("This seat is taken. Please choose another seat.")
            business(textfile, FerryID, destination)
            break
        else:
            seat [x] = 1
            break
    
    while True:
        print("The price for this seat is", fare)
        purchase = input("Are you sure you want to purchase this seat? (yes/no)")
        if (purchase=="yes"):
            name = input("Please enter your name: ")
            textfile.seek(0)
            textfile.write("".join(str(i) for i in seat))
            textfile.close()
            boardingticket(FerryID, destination, name, selectseat, typeofclass, fare)
            break
        elif (purchase=="no"):
            MainMenu()
            break
        else:
            print("Please enter a valid choice")
            business(textfile, FerryID, destination)
            break
            
            

def economy(textfile, FerryID, destination):
    fare = "Rm 80"
    typeofclass = "Economy"
    textfile.seek(0)
    seat = list(textfile.read())
    print("\n")
    print("*************************************************************************")
    print("   *   ECONOMY CLASS                                                    *")
    print("*************************************************************************")
    print("   *      1      *      2      *      3      *      4      *     5      *")  
    print("*************************************************************************")
    print(" C *     ",seat[10],"     *     ",seat[11],"     *     ",seat[12],"     *    ",seat[13],"     *     ",seat[14],"     *"),
    print("*************************************************************************")
    print(" D *     ",seat[15],"     *     ",seat[16],"     *     ",seat[17],"     *    ",seat[18],"     *     ",seat[19],"     *")
    print("*************************************************************************")
    print(" E *     ",seat[20],"     *     ",seat[21],"     *     ",seat[22],"     *    ",seat[23],"     *     ",seat[24],"     *"),
    print("*************************************************************************")  
    print(" F *     ",seat[25],"     *     ",seat[26],"     *     ",seat[27],"     *    ",seat[28],"     *     ",seat[29],"     *"),
    print("*************************************************************************")
    print(" G *     ",seat[30],"     *     ",seat[31],"     *     ",seat[32],"     *    ",seat[33],"     *     ",seat[34],"     *"),
    print("*************************************************************************")
    print(" H *     ",seat[35],"     *     ",seat[36],"     *     ",seat[37],"     *    ",seat[38],"     *     ",seat[39],"     *"),
    print("*************************************************************************")
    print(" I *     ",seat[40],"     *     ",seat[41],"     *     ",seat[42],"     *    ",seat[43],"     *     ",seat[44],"     *"),
    print("*************************************************************************")
    print(" J *     ",seat[45],"     *     ",seat[46],"     *     ",seat[47],"     *    ",seat[48],"     *     ",seat[49],"     *"),
    print("*************************************************************************")
    print("\n")
    print ("1 = seat is taken, 0 = empty seat")
    selectseat = input("Please choose your seat (eg. D1):")
    y = int(selectseat[1])
    if (y>=1) and (y<=5):
        if (selectseat[0]== "C"):
            x = y + 9      
        elif (selectseat[0]=="D"):
            x = y + + 14
        elif (selectseat[0]=="E"):
            x = y + 19
        elif (selectseat[0]=="F"):
            x = y + 24
        elif (selectseat[0]=="G"):
            x = y + 29             
        elif (selectseat[0]=="H"):
            x = y + 34
        elif (selectseat[0]=="I"):
            x = y + 39
        elif (selectseat[0]== "J"):
            x = y + 44
            
    else:
        print ("Invalid seat. Enter a correct seat.")
        economy(textfile, FerryID, destination)
        
    while True:
        if (seat[x] == "1"):
            print ("This seat is taken. Please choose another seat.")
            economy(textfile, FerryID, destination)
            break
        else:
            seat [x] = 1
            break

    while True:
        print("The price for this seat is", fare)
        purchase = input("Are you sure you want to purchase this seat? (yes/no)")
        if (purchase=="yes"):
            name = input("Please enter your name: ")
            textfile.seek(0)
            textfile.write("".join(str(i) for i in seat))
            textfile.close()
            boardingticket(FerryID, destination, name, selectseat, typeofclass, fare)
            break
        elif (purchase == "no"):
            MainMenu()
            break
        else:
            print("Please enter a valid choice")
            economy(textfile, FerryID, destination)
            break
        

        
def boardingticket(FerryID, destination, name, selectseat, typeofclass, fare):
    if(FerryID=="F001"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "10am"
        else:
            source = "Langkawi"
            time = "2pm"
    elif(FerryID=="F002"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "11am"
        else:
            source = "Langkawi"
            time = "3pm"
    elif(FerryID=="F003"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "12pm"
        else:
            source = "Langkawi"
            time = "4pm"

    elif(FerryID=="F004"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "1pm"
        else:
            source = "Langkawi"
            time = "5pm"
    elif(FerryID=="F005"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "2am"
        else:
            source = "Langkawi"
            time = "10am"
    elif(FerryID=="F006"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "3pm"
        else:
            source = "Langkawi"
            time = "11am"

    elif(FerryID=="F007"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "4pm"
        else:
            source = "Langkawi"
            time = "12pm"

    elif(FerryID=="F008"):
        if (destination == "Langkawi"):
            source = "Penang"
            time = "5pm"
        else:
            source = "Langkawi"
            time = "1pm"
        

    import datetime
    x=datetime.datetime.now()
    print("This is your ticket information.\n")
    print("Boarding Ticket")
    print("---------------------------------")
    print("Name:", name)
    print("Class type:", typeofclass)
    print("Seat number:", selectseat)
    print("Date of departure:", x.strftime("%d/%m/%Y"))
    print("Time of departure:", time)
    print("Source of trip:", source)
    print("Destination of trip:", destination)
    print("FerryID:", FerryID)
    print("Fare: ",fare)
    print("---------------------------------\n")
    print("Kindly print out this boarding ticket for your departure.")
    menu=input("Please press any key to return to main menu")
    MainMenu()

def V():
    import datetime
    x=datetime.datetime.now
    print("\n")
    print("SEATING ARRANGEMENT MODULE")
    print("F-to select Ferry ID")
    print("T-to select Trip Time")
    tripview = input("Please choose:")
    if(tripview=="F"):
        f()
    elif (tripview == "T"):
        t()




def t():
    print ("TRIP TIME:")
    print ("10am")
    print ("11am") 
    print ("12pm") 
    print ("01pm") 
    print ("02pm")
    print ("03om") 
    print ("04pm") 
    print ("05pm") 
    print("Each trip takes 3 hours")
    time = input("Please enter Trip Time (eg: 10am)")     
    destination = input("Please enter the destination (Penang/Langkawi):")
    if ((time=="10am")and(destination=="Langkawi")) or ((time=="02pm")and(destination=="Penang")):
        ferryID = "F001"
    elif ((time=="11am")and(destination=="Langkawi")) or ((time=="03pm")and(destination=="Penang")):
        ferryID = "F002"
    elif ((time=="12pm")and(destination=="Langkawi")) or ((time=="04pm")and(destination=="Penang")):
        ferryID = "F003"
    elif ((time=="01am")and(destination=="Langkawi")) or ((time=="05pm")and(destination=="Penang")):
        ferryID = "F004"
    elif ((time=="02pm")and(destination=="Langkawi")) or ((time=="10am")and(destination=="Penang")):
        ferryID = "F005"
    elif ((time=="03pm")and(destination=="Langkawi")) or ((time=="11am")and(destination=="Penang")):
        ferryID = "F006"
    elif ((time=="04pm")and(destination=="Langkawi")) or ((time=="12pm")and(destination=="Penang")):
        ferryID = "F007"
    elif ((time=="05pm")and(destination=="Langkawi")) or ((time=="01pm")and(destination=="Penang")):
        ferryID = "F008"
        
    if (destination == "Langkawi"):
        textfile= open("PtL"+ferryID+".txt", "r")
        seatar(ferryID, time, destination, textfile)      
    elif (destination == "Penang"):
        textfile= open("LtP"+ferryID+".txt", "r")
        seatar(ferryID, time, destination, textfile)  
    else:
        print("invalid Trip time or destination.")
        MainMenu()


def f():
    ferryID = input("Please enter Ferry ID (eg: F001) to view seating arrangement.")
    destination = input("Please enter the destination (Penang/Langkawi):")
    if(ferryID=="F001"):
        if (destination == "Langkawi"):
            time = "10am"
        else:
            time = "2pm"
    elif(ferryID=="F002"):
        if (destination == "Langkawi"):
            time = "11am"
        else:
            time = "3pm"
    elif(ferryID=="F003"):
        if (destination == "Langkawi"):
            time = "12pm"
        else:
            time = "4pm"

    elif(ferryID=="F004"):
        if (destination == "Langkawi"):
            time = "1pm"
        else:
            time = "5pm"
    elif(ferryID=="F005"):
        if (destination == "Langkawi"):
            time = "2am"
        else:
            time = "10am"
    elif(ferryID=="F006"):
        if (destination == "Langkawi"):
            time = "3pm"
        else:
            time = "11am"

    elif(ferryID=="F007"):
        if (destination == "Langkawi"):
            time = "4pm"
        else:
            time = "12pm"

    elif(ferryID=="F008"):
        if (destination == "Langkawi"):
            time = "5pm"
        else:
           time = "1pm"
    else:
        print ("Invalid Ferry ID")
        MainMenu()
        
    if (destination == "Penang"):
        textfile= open("LtP"+ferryID+".txt", "r")
        seatar(ferryID, time, destination, textfile)       
    elif (destination=="Langkawi"):
        textfile= open("PtL"+ferryID+".txt", "r")
        seatar(ferryID, time, destination, textfile)      
    else:
        print("invalid destination")
        MainMenu()


def seatar(ferryID, time, destination, textfile):        
    seat = list(textfile.read())

    print("\n")
    print("*************************************************************************")
    print("   *   TRIP: ",destination,"                                             ")
    print("*************************************************************************")
    print("   *   Ferry ID:",ferryID, "             ", "Time:",time,"                         *")
    print("*************************************************************************")
    print("   *   BUSINESS CLASS                                                   *")
    print("*************************************************************************")
    print("   *      1      *      2      *      3      *      4      *     5      *") 
    print("*************************************************************************")
    print(" A *     ",seat[0],"     *     ",seat[1],"     *     ",seat[2],"     *     ",seat[3],"     *    ",seat[4],"     *"),
    print("*************************************************************************")
    print(" B *     ",seat[5],"     *    ",seat[6],"      *     ",seat[7],"     *     ",seat[8],"     *    ",seat[9],"     *"),
    print("*************************************************************************")
    print("   *   ECONOMY CLASS                                                    *")
    print("*************************************************************************")
    print(" C *     ",seat[10],"     *     ",seat[11],"     *     ",seat[12],"     *    ",seat[13],"     *     ",seat[14],"     *"),
    print("*************************************************************************")
    print(" D *     ",seat[15],"     *     ",seat[16],"     *     ",seat[17],"     *    ",seat[18],"     *     ",seat[19],"     *")
    print("*************************************************************************")
    print(" E *     ",seat[20],"     *     ",seat[21],"     *     ",seat[22],"     *    ",seat[23],"     *     ",seat[24],"     *"),
    print("*************************************************************************")  
    print(" F *     ",seat[25],"     *     ",seat[26],"     *     ",seat[27],"     *    ",seat[28],"     *     ",seat[29],"     *"),
    print("*************************************************************************")
    print(" G *     ",seat[30],"     *     ",seat[31],"     *     ",seat[32],"     *    ",seat[33],"     *     ",seat[34],"     *"),
    print("*************************************************************************")
    print(" H *     ",seat[35],"     *     ",seat[36],"     *     ",seat[37],"     *    ",seat[38],"     *     ",seat[39],"     *"),
    print("*************************************************************************")
    print(" I *     ",seat[40],"     *     ",seat[41],"     *     ",seat[42],"     *    ",seat[43],"     *     ",seat[44],"     *"),
    print("*************************************************************************")
    print(" J *     ",seat[45],"     *     ",seat[46],"     *     ",seat[47],"     *    ",seat[48],"     *     ",seat[49],"     *"),
    print("*************************************************************************")
    print("1 = seat is taken, 0 = empty seat\n")
    menu=input("Please press any key to return to main menu")
    MainMenu()
    
def Q():
    repeat=input("Are you sure to quit this system?(yes/no)")
    if (repeat=="yes"):
        exit()
    else:
        MainMenu()
        
MainMenu()
