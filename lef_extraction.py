# getting cellNames
cellNameFile=open('cellName.txt')
cellNames=cellNameFile.read().strip().split('\\')[:-1]
print(cellNames)
count=0
for cellname in cellNames:
    lastInd=int(cellname.index("_"))+3
    cellname=cellname[:lastInd]
    cellNames[count]=cellname
    count+=1
print(cellNames)



#read lef files
lefFile=open('lef.txt')
lefStringLines=lefFile.readlines()
lefCells=[]
for eachLine in lefStringLines:
    if "MACRO" in eachLine:
        cellNme=eachLine.split()[1]
        lefCells.append(cellNme)
        # print(cellNme)
# print(lefCells)
        


x=[]

newCell=open("newList.txt","w")
for lefcell in lefCells:
    for eachCell in cellNames:
        # print(lefcell,eachCell)
        if eachCell.lower().strip() in lefcell.lower().strip():
            print(lefcell)
            x.append(lefcell)
cellString="\n".join(x)
# print(string)
# newCell.write(cellString)

# print("SDFFQ_X1" in "A2SDFFQ_X1M_A9TH_W3")
# print("XOR3_X4" in "XOR3_X4M_A9TH_W3")
# print(x)