PlainText = "instruments"

PlanTextPairs = []

#print(PlainText)
#print(len(PlainText) % 2)

if (len(PlainText) % 2 == 1):
    PlainText = PlainText + "z"


print(PlainText)

for i in range(0,len(PlainText), 2):
    #print(PlainText[i], PlainText[i+1])
    PlanTextPairs.append(PlainText[i] + PlainText[i+1])

print(PlanTextPairs)
