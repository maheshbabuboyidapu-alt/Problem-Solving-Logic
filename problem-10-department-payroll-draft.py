emp = [
    {"name": "Ravi",  "department": "Engineering", "hours": 45, "rate": 200},
    {"name": "Sita",  "department": "Sales",       "hours": 38, "rate": 250},
    {"name": "Arjun", "department": "Engineering", "hours": 50, "rate": 180},
    {"name": "Divya", "department": "Sales",       "hours": 40, "rate": 220},
]
mic = []
st = 40
seen = set()


for e in emp:
    dip = e["department"]

    if dip not in seen:
        seen.add(dip)
        mic.append(dip)


def cs(hours, rate):
    if hours > st:
        ot = hours - st
        otp = ot * (rate * 1.5)
        sal = (st * rate) + otp
    else:
        sal = hours * rate

    return sal


for m in mic:
    td = 0
    hp = 0
    hpn = ""
    lp = None
    lpn = ""

    print(f"Department: {m}")

    for e in emp:
        if m == e["department"]:

            h = e["hours"]
            r = e["rate"]

            s = cs(h, r)

            print(f"   - {e['name']}: ${s}")

            td += s

            if hp < s:
                hp = s
                hpn = e["name"]

            if lp is None or lp > s:
                lp = s
                lpn = e["name"]

    print(f"Total of {m} department is: ${td}")
    print(f"Highest paid person in the {m} department is {hpn} (${hp})")
    print(f"Lowest paid person in the {m} department is {lpn} (${lp})")
    print()
