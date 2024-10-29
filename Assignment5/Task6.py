coins = [1,2,5]
amount = 67
ans = 0
while(amount != 0):
    if(amount >= 5):
        if(amount%5 == 0):
            ans = ans + amount//5
            amount = 0
        else:
            ans += amount//5
            amount = amount % 5
    elif(amount >= 2):
        if(amount%2 == 0):
            ans += amount//2
            amount = 0
        else:
            ans += amount//2
            amount = amount % 2
    else:
        ans += 1
        amount -= 1


print(ans)