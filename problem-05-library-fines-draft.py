try:
    d_over = int(input("Enter overdue:"))
except ValueError:
    print("Invalid input of \"days overdue\"")
    exit()    
if d_over<0:
    print("Days overdue can't be negative")
    exit()  
b_type=input("Enter book type:")            
if b_type.lower() not in ["fiction", "non-fiction", "reference"]:
    print("Invalid booktype!")
    exit()
membership=input("Are you had mambership:")
if membership.lower() not in ["premium","regular","non-member"]:
    print("Invalid input of member!")
    exit()
 
tier1_p=5
tier2_p=10
tier3_p=20
tier4_p=50
 
days_1=0
days_2=0
days_3=0
days_4=0

day_con1=7
day_con2=14
day_con3=30

if d_over <=day_con1:
    base_fine=d_over*tier1_p
    print(f"Base fine:{d_over}days X ${tier1_p}=${base_fine:.2f}")
elif d_over>=8 and d_over<=day_con2:
    days_2=d_over-day_con1
    base_fine=day_con1*tier1_p+days_2*tier2_p
    print(f"Base fine:{day_con1}days X ${tier1_p}+{days_2}days X ${tier2_p}=${base_fine:.2f}")
elif d_over>day_con2 and d_over<=day_con3:
    days_3=d_over-day_con2
    days_2=day_con2-day_con1
    base_fine=day_con1*tier1_p+days_2*tier2_p+days_3*tier3_p
    print(f"Base fine:{day_con1}days X ${tier1_p}+{days_2}days X ${tier2_p}+{days_3}days X ${tier3_p}=${base_fine:.2f}")
elif d_over>=31:
    days_4=d_over-day_con3
    days_3=day_con3-day_con2
    days_2=day_con2-day_con1
    base_fine=day_con1*tier1_p+days_2*tier2_p+days_3*tier3_p+days_4*tier4_p
    print(f"Base fine:{day_con1}days X ${tier1_p}+{days_2}days X ${tier2_p}+{days_3}days X {tier3_p}+{days_4}days X {tier4_p}=${base_fine:.2f}")

if b_type.lower() == "fiction":
    multi_x="1x"
    base_fine*=1     # no change because it is fiction book
elif b_type.lower() == "non-fiction":
    multi_x="1.5x"
    base_fine*=1.5      
elif b_type.lower() == "reference":
    multi_x="2x"
    base_fine*=2
    
print(f"Multiplier the fine by book type:{b_type}({multi_x})=${base_fine:.2f}")  

if membership.lower() == "non-member":
    d=0.0
    d_p=0
    m_d=base_fine*d
elif membership.lower() == "regular":
    d=0.1
    d_p=10
    m_d=base_fine*d
elif membership.lower() == "premium":
    d=0.2
    d_p=20
    m_d=base_fine*d                                              
print(f"Membership discount:{d_p}%=-${m_d:.2f}")
base_fine-=m_d    
print(f"After discount:{base_fine:.2f}")       

if base_fine > 500:
    base_fine=500
print(f"Final fine:${base_fine:.2f}")    