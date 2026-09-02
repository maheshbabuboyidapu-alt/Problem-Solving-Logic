years=int(input("Enter the employee years of experience:"))

if years < 0 :
	print("Years can't be negative, please enter valid years of experience!")
	exit()
	
rating=input("Enter the performance rating of employee (Poor/Average/Good/Excellent):")

if rating.lower() not in ["poor","average","good","excellent"]:
	print("Invalid rating!, please enter only in (Poor/Average/Good/Excellent).")
	exit()
	
attendance=int(input("Enter the employee attendance percentage:"))
if attendance <0 or attendance > 100:
	print("Invalid employee attendance percentage! \nplease enter valid employee attendance percentage")
	exit()	

zero_p=0.00
five_p=0.05
ten_p=0.10
twenty_p=0.20
thirty_p=0.30

zero=0
five=5
ten=10
twenty=20
thirty=30

# Base salary by experience years

if years <= 2:
	    base_salary=25000
elif years <= 5:
	    base_salary=40000
elif years <= 10:
	    base_salary=60000
elif years >= 11:
	    base_salary=90000	    		    
	    
print(f"Base salary : ₹{base_salary:.2f}")

# Bonus adding based on performance rating

if rating.lower() == "poor" :
	per_b=zero_p
	dec_b=zero
elif rating.lower() == "average" :
	per_b=five_p
	dec_b=five
elif rating.lower() == "good" :
	per_b=ten_p
	dec_b=ten
elif rating.lower() == "excellent" :
	per_b=twenty_p
	dec_b=twenty
	
bonus=base_salary*per_b

print(f"Bonus:{dec_b}%=₹{bonus:.2f}")

base_salary+=bonus

print(f"After bonus:₹{base_salary:.2f}")

# Penalty apply based on attendance

if attendance < 70 :
			per_p=twenty_p
			dec_p=twenty
elif attendance < 85 :
			per_p=ten_p
			dec_p=ten
elif attendance < 95 :
			per_p=five_p
			dec_p=five
elif attendance <= 100 :
			per_p=zero_p
			dec_p=zero
			
penalty=base_salary*per_p

print(f"Attendance penalty:{dec_p}%=₹{penalty:.2f}")

base_salary-=penalty

print(f"After penalty:₹{base_salary:.2f}")

if base_salary <= 30000 :
			per_t=zero_p
			dec_t=zero
elif base_salary <= 60000 :
	    	per_t=ten_p
	    	dec_t=ten
elif base_salary <= 100000:
		    per_t=twenty_p
		    dec_t=twenty
elif base_salary > 100000 :
	        per_t=thirty_p
	        dec_t=thirty

tax = base_salary*per_t	        	        		

print(f"Tax: {dec_t}%=₹{tax:.2f}")	

final_salary = base_salary-tax

print(f"Final salary:₹{final_salary:.2f}")