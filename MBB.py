# Write your code here :-)
# MBBs
# Convert large numbers into X.XXM and X.XXB

print('Hello there')
print('Please input the list of numbers for conversion, with a space separating the numbers. Do not include decimal points or commas in your numbers.')
print('At the moment, this program will not be able to round up the numbers when required.')
numbers = input('>')
num_list = numbers.split()

for i in range(0, len(num_list)):
    num_list[i] = int(num_list[i])

print('Your number list is ' + str(num_list))

mbb_list = []
for i in range(0, len(num_list)):
    if num_list[i] > 999999999:
        num_list[i] = str(num_list[i])
        rounder = num_list[i][-7]
        rounder = int(rounder)
        if rounder >= 5:
            print('round below number up')
        bnum = num_list[i][:-9] + '.' + num_list[i][-9:-7] + 'B'
        mbb_list.append(bnum)
        print(bnum)
    else:
        num_list[i] = str(num_list[i])
        rounder = num_list[i][-4]
        rounder = int(rounder)
        if rounder >= 5:
            print('round below number up')
        mnum = num_list[i][:-6] + '.' + num_list[i][-6:-4] + 'M'
        mbb_list.append(mnum)
        print(mnum)

print(mbb_list)
