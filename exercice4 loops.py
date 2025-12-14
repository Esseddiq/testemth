invalid=0
count=0
sum=0
while True:
    str_number=input("please enter a number:\n")
    if str_number=="done":
        break
    try:
        number=int(str_number)
        count=count+1
        sum=sum+number
    except:
        print("Invalid data")
        invalid=invalid+1
if count>0:
    print("you've entered",count,"numbers")
    print("their sum =",sum,)
    print("their avrege =",sum/count)
    print("you've entered",invalid,"invalid inputs")
else :
    print ("No valid numbers were entered!!")
    print("you've entered",invalid,"invalid inputs")