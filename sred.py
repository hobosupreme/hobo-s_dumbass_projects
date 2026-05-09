temp = int(input("Enter the temperature (in degrees): "))
rain = str(input("Is it raining? (y/n): "))
rain = bool(rain == "y" or rain == "y")
    

if temp <= 32 :
    outfit = "Wear a heavy coat"
elif temp > 32 and temp <= 60:
    outfit = "Wear a jacket"
elif temp > 60 and temp <= 80 : 
    outfit = "Wear a t-shirt"
elif temp > 80 :
    outfit = "Wear shorts"

if(rain == True) : 
    outfit = outfit + " and bring an umbrella"
elif(rain == False) :
    outfit = outfit + " and sunglasses"
else :
    outfit = "Check your inputs"

print("Suggestion: " + outfit)