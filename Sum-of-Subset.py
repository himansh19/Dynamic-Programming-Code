# sum of subset

def sum_of_subset(s,k,rem):
    x[k]=1
    if s+my_list[k]==target_sum:
        list1=[]
        for i in range (0,k+1):
            if x[i]==1:
                list1.append(my_list[i])
        print( list1 )       
    elif s+my_list[k]+my_list[k+1]<=target_sum :
        sum_of_subset(s+my_list[k],k+1,rem-my_list[k])
    if s+rem-my_list[k]>=target_sum and s+my_list[k+1]<=target_sum :
        x[k]=0
        sum_of_subset(s,k+1,rem-my_list[k])

my_list=[]
n=int(input("Enter number of elements"))
print('Number of elements: ', n)
total=0
for i in range (0,n):
    ele=int(input())
    my_list.append(ele) 
    total=total+ele
my_list.sort()    
print(my_list)
target_sum=int(input("Enter required Sum"))    
print('Required Sum: ',target_sum)
x=[0]*(n+1)
sum_of_subset(0,0,total)     
