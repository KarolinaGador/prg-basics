winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

total = 0
for val in winter_semester.values():
    total = total + int(val)

print(total)    