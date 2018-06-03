n=int(input('Enter the number of list: '))
students={}
for i in range (n):
    (name, date, attendance)=list(map(str.strip,input().replace("-",":").split(':')))
    name = name.split()[0]
    if name not in students:
        students[name]={date:attendance}
    else:
        students[name].update({date:attendance})
a=input('Enter a student: ')
if a in students:
    for date, attendance in students[a].items():
        print ("%s - %s"%(date, attendance))
