total_bill=float(input("Whst was your total bill $"))
how_many_friends=int(input("How many friends you have "))
percentage=int(input("Tip percentage "))

total_bill_now=total_bill+ (total_bill*percentage/100)
output_num=total_bill_now/how_many_friends
print(f"Each person has to pay ${output_num}")