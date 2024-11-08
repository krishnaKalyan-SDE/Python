mantra="Hare Krishna Hare Krishna Krishna Krishna Hare Hare "
# pos=mantra.find("Hare")
# new_pos=mantra.find("Hare",pos+1)
# print(new_pos)

#find the cout of 'Hare' in above mantra
count=0
for i in range(len(mantra)):
    if(mantra[i]=='a'):
        count+=1

print(count)
