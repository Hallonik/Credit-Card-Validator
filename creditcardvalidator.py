#use luhns algorithm to check the validity of a credit card no.

card_no="35009010075"
odd_sum=0
even_sum=0
double_list=[]

number=list(card_no)
for (idx,val) in enumerate(number):
    if idx%2!=0:                    #this is an odd no.
        odd_sum+=int(val)
    else:                          #this is an even no
        double_list.append(int(val)*2)



#converting a list into a string
double_string=""
for x in double_list:
    double_string+=str(x)

#converting a string back to a list
double_list= list (double_string)

for x in double_list:
    even_sum+=int(x)

net_sum=odd_sum+even_sum

if net_sum%10==0:
    print("Valid Card")

else:
    print("Invalid card")




