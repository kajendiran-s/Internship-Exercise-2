def order(num):
    n = 0
    while(num != 0):
        n += 1
        num = num // 10
    return n


def IsArmstrong(num):
    n = order(num)
    temp = num
    sum = 0
    while(temp != 0):
        dig = temp%10
        sum += dig**n
        temp //= 10

    if(num == sum):
        return "Armstrong number"
    else:
        return "Not an Armstrong number"

print(IsArmstrong(4071))
