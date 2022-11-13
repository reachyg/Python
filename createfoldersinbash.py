with open("C:\\Arena\\createfolders.txt", mode = "w") as f:
    day = "Repo05"
    exercises = "21"
    for i in range(1, 22):
        if i < 10:
            txt = "cd /c/Arena/" + day + "\n" + "mkdir " + "ex0" + str(i) + '\n' + "cd /c/Arena/" + day + "/ex0" + str(i) + "\n" + "mkdir " + "src" + '\n'
        else:
            txt = "cd /c/Arena/" + day + "\n" + "mkdir " + "ex" + str(i) + '\n' + "cd /c/Arena/" + day + "/ex" + str(i) + "\n" + "mkdir " + "src" + '\n'
        f.write(txt)
