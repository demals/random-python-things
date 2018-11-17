frq = []
done = []
while True:
    mark = int(input("Input a number: "))
    if mark == 0:
        break
    else:
        frq.append(mark)
co1 = ("[Number]")
print(co1.rjust(4),end=" ")
co2 = ("[Frequency]")
print(co2.rjust(4))
for i in frq: 
    if frq.count(i) == 0:
        continue
    if i in done:
        continue
    else:
        co3 = str(i)
        co4 = str(frq.count(i))
        print(co3.center(len(co1)),end="")
        print(co4.center(len(co2)))
        done.append(i)
        
        
