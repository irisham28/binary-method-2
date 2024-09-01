#binary search method 2

array = list(map,input("enter the numbers ").split(" "))

finding_item = input("which item are you looking for?")

start = 0 
end = len(array)-1
flag = False

while start<=end:
    mid =(start+end)//2

    if array[mid] == finding_item:
        print("you got it!")
        flag = True
        break

    elif array[mid] >finding_item:
        end= mid-1

    else:
        start = mid+1


if flag==False:
    print("we never got ur number")


