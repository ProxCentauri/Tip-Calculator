print("welcome to the tip calculator")

bill = float(input("what was the amt of your bill? $"))
tip = int(input("what amt of tip would you like to give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
tip_percent = tip/100
split = bill * tip_percent
final_tip = bill + split
final_to_give = final_tip/people
print (f"each person should pay {final_to_give}")
