import collections.abc

f = open("mat_dv.txt", "r")

lines = f.read().split("\n")
best = {}
for line in lines:
    i = lines.index(line)
    splited = line.split(" ")
    second_name = splited[0]
    first_name = splited[1]
    grade = splited[2]
    algebra = int(splited[3])
    geometry = int(splited[4])
    if (grade not in best):
        best[grade] = [
            {"row":i, "points":algebra},
            {"row":i, "points":geometry}
        ]
    elif (best[grade][0]["points"] < algebra): best[grade][0] = {"row":i, "points":algebra}
    elif (best[grade][0]["points"] == algebra): best[grade][0] = {"row":[best[grade][0]["row"],i], "points":algebra}
    elif (best[grade][1]["points"] < geometry): best[grade][1] = {"row":i, "points":geometry}
    elif (best[grade][1]["points"] == geometry): best[grade][1] = {"row":[best[grade][1]["row"],i], "points":geometry}

    if ("алгебра" not in best): best["алгебра"] = {"row":i, "points":algebra}
    elif (best["алгебра"]["points"] < algebra): best["алгебра"] = {"row":i, "points":algebra}
    elif (best["алгебра"]["points"] == algebra): best["алгебра"] = {"row":[best["algebra"]["row"], i], "points":algebra}

    if ("геометрия" not in best): best["геометрия"] = {"row":i, "points":geometry}
    elif (best["геометрия"]["points"] < geometry): best["геометрия"] = {"row":i, "points":geometry}
    elif (best["геометрия"]["points"] == geometry): best["геометрия"] = {"row":[best["geometry"]["row"], i], "points":geometry}
for key, el in best.items():
    print(key+":")
    if (isinstance(el, collections.abc.Sequence)):
        if (isinstance(el[0]["row"], collections.abc.Sequence)):
            for row in el[0]["row"]:
                line = lines[row].split(" ")
                print(" ", "алгебра:", line[0], line[1], line[3])
        else:
            line = lines[el[0]["row"]].split(" ")
            print(" ", "алгебра:", line[0], line[1], line[3])

        if (isinstance(el[1]["row"], collections.abc.Sequence)):
            for row in el[1]["row"]:
                line = lines[row].split(" ")
                print(" ", "геометрия:", line[0], line[1], line[3])
        else:
            line = lines[el[1]["row"]].split(" ")
            print(" ", "геометрия:", line[0], line[1], line[3])

    else:
        line = lines[el["row"]].split(" ")
        print(" ", line[0], line[1], line[2], el["points"])

f.close()