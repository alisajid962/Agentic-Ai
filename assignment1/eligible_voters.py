total_voters=0
voter_ages=[]
eligible_voters=0
non_eligible_voters=0
while total_voters<10:
    voter_age=int(input("Enter Your Age Please: "))
    if 18<=voter_age<120:
        voter_ages.append(voter_age)
        eligible_voters=eligible_voters+1
        total_voters=total_voters+1
    elif(0==voter_age>120):
        continue
    else:
        non_eligible_voters=non_eligible_voters+1
# ========================================
sum=0
for age in voter_ages:
    sum=age+sum
no_of_ages=len(voter_ages)
average=sum/no_of_ages


    
print(f"Eligible Voter Ages: ",voter_ages)
print(f"Average of Eligible voters age of the eligble voter: {average}")
print(f"No of Eligible voters: {eligible_voters}")
print(f"No of Non Eligible voters: {non_eligible_voters}")


    
      
    


