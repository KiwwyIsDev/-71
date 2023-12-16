day = float(input("Day : "))
month = float(input("Month : "))


if (int(month) <= 0 or int(month) > 12) or (int(day) <= 0 or int(day) > 31):
    print('error')
else:
    # print(day, month)

    monthList = {
        1: {
            "firstDay": "M",
            "lastDay": 31
        },
        2: {
            "firstDay": "TH",
            "lastDay": 29
        },
        3: {
            "firstDay": "F",
            "lastDay": 31
        },
        4: {
            "firstDay": "M",
            "lastDay": 30
        },
        5: {
            "firstDay": "W",
            "lastDay": 31
        },
        6: {
            "firstDay": "Sat",
            "lastDay": 30
        },
        7: {
            "firstDay": "M",
            "lastDay": 31
        },
        8: {
            "firstDay": "TH",
            "lastDay": 31
        }, 
        9: {
            "firstDay": "Sun",
            "lastDay": 30
        },
        10: {
            "firstDay": "T",
            "lastDay": 31
        },
        11: {
            "firstDay": "F",
            "lastDay": 30
        },
        12: {
            "firstDay": "Sun",
            "lastDay": 31
        },
    }

    daytodate = {
        'Sun': 'Sunday',
        'M': 'Monday',
        'T': 'Tuesday',
        'W': 'Wednesday',
        'TH': 'Thursday',
        'F': 'Friday',
        'Sat': 'Saturday'
    }
    oneMonth = ["Sun", "M", "T", "W", "TH", "F", "Sat"] * 6
    # print(oneMonth)
    firstDayOfMonth = monthList.get(int(month)).get("firstDay")
    firstDateOfMonth = oneMonth.index(firstDayOfMonth)

    # print(f"START WITH {firstDateOfMonth}")
    # print(f"START WITH {oneMonth[firstDateOfMonth]}")
    count = 0
    month_use = monthList.get(int(month))
    result = {}
    for i in range(1, month_use.get('lastDay') + 1):
        index = firstDateOfMonth + count

        # print(f"Day {i}: {oneMonth[index]}")
        result[i] = oneMonth[index]

        count += 1

    # print(result)
    result_real = result.get(int(day))
    if result_real == None:
        print("error")
    else:
        print(daytodate.get(result_real))
