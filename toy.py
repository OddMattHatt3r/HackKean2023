from quantum import senderProg,receiverProg,makeKey
userinput = input("What is your 8 character message?: ")

l,m=[],[]
sendermessage = []
for i in userinput:
    l.append(ord(i))
#print(l)
for i in l:
    m.append(int((str(bin(i)))[2:]))
#print(m)

for bin in m:
    sendermessage.append("0")
    for num in str(bin):
        sendermessage.append(num)

#print(userinput)

n = len(sendermessage)
#print(n)

try:
    x,senderBasess,sendermessages = senderProg(sendermessage,n)
    #print(type(x[0]))

    #print("\nENCODED: ", x)
    print("\nSender Bases: ", senderBasess)
    print("\nSender Message: ", sendermessages)
    receiverResults,receiverBases = receiverProg(x,n)
    print("\nReciever Bases: ", receiverBases)
    print("\nReciever Results: ", receiverResults)

    key = makeKey(senderBasess,receiverResults,receiverBases,sendermessages,sendermessages,n)


    print("\nFINAL KEY: " ,str(key))
except IndexError:
    x,senderBasess,sendermessages = senderProg(sendermessage,n)
    print(type(x[0]))

    print("\nENCODED: ", x)
    print("\nSender Bases: ", senderBasess)
    print("\nSender Message: ", sendermessages)
    receiverResults,receiverBases = receiverProg(x,n)
    print("\nReciever Bases: ", receiverBases)
    print("\nReciever Results: ", receiverResults)

    key = makeKey(senderBasess,receiverResults,receiverBases,sendermessages,sendermessages,n)


    print("\nFINAL KEY: " ,str(key))