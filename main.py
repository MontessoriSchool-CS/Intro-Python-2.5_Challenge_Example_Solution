# FORK ME or copy the code!  Please don't request edit access. This is the original so it needs to stay undedited for all users.

#Get input for height & width. Convert to integers and store in variables

height = int(input("Enter the height of the rectangle in centimetres."))

width = int(input("Enter the width of the rectangle in centimetres."))

#Calculate the area & store the result in the area variable

area = height * width

#Output the area variable (converted to string)

print("The area of the rectangle is " + str(area) + "cm2")

#Another way of outputting integer as string is replace line 9 with area = str(height * width)

#Then you don't need the str on line 13