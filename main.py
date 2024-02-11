arr = [4,2,3,4,6]
max = arr[0]
for i in range (len(arr)):
   if  max < arr[i]:
    max = arr[i]

print(max)
