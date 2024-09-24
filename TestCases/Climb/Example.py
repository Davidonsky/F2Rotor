# Example data

 
#Authors: Alessandra Di Rauso, Sara Vitale
    #Date: 16/06/2024
    #Version: 1.00

Pd = 1000  
Pn = 200   
MTOW = 1500  
Voo = 70  

     
  #Available power Pd, Main and tail rotor power Pn, Maximum takeoff weight MTOW, Horizontal speed (fixed) Voo, Acceleration due to gravity 

 #Create the Helicopter object with the provided data

properties, climb = Helicopter_properties(Pd, Pn, MTOW, Voo)


 #Calculate the rate of climb and the climb angle

ROC, gamma = climb()

 #Display the results of the example

print("Example calculation:")
print("Rate of Climb (ft/min):", ROC)
print("Climb Angle (degrees):", gamma)
print("---------")


 #Test with other scenarios

test_cases = [
    (1200, 500, 1800, 50),
    (1200, 300, 1800, 70),
    (1200, 100, 1800, 100)
]

print("Test with other scenarios:")
test_Helicopter_climb(test_cases)
