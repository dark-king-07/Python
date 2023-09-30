l = list(int(num) for num in input('Enter 3 numbers\n').split())
li = sorted(l)
sq = [x**2 for x in li]
if(sq[0] + sq[1] == sq[2]):
    print("Yes it is a right angled triangle. Sides are: ",l)
else:
    print("No it is not a right angled triangle. Sides are: ",l)
