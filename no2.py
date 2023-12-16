count = 0
while True:
    wight = float(input())
    hight = float(input())
    # print(wight,hight)
    if int(wight) <= 0 or int(hight) <= 0:
        break
    bmi = wight / ((hight / 100) ** 2)
    # print(wight, hight)
    # print(bmi)
    if bmi < 18.5:
        count += 1

print(f"BMI < 18.5 = {count}")
