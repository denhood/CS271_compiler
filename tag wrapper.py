import string
f = open("Main.jack",'r')
tagLst = list()
outputLst = list()
tempstr = str()
keywordlst = 'class constructor function method field static var int char boolean void true false null this let do if else while return'.split(' ')
symbollst = '{ } ( ) [ ] . , ; + - * / & | < > = ~'.split(' ')
charnums = string.ascii_letters + string.digits +"\""
for line in f: #go through file line by line
    line = line.strip() #remove all whitespace from line
    if(line): #if line is not empty
        for position in range(len(line)): #go through line char by char
            if(line[position] in charnums): #if it is a letter, concatenate
                tempstr += line[position] 
            else:
                if(tempstr): #tempstr is not empty
                    try:
                        tempstr = int(tempstr)
                    except:
                        pass
                    outputLst.append(tempstr)
                if(line[position] != ' '):#current char not a space
                    outputLst.append(line[position])
                tempstr = "" #reset tempstr
for item in outputLst:
    if(item in keywordlst):
        tagLst.append("<keyword>"+item+"</keyword")
    elif(item in symbollst):
        tagLst.append("<symbol>"+item+"</symbol>")
    elif(isinstance(item, int)):
        tagLst.append("<integerConstant>"+str(item)+"</integerConstant>")
    elif(item[0] == "\"" and item[len(item)-1] == "\""):
        tagLst.append("<stringConstant>"+item+"</stringConstant>")
    else:
        tagLst.append("<identifier>"+item+"</identifier>")
