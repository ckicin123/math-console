import io
import random
import time
print(" ________________________________________")
print("/                                        \\")
print("|enter \"showFunctions()\" to see functions|")
print("\\________________________________________/")
def showFunctions():
    functions=[
        "matrix.display():\n displays a matrix giving it's multiplier",
        "matrix.displayTrue():\n displays a matrix with it's contents multiplied by it's multiplier",
        "matrixAdd(matrixA,matrixB):\n adds matrixA and matrixB",
        "matrixSub(matrixA,matrixB):\n subtracts matrixB from matrixA",
        "matrixMulti(matrixA,matrixB):\n multiplies matrixB by matrixA",
        "realMatrixMulti(real number,matrix):\n multiplies the real number and the matrix",
        "det(matrix):\n find the determinant of a matrix",
        "getMinor(matrix,(x coordinate,y coordinate)):\n gets the miner of the point in the matrix at the given coordinates",
        "inverse(matrix):\n finds the inverse of a matrix",
        "factorial(num):\n gets the factorial",
        "doubleFactorial(num):\n gets the factorial but only includes factors with the same polarity as the given num",
        "choose(n,r):\n returns n choose r with the given inputs",
        "binomialExpansion(a,b,power):\n returns the binomial expansion in the form (a+b)^power with the given inputs",
        "listSum(list):\n given a list it will return the sum of all the elements in the list",
        "sumInputs():\n sums inputs given until 0 is given as the input and then returns the sum",
        "listMean(list):\n given a list it will return the mean of all the elements in the list",
        "meanInputs():\n returns the mean of all inputs when 0 is entered",
        "getFactors(num):\n returns all the factors of the given number",
        "massCalc():\n enables you to predefine a sequence of operations and then input terms for that sequence of operatoins in a quicker fashion than what a calculator could offer",
        "solveQuadratic(a,b,c):\n solves a quadratic equation when the it's in the form ax^2+bx+c=0",
        "lowestCommonMultiple([a,b,c,d...]):\n given a list of any length it will return the lowest common multiple and what each number needed to be multiplied by to reach that number",
        "highestCommonFactor([a,b,c,d...]):\n given a list of any length it returns the highest common multiple",
        "deVries(polinomial): gives all the De Vries eqautions for the entered polinomial",
        "deVriesCalc([alpha,beta..]) gives all De Vries equations with values given all the ",
        "differentiate(equation,point) gets the gradient at a given point given an equation",
        "note():\n enables note taking which is encrypted for some reason",
        "isInt(num):\n returns True if num is an integer, returns False if a isn't",
        "isFloat(num):\n returns True if num is a real float, returns False if not",
        "stringifyList(list):\n returns a string encoded version of the inputted list",
        "destringifyList(string):\n returns the list version of the encoded input",
        "enrypt(string):\n returns encrypted format",
        "decrpy(string):\n returns decrpyted format",
        "mergeSort(list)\n returns sorted list (don't use this, python has a sorted() function, i got bored ok?",
        "clr():\n clear:s screen"
               ]
    print("functions:\n\n\n",end="")
    for i in functions:
        print(i,end="\n\n")
def timeMeasure():
    while True:
        curTime=time.monotonic()
        yield "started timer"
        print("time taken to calculate: "+str(time.monotonic()-curTime))
        yield "time ended"
timer=timeMeasure()
def clr():
    for i in range(30):
        print("\n")
def isInt(a):
    a=str(a)
    if len(a)==0:
        return False
    if a[0]=="-":
        a=a[1:len(a)]
    if a.isnumeric():
        return True
    return False
def isFloat(a):
    a=str(a)
    if len(a)==0:
        return False
    if a[0]=="-":
        a=a[1:len(a)]
    totalNumeracy=False
    if "." in a:
        sides=a.split(".")
        totalNumeracy=True
        for i in sides:
            if i.isnumeric()==False:
                totalNumeracy=False
                break
    else:
        totalNumeracy=a.isnumeric()
    return totalNumeracy
def yorn():
    ans=""
    while ans!="y" and ans!="n":
        ans=input("y/n: ")
    if ans=="y":
        return True
    else:
        return False
def largest(a,b):
    return (abs(a-b)+a+b)/2
def smallest(a,b):
    return -(abs(a-b)-a-b)/2
def factorial(x):
    if isInt(x)==False:
        return "invalid input"
    ans=1
    for i in range(1,x+1):
        ans*=i
    return ans
def choose(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))
def binomialExpansion(a,b,power):
    terms=[]
    stringForm=""
    for i in range(power+1):
        curTerm=choose(power,i)*(b**i)*(a**(power-i))
        terms.append(curTerm)
        stringForm+=" "
        if curTerm>=0:
            stringForm+="+"
        stringForm+=" "+str(curTerm)
    print(stringForm)
    return terms
def listSum(a):
    sum=0
    for i in a:
        sum+=i
    return sum
def sumInputs():
    sum=0
    while True:
        ans=input(": ")
        if isFloat(ans):
            num=float(ans)
            if num==0:
                break
            sum+=num
            print(sum)
        else:
            print("enter a number damn it")
    print("sum:")
    return sum
def getFactors(a):
    factors=[]
    if isInt(str(a)):
        for i in range(1,a//2):
            if a/i==a//i:
                factors.append(a//i)
        return factors
    else:
        return "not an interger"
def listMean(a):
    return listSum(a)/len(a)
def meanInputs():
    sum=0
    length=0
    while True:
        ans=input(": ")
        if isFloat(ans):
            num=float(ans)
            if num==0:
                break
            length+=1
            sum+=num
            print(sum/length)
        else:
            print("enter a number damn it")
    print("mean:")
    return sum/length
def massCalc():
    allowedOps=["+","-","/","*","**"]
    operations=[]
    print("enter \"end\" to finish setting operators")
    while True:
        ans=input("enter operation (+, -, /, *, **)\n: ")
        if ans in allowedOps:
            operations.append(ans)
        else:
            if ans=="end":
                break
            print("not an allowed operation")
    while True:
        stringExpression=""
        ans=""
        while isFloat(ans)==False:
            ans=input("enter num: ")
        output=float(ans)
        stringExpression+=ans
        for i in operations:
            ans=""
            while isFloat(ans)==False:
                ans=input("enter num: ")
            num=float(ans)
            if i=="+":
                output+=num
            elif i=="-":
                output-=num
            elif i=="/":
                output/=num
            elif i=="*":
                output*=num
            elif i=="**":
                output**=num
            stringExpression+=i+ans
            print(stringExpression)
            print("="+str(output)+"\n")
        print("end here?")
        if yorn():
            break
def solveQuadratic(a,b,c):
    if isFloat(a) and isFloat(b) and isFloat(c):
        descriminant=(b**2)-(4*a*c)
        print("descriminant = "+str(descriminant))
        for i in range(1,-2,-2):
            print((-b+(i*(descriminant)**(1/2)))/(2*a))
    else:
        return "an input was not a number"
def lowestCommonMultiple(a):
    multiList=[]
    newVals=[]
    for i in a:
        if isFloat(i)==False:
            return "invalid input"
        multiList.append(1)
        newVals.append(i)
    while sorted(newVals)[0]!=sorted(newVals)[-1]:
        index=newVals.index(sorted(newVals)[0])
        multiList[index]+=1
        newVals[index]=a[index]*multiList[index]
    print("list of multipliers to achieve lowest common factor")
    print(multiList)
    print("lowest common factor: "+str(newVals[0]))
def highestCommonFactor(a):
    for i in a:
        if isFloat(i)==False:
            return "invalid input"
    lowestVal=sorted(a)[0]
    for i in range(lowestVal,0,-1):
        valid=True
        for j in a:
            if j//i!=j/i:
                valid=False
                break
        if valid:
            return i
def doubleFactorial(a):
    if isInt(a)==False:
        return "invalid input"
    ans=1
    for i in range(a,0,-2):
        ans*=i
    return ans
def deVries(polinomial):
    next(timer)
    sign="-"
    roots=[]
    for i in range(polinomial):
        roots.append(chr(945+i))
    for count in range(1,polinomial+1): #num of roots = polinomial
        equation=""
        holder=[]
        for num in range(count):
            holder.append(num)
        temp=[]
        term=""
        for termIndex in holder:
            term+=roots[termIndex]
        equation+=" + "+term
        for j in range(int(choose(polinomial,count))-1):
            for pos in range(len(holder)-1,-1,-1):
                if holder[pos]!=polinomial-(len(holder)-pos):
                    holder[pos]+=1
                    break
                elif holder[pos-1]!=polinomial-(len(holder)-(pos-1)):
                    holder[pos-1]+=1
                    for numPos in range(pos-1,len(holder)):
                        holder[numPos]=holder[pos-1]+numPos-(pos-1)
                    break
                if pos==0 and False:
                    holder[0]+=1
                    for numPos in range(1,len(holder)):
                        holder[numPos]=holder[0]+numPos
                    break
            term=""
            for termIndex in holder:
                term+=roots[termIndex]
            equation+=" + "+term
        print(sign+chr(97+count)+"/a = "+equation+"\n")
        if sign=="-":
            sign="+"
        else:
            sign="-"
    next(timer)
def deVriesCalc(roots):
    next(timer)
    polinomial=len(roots)
    sign="-"
    for count in range(1,polinomial+1): #num of roots = polinomial
        equation=0
        holder=[]
        for num in range(count):
            holder.append(num)
        temp=[]
        term=1
        for termIndex in holder:
            term*=roots[termIndex]
        equation+=term
        for j in range(int(choose(polinomial,count))-1):
            for pos in range(len(holder)-1,-1,-1):
                if holder[pos]!=polinomial-(len(holder)-pos):
                    holder[pos]+=1
                    break
                elif holder[pos-1]!=polinomial-(len(holder)-(pos-1)):
                    holder[pos-1]+=1
                    for numPos in range(pos-1,len(holder)):
                        holder[numPos]=holder[pos-1]+numPos-(pos-1)
                    break
                if pos==0 and False:
                    holder[0]+=1
                    for numPos in range(1,len(holder)):
                        holder[numPos]=holder[0]+numPos
                    break
            term=1
            for termIndex in holder:
                term*=roots[termIndex]
            equation+=term
        print(sign+chr(97+count)+"/a = "+str(equation)+"\n")
        if sign=="-":
            sign="+"
        else:
            sign="-"
    next(timer)
def differentiate(equation, point):
    terms=[]
    term=[]
    part=""
    i=0
    skip=True
    while i<len(equation):
        char=equation[i]
        if char=="x":
            if part=="" or part=="-" or part=="+":
                part+="1"
            term.append(part)
            part=""
            if i+1==len(equation):
                part="1"
                term.append(part)
                terms.append(term)
                break
            elif equation[i+1]=="^":
                first=True
                highest=len(equation)-1
                part=""
                for j in range(i+2,len(equation)):
                    if equation[j]=="-" or equation[j]=="+" and first==False:
                        highest=j
                        break
                    part+=equation[j]
                    first=False
                i=highest
                term.append(part)
                part=""
            else:
                term.append(1)
                i+=1
            terms.append(term)
            term=[]
            part=""
            skip=True
        char=equation[i]
        part+=char
        i+=1
        if char=="+" or char=="-" and skip==False:
            part=""
        skip=False
    ans=0
    dervStr=""
    print(terms)
    for term in terms:
        coef=int(term[0])*int(term[1])
        pow=int(term[1])-1
        ans+=(coef*(point**pow))
        dervStr+=str(coef)+"x^"+str(pow)+"+"
    print(dervStr)
    return ans
minorTable=[
    [
    [["0,0"]],
        ],
    [
    [["1,1"],["0,1"]],
    [["1,0"],["0,0"]]
        ],
    [
    [["1,1","2,1","1,2","2,2"],["0,1","2,1","0,2","2,2"],["0,1","1,1","0,2","1,2"]],
    [["1,0","2,0","1,2","2,2"],["0,0","2,0","0,2","2,2"],["0,0","1,0","0,2","1,2"]],
    [["1,0","2,0","1,1","2,1"],["0,0","2,0","0,1","2,1"],["0,0","1,0","0,1","1,1"]]
        ]]
class matrix():
    def __init__(self,matrix):
        self.matrix=matrix
        self.y=len(matrix)
        self.x=len(matrix[0])
        self.multiplier=1
    def display(self):
        print(str(self.multiplier)+" times")
        for i in self.matrix:
            print(i)
    def displayTrue(self):
        temp=matrix(a.copy())
        for x in range(temp.x):
            for y in range(temp.y):
                temp.matrix[y][x]*=self.multiplier
        for i in temp.matrix:
            print(i)
    def copy(self):
        copy=[]
        templine=[]
        for i in self.matrix:
            for j in i:
                templine.append(j)
            copy.append(templine)
            templine=[]
        return copy
    def set0(self,x,y):
        line=[]
        new=[]
        self.x=x
        self.y=y
        for i in range(y):
            for j in range(x):
                line.append(0)
            new.append(line)
            line=[]
        self.matrix=new
    def setVal(self,val,x,y):
        line=[]
        new=[]
        self.x=x
        self.y=y
        for i in range(y):
            for j in range(x):
                line.append(val)
            new.append(line)
            line=[]
        self.matrix=new
def getMinor(a,coords):
    if type(a)!=type(matrix([[0]])):
        print("not a matrix")
        return
    if a.x!=a.y:
        print("collums and rows are not equal")
        return
    global minorTable
    print("getting minor of: "+str(a.matrix[coords[1]][coords[0]]))
    a.display()
    minor=matrix(a.copy())
    minor.set0(a.x-1,a.x-1)
    minorCoords=minorTable[a.x-1]
    xCounter=0
    yCounter=0
    for i in minorCoords[coords[1]][coords[0]]:
        currentCoords=i.split(",")
        minor.matrix[yCounter][xCounter]=a.matrix[int(currentCoords[1])][int(currentCoords[0])]
        xCounter+=1
        if xCounter>minor.x-1:
            xCounter=0
            yCounter+=1
    print("\n\n")
    minor.display()
    return minor
def matrixAdd(a,b):
    if a.x!=b.x or a.y!=b.y:
        print("invalid, size is not the same")
        return
    print("adding matricies\n")
    a.display()
    print("\nand\n")
    b.display()
    new=matrix(a.copy())
    for y in range(new.y):
        for x in range(new.x):
            new.matrix[y][x]+=b.matrix[y][x]
    print("\n\n")
    new.display()
    return new

def matrixSub(a,b):
    if a.x!=b.x or a.y!=b.y:
        print("invalid, size is not the same")
        return
    print("adding matricies\n")
    a.display()
    print("\nand\n")
    b.display()
    new=matrix(a.copy())
    for y in range(new.y):
        for x in range(new.x):
            new.matrix[y][x]-=b.matrix[y][x]
    print("\n\n")
    new.display()
    return new

def matrixMulti(a,b):
    if a.x!=b.y:
        print("invalid, collums of a not equal to rows of b")
        return
    print("multiplying matricies\n")
    a.display()
    print("\nand\n")
    b.display()
    new=matrix(a.copy())
    new.set0(b.x,a.y)
    for ay in range(new.y):
        for bx in range(b.x):
            sum=0
            for ny in range(new.y):
                sum+=(a.matrix[ay][ny]*b.matrix[ny][bx])
            new.matrix[ay][bx]=sum
    print("\n\n")
    new.display()
    return new
def realMatrixMulti(a,b):
    if type(a)!=type(1) and type(a)!=type(1.5):
        print("first given input was not a number")
        return
    if type(b)!=type(matrix([[1],[1]])):
        print("second given input was not a matrix")
        return
    print("multiplying real and matrix\n")
    print(a)
    print("\nand\n")
    b.display()
    new=matrix(b.copy())
    for y in range(new.y):
        for x in range(new.x):
            new.matrix[y][x]*=a
    print("\n\n")
    new.display()
    return new
def det(a):
    determinant="not supported"
    abcd=[]
    if type(a)!=type(matrix([[0]])):
        print("not a matrix")
        return
    if a.x!=a.y:
        print("not an even matrix")
        return
    if a.x==1:
        determinant=a.matrix[0][0]
    if a.x==2:
        for y in range(a.y):
            for x in range(a.x):
                abcd.append(a.matrix[y][x])
        determinant=(abcd[0]*abcd[3])-(abcd[2]*abcd[1])
        print("the determinant of")
        a.display()
        print("is: "+str(determinant))
    if a.x==3:
        coordsToMinor=[(0,0),(1,0),(2,0)]
        determinant=0
        sign=1
        for i in coordsToMinor:
            determinant+=(sign*a.matrix[i[1]][i[0]]*det(getMinor(a,i)))
            sign*=-1
        print("determinant: "+str(determinant))
    return determinant
def inverse(a):
    inverseMatrix=matrix(a.copy())
    inverseMatrix.set0(a.x,a.y)
    inverseMatrix.display()
    ix=inverseMatrix.x
    iy=inverseMatrix.y
    determinant=det(a)
    if determinant==0:
        return "not possiblea as determinant=0"
    for y in range(iy):
        for x in range(ix):
            inverseMatrix.matrix[y][x]=det(getMinor(a,(x,y)))
    inverseMatrix.display()
    print("applying cofactors")
    sign=1
    for y in range(iy):
        for x in range(ix):
            print(inverseMatrix.matrix[y][x])
            print(sign)
            inverseMatrix.matrix[y][x]*=sign
            sign*=-1
    inverseMatrix.display()
    temp1=0
    temp2=0
    print("flipping")
    for x in range(1,iy):
        temp1=inverseMatrix.matrix[x][0]
        temp2=inverseMatrix.matrix[0][x]
        inverseMatrix.matrix[x][0]=temp2
        inverseMatrix.matrix[0][x]=temp1
    for x in range(1,iy-1):
        temp1=inverseMatrix.matrix[iy-1][ix-1-x]
        temp2=inverseMatrix.matrix[ix-1-x][iy-1]
        inverseMatrix.matrix[iy-1][ix-1-x]=temp2
        inverseMatrix.matrix[ix-1-x][iy-1]=temp1
    inverseMatrix.display()
    print("multiplying by determinant")
    determinant=det(a)
    print("1/"+str(determinant)+" times by the matrix")
    inverseMatrix.display()
    inverseMatrix.multiplier=1/determinant
    print("is the inverse")
    return inverseMatrix
def stringifyList(a):
    string=""
    for i in a:
        if type(i)==type([]):
            string+=chr(1000)
            string+=stringifyList(i)
        else:
            string+=chr(1002)
            string+=str(i)
    string+=chr(1003)
    return string
def destringifyList(a):
    specialChars=[chr(1000),chr(1002),chr(1003)]
    list=[]
    temp=""
    writeToTemp=False
    i=0
    currentLevel=0
    while i<len(a):
        if writeToTemp:
            if a[i] in specialChars:
                writeToTemp=False
                list.append(temp)
                temp=""
            else:
                temp+=a[i]
        if a[i]==chr(1002):
            writeToTemp=True
        if a[i]==chr(1000):
            for j in range(i,len(a)):
                if a[j]==chr(1000):
                    currentLevel+=1
                elif a[j]==chr(1003):
                    currentLevel-=1
                if a[j]==chr(1003) and currentLevel==0:
                    list.append(destringifyList(a[i+1:j+1]))
                    i=j
                    break
        i+=1
    return list
def encrypt(a):
    encc=""
    for j in a:
        sum=0
        order=ord(j)
        for i in range(random.randint(2,4)):
            encc+="!"
            sect=random.randint(-order,order)
            sum+=sect
            encc+=str(sect)
        encc+="!"+str(order-sum)+"!"
    return encc
def decrypt(a):
    bus=[]
    boo=False
    cw=[]
    cs=""
    for i in a:
        if i=="!" and boo==False:
            boo=True
            if cs!="":
                cw.append(cs)
            cs=""
        elif i=="!":
            bus.append(cw)
            cw=[]
            boo=False
        else:
            cs+=i
            boo=False
    bus.append(cw)
    dec=""
    for i in range(len(bus)):
        sum=0
        for j in bus[i]:
            sum+=int(j)
        dec+=chr(sum)
    return dec
def note():
    
    def chooseCat(catagories):
        ans=""
        print("choose a catagory:")
        for i in catagories:
            print(i)
        while ans not in catagories:
            ans=input(": ")
        return ans
    
    catagories=[]
    with io.open("noteData.txt",mode="r",encoding="utf-8") as file:
        data=destringifyList(decrypt(file.read()))
    for i in data:
        catagories.append(i[0])
    ans=""
    while ans!="1" and ans!="2":
        ans=input("1:read\n2:write\n: ")
    # reading code
    if ans=="1":
        if len(catagories)==0:
            return "no catagories to read"
        print("which section would you like to read?")
        chosenCat=chooseCat(catagories)
        print("\nnotes in catagory: ")
        for i in range(len(data)):
            if data[i][0]==chosenCat:
                for j in range(1,len(data[i])):
                    print(data[i][j])
                break
    # writing code
    if ans=="2":
        ans=""
        while ans not in ["1","2","3","4"]:
            ans=input("1:create catagory\n2:add to a catagory\n3:remove from a catagory\n4:remove a catagory\n: ")
        #creating catagory
        if ans=="1":
            while True:
                ans=input("name your catagory\n: ")
                print("are you sure this is what you want the name to be?")
                if yorn():
                    break
            cat=[ans]
            data.append(cat)
        #adding to catagory
        if ans=="2":
            if len(catagories)==0:
                return "no catagory to add to"
            catChosen=chooseCat(catagories)
            ans=input("enter note you want to add\n: ")
            for i in range(len(data)):
                if data[i][0]==catChosen:
                    data[i].append(ans)
                    break
        #removing from catagory
        if ans=="3":
            if len(catagories)==0:
                return "no catagories to remove from"
            catChosen=chooseCat(catagories)
            for i in range(len(data)):
                if data[i][0]==catChosen:
                    catIndex=i
                    break
            for i in range(1,len(data[catIndex])):
                print(str(i)+": "+str(data[catIndex][i]))
            ans=""
            while True:
                ans=input("which note would you like to remove?")
                if isInt(ans):
                    ans=int(ans)
                    if ans>0 and ans<len(data[catIndex]):
                        break
            data[catIndex].pop(ans)
        #remove a catagory
        if ans=="4":
            if len(catagories)==0:
                return "no catagories to remove"
            catChosen=chooseCat(catagories)
            for i in range(len(data)):
                if data[i][0]==catChosen:
                    data.pop(i)
        with io.open("noteData.txt",mode="w",encoding="utf-8") as file:
            file.write(encrypt(stringifyList(data)))
def mergeSort(listToSort):
    l=[]
    l2=[]
    for i in listToSort:
        l2.append([i])
    """
    for i in range(0,length-1,2):
        if l[i]<l[i+1]:
            l2.append([l[i],l[i+1]])
        else:
            l2.append([l[i+1],l[i]])
    if length%2==1:
        l2.append([l[-1]])
    """
    tl=0 #target list
    finaltempl="rr"
    while len(finaltempl)>1:
        finaltempl=[]
        if tl==0:
            tarlist=l2
            l=[]
        else:
            tarlist=l
            l2=[]
        for i in range(0,len(tarlist)-1,2):
            ci1=0
            ci2=0
            focuspart1=tarlist[i]
            focuspart2=tarlist[i+1]
            templ=[]
            while ci1!=len(focuspart1) and ci2!=len(focuspart2):
                if focuspart1[ci1]<focuspart2[ci2]:
                    templ.append(focuspart1[ci1])
                    ci1+=1
                else:
                    templ.append(focuspart2[ci2])
                    ci2+=1
            if ci1==len(focuspart1):
                for i in range(ci2,len(focuspart2)):
                    templ.append(focuspart2[i])
            else:
                for i in range(ci1,len(focuspart1)):
                    templ.append(focuspart1[i])
            finaltempl.append(templ)
        if len(tarlist)%2==1:
            finaltempl.append(tarlist[-1])
        #print(finaltempl,end="\n\n")
        if tl==0:
            for i in finaltempl:
                l.append(i)
            tl=1
        else:
            for i in finaltempl:
                l2.append(i)
            tl=0
    if len(l)==1:
        return l[0]
    else:
        return l2[0]

# can predefine values and such here
a=matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
          ])
b=matrix([
    [1,1,1],
    [2,2,2],
    [3,3,3]
          ])
c=matrix([
    [1110],
    [370],
    [1113]
    ])
d=matrix([
    [1,2],
    [3,4]
    ])
