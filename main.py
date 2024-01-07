print("enter a binary number up to 8 digits")
binary = input()
dec_arr = []
for i in range(len(binary)):
        dec_arr.append(pow(int(binary[i])*2,-1*(i-(len(binary)-1))))
if int(binary[-1]) == 0:
    dec_arr[-1] = 0
print(sum(dec_arr))