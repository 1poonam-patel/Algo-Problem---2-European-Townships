f = open("ET_large.txt","r")
t = int(f.readline())

ans=[]

for i in range(t) :
    n = int(f.readline())
    
    totalTime = 0
    totalAccent = 0
    totalNormal = 0
    
    for _ in range(n) :
        data = f.readline()
        if(data[-1] == "\n") :
            data = data[:-1:]
        data = data.split(",")
        data = [int(temp) for temp in data]
        
        totalBedroom = data[0]
        roofBedrooms = data[1]
        standerdRoom = data[2]
        victorialHall = data[3]

        totalWalls = (standerdRoom)*4 + roofBedrooms*3 + victorialHall*6

        accentWallsQty = totalWalls*(1/3)*1.5
        normalWallQty = totalWalls*(2/3)*2.25

        accentWallsTime = totalWalls*(1/3)*2.5
        normalWallTime = totalWalls*(2/3)*3.25

        totalTime += (accentWallsTime+normalWallTime)
        totalAccent += accentWallsQty
        totalNormal += normalWallQty

        totalTime = round(totalTime,2)
        totalAccent = round(totalAccent,2)
        totalNormal = round(totalNormal,2)
        
    ans.append([totalTime,totalAccent,totalNormal])
#ans is inside ans variable
f.close()
f2 = open("problem-2_output_large","w")

for a in ans :
    for i in a:
        f2.write(str(i))
        f2.write(" ")
    f2.write("\n")

f2.close()