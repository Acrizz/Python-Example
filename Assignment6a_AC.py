
def Validate_Integer_Input( int_Input ):
   try:
        int_Input = float(int_Input)                     # int_Input = int(int_Input)
        if(int_Input > 0):                 
            global strFlag
            strFlag = True
        else:
            print("Value Must Be Positive")
   except ValueError:
        int_Input = int(0)
        print("Value Must be Numeric")
   return int_Input


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
            
    #else:
     #   if int_Employment_Type == 2:
          #  if int_AirFare_Cost > 400:
       #         intAirfareReimbursement = 400
      #  else:
         #    intAirFare_Reimbursement = int_AirFare_Cost
          #   return intAirfareReimbursement



def Get_Food_Reimbursement(int_NumDays, int_Employment_Type):
    intFoodReimbursement = float()
    if int_Employment_Type == 1.0:
        intFoodReimbursement = int_NumDays * 75
        return intFoodReimbursement
    if int_Employment_Type == 2.0:  
         intFoodReimbursement = int_NumDays * 50
         return intFoodReimbursement


def Get_Lodging_Reimbursement(int_NumDays, int_Employment_Type):
    intLodgingReimbursement = float()
    if int_Employment_Type == 1.0:
        intLodgingReimbursement = int_NumDays * 125
        return intLodgingReimbursement
    if int_Employment_Type == 2.0:
        intLodgingReimbursement = int_NumDays * 100
        return intLodgingReimbursement

def Get_TravelCost(int_NumDays, int_LodgingCost, int_FoodCost, int_Airfarecost):
    dblTravelCost = float(0)
    dblTravelCost = (int_NumDays * int_LodgingCost) + (int_NumDays * int_FoodCost) + int_Airfarecost
    return dblTravelCost
    #print("The total travel cost is ", dblTravelCost)

#def Get_Total_Reimbursement(int_AirfareReimbursement, int_LodgingReimbursement, int_foodReimbursement):
#   dblTotalReimbursement = float(0)
 #  dblTotalReimbursement = int_AirfareReimbursement + int_LodgingReimbursement + int_foodReimbursement
 #  return dblTotalReimbursement

#def Get_Employee_Responsibility(dblTravelCost, dblTotalReimbursement):
   # dblEmployeeResponsibility = float(0)
  #  dblEmployeeResponsibility = dblTravelCost - dblTotalReimbursement
   # return dblEmployeeResponsibility



###
intNumDays = int(0) 
intAirfarecost = int(0)
intLodgingCost = int(0)
intFoodCost = int(0)
intTotalTravelCost = int(0)
intEmploymentType = int(0)
intTotalReimbursement = int(0)


strFlag = bool(False)
while strFlag is False:
    intEmploymentType = (input("Please enter 1 for management or 2 for non-management: "))
    Validate_Employment_Type(intEmploymentType)
strFlag = bool(False)
while strFlag is False:
    intNumDays = (input("Please enter number of days of trip: "))
    Validate_Integer_Input(intNumDays)
strFlag = bool(False)
while strFlag is False:
    intAirfareCost = (input("Please enter Airfare Cost: "))
    Validate_Integer_Input(intAirfareCost)
strFlag = bool(False)
while strFlag is False:
    intLodgingCost = (input("Please enter total lodging costs: "))
    Validate_Integer_Input(intLodgingCost)
strFlag = bool(False)
while strFlag is False:
    intFoodCost = (input("Please enter total food costs: "))
    Validate_Integer_Input(intFoodCost)


intTotalTravelCost = Get_TravelCost(intNumDays, intLodgingCost, intFoodCost, intAirfareCost)
print("The total travel costs are : ", intTotalTravelCost)

intAirfareReimbursement = Get_Airfare_Reimbursement(intEmploymentType, intAirfareCost)
intFoodReimbursement = Get_Food_Reimbursement(intNumDays, intEmploymentType)
intLodgingReimbursement = Get_Lodging_Reimbursement(intNumDays, intEmploymentType)

intTotalReimbursement = intAirfareReimbursement + intFoodReimbursement + intLodgingReimbursement
print("The total amount reimbursed by company is ", intTotalReimbursement)

intTotalEmployeeResponsible = intTotalTravelCost - intTotalReimbursement
print("The total amount employee is responsible for is ", intTotalEmployeeResponsible)








             

        
            
            
    
