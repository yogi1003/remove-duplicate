
data = open(input("your file: "), "r")
lines = data.readlines()
result = open("result.txt", "w")
count=0
dup = []

for licate in lines:
    count+=1
    print(f"\rfrom : {count} lines", end='')
    if licate not in dup:
        dup.append(licate)
count=0
print()
for nodup in dup:
    count+=1
    result.write(nodup)
    print(f"\rto : {count} lines", end='')
print('\n')

data.close()
result.close()
print("Finish : result.txt")
