
#Aleksander Chrismer
#OOP
#Assignment 6a


#Validate integer inputs
def Validate_Integer_Input( int_Input ):
   try:
        int_Input = int(int_Input)
        if(int_Input > 0):                 
            global strFlag
            strFlag = True
        else:
            print("Value Must Be Positive")
   except ValueError:
        int_Input = int(0)
        print("Value Must be Numeric")
   return int_Input

#Validte employment input
def Validate_Employment_Type( int_Employment ):
   try:
        int_Employment = int(int_Employment)
        if(int_Employment == 1) | (int_Employment == 2):
            global strFlag
            strFlag = True
        else:
            print("Please select 1 or 2 based on employment status")
   except ValueError:
        int_Employment = int(0)
        print("Please select 1 or 2 based on employment status")
   return int_Employment



#Get airfare reimbursement
def Get_Airfare_Reimbursement(int_Employment_Type, int_AirFare_Cost):   
    intAirfareReimbursement = float()
    if int_Employment_Type == 1.0:
        if int_AirFare_Cost > 500:
            intAirfareReimbursement = 500
        else:
            intAirFareReimbursement = int_AirFare_Cost
            return intAirFareReimbursement
    if int_Employment_Type == 2.:
        if int_AirFare_Cost > 400:
            intAirFareReimbursement = 400
        else:
            intAirFareReimbursement = int_AirFare_Cost
            return intAirFareReimbursement
            
        #Get food reimbursement
def Get_Food_Reimbursement(int_NumDays, int_Employment_Type):
    intFoodReimbursement = float()
    if int_Employment_Type == 1.0:
        intFoodReimbursement = int_NumDays * 75
        return intFoodReimbursement
    if int_Employment_Type == 2.0:  
         intFoodReimbursement = int_NumDays * 50
         return intFoodReimbursement

     #get lodging reimbursement
def Get_Lodging_Reimbursement(int_NumDays, int_Employment_Type):
    intLodgingReimbursement = float()
    if int_Employment_Type == 1.0:
        intLodgingReimbursement = int_NumDays * 125
        return intLodgingReimbursement
    if int_Employment_Type == 2.0:
        intLodgingReimbursement = int_NumDays * 100
        return intLodgingReimbursement

    #Get total travel cost
def Get_TravelCost(int_LodgingCost, int_FoodCost, int_Airfarecost):
   intTravelCost = float(0)
   intTravelCost = (int_LodgingCost) + (int_FoodCost) + (int_Airfarecost)
   return intTravelCost

  #print travel cost 
def Print_Travel_Cost(intTravelCost):
    intTravelCost = "${:,.2f}".format(intTravelCost)
    print("The total travel costs are: ", intTravelCost)

    #calculate total reimbursement
def Get_Total_Reimbursement(int_AirfareReimbursement, int_LodgingReimbursement, int_foodReimbursement):
   dblTotalReimbursement = float(0)
   dblTotalReimbursement = int_AirfareReimbursement + int_LodgingReimbursement + int_foodReimbursement
   return dblTotalReimbursement

#print total reimbursement
def Print_Total_Reimbursement(int_Total_Reimbursement):
    int_Total_Reimbursement = "${:,.2f}".format(int_Total_Reimbursement)
    print("The total amount reimbursed by company is ", int_Total_Reimbursement)

    #Calculate employee responsibility
def Get_Employee_Responsibility(dblTravelCost, dblTotalReimbursement):
   dblEmployeeResponsibility = float(0)
   dblEmployeeResponsibility = dblTravelCost - dblTotalReimbursement
   return dblEmployeeResponsibility

#print employee responsibility
def Print_Employee_Responsibility(int_Employee_Responsibility):
    int_Employee_Responsibility = "${:,.2f}".format(int_Employee_Responsibility)
    print("The total employee responsibility is", int_Employee_Responsibility)


#########
###Main####

intNumDays = int(0) 
intAirfarecost = int(0)
intLodgingCost = int(0)
intFoodCost = int(0)
intTotalTravelCost = int(0)
intEmploymentType = int(0)
intTotalReimbursement = int(0)
intTotalEmployeeResponsible = int(0)

#entering inputs and validating
strFlag = bool(False)
while strFlag is False:
    intEmploymentType = (input("Please enter 1 for management or 2 for non-management: "))
    intEmploymentType = Validate_Employment_Type(intEmploymentType)
strFlag = bool(False)
while strFlag is False:
    intNumDays = (input("Please enter number of days of trip: "))
    intNumDays = Validate_Integer_Input(intNumDays)
strFlag = bool(False)
while strFlag is False:
    intAirfarecost = (input("Please enter Airfare Cost: "))
    intAirfarecost = Validate_Integer_Input(intAirfarecost)
strFlag = bool(False)
while strFlag is False:
    intLodgingCost = (input("Please enter total lodging costs: "))
    intLodgingCost = Validate_Integer_Input(intLodgingCost)
strFlag = bool(False)
while strFlag is False:
    intFoodCost = (input("Please enter total food costs: "))
    intFoodCost = Validate_Integer_Input(intFoodCost)

#calling function to get travel costs and printing
intTotalTravelCost = Get_TravelCost(intLodgingCost, intFoodCost, intAirfarecost)
Print_Travel_Cost(intTotalTravelCost)

intAirfareReimbursement = Get_Airfare_Reimbursement(intEmploymentType, intAirfarecost)
intFoodReimbursement = Get_Food_Reimbursement(intNumDays, intEmploymentType)
intLodgingReimbursement = Get_Lodging_Reimbursement(intNumDays, intEmploymentType)

#calling function to get total reimbursement and printing
intTotalReimbursement = Get_Total_Reimbursement(intAirfareReimbursement, intFoodReimbursement, intLodgingReimbursement)
Print_Total_Reimbursement(intTotalReimbursement)

#calling function to get total amount employee is responsible for and printing
intTotalEmployeeResponsible = Get_Employee_Responsibility(intTotalTravelCost, intTotalReimbursement)
Print_Employee_Responsibility(intTotalEmployeeResponsible)








             

        
            
            
    
