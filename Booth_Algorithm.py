#BoothAlgorithm
#initialising global variables
global Acc
global helper
global multiplicand
global multiplier
#function for addition
def Addition(str1,str2,N):
    #filling rest of the string with zeroes 
    str1=str1.zfill(N)
    str2=str2.zfill(N)
    #variable to store final result
    result=""
    #variable to store carry
    carry=0
    #iteration for bitwise addition
    for i in range(N-1,-1,-1):
        r=carry
        if str1[i]=="0":
            r+= 0
        else:
            r+=1
        if str2[i]=="0":
            r+=0
        else:
            r+=1
        if r%2==0:
            result="0"+result
        else:
            result= "1"+result
        if r>=2:
            carry=1
        else:
            carry=0
    #filling rest of the resultant string with zeroes
    a= result.zfill(N)
    return a
         
#function to find Two's complement
def TwoComplement(Str1,N):
    #handling negative numbers
    if (Str1[0]=="0"):
        Str1=Str1.zfill(N)
    elif(Str1[0]=="1"):
        Str1=str.rjust(Str1,N,"1")
   
    B=""
    #for changing the bits from 1 to 0 and vice versa
    for i in range(0,N):
        if (Str1[i]=="0"):
            B+="1"
        elif (Str1[i]=="1"):
            B+="0"
    K="1"
    K=K.zfill(N)
    #Adiing 1 to one's complement
    Str3=Addition(B,K,N)
    return Str3
#function to shift the bits
def Rightshift(Str1):
    Str2=Str1[0]
    for i in range(len(Str1)):
        if i > 0:
           Str2+=Str1[i-1]

    return Str2
#function for executing Booth's Algorithm   
def BoothsAlgo(Str1,Str2,N):
    Accumulator=""
    Accumulator =Accumulator.zfill(N)
    multiplicand= Str1
    multiplicand1 = TwoComplement(Str1,N)
    helper="0"
    #initialising a register for operations
    Acc=Accumulator+Str2+helper
    left = Str2+helper
    for i in range(0,N):
        #Condition to call Arithmetic rightshift of acc register
        if (Acc[len(Acc)-2:]=="00" or Acc[len(Acc)-2:]=="11"):
            Acc=Rightshift(Acc)
            Accumulator = Acc[:N]
            left = Acc[N:]
        #Condition to add multiplier to accumulator    
        elif(Acc[len(Acc)-2:]=="01"):
            Accumulator = Addition(Accumulator,multiplicand,N)
            Acc = Accumulator + left
            Acc=Rightshift(Acc)
            Accumulator = Acc[:N]
            left = Acc[N:]
        #Condition to subtract multiplier from accumulator
        elif (Acc[len(Acc)-2:]=="10"):
            Accumulator = Addition(Accumulator,multiplicand1,N)
            Acc = Accumulator + left
            Acc=Rightshift(Acc)
            Accumulator = Acc[:N]
            left = Acc[N:]
    return Acc[:len(Acc)-1]
#function to evaluate result of Booth's Algorithm 
def value(Str1):
    if (Str1[0]=="0"):
        return int(Str1,2)
    if (Str1[0]=="1"):
        N=len(Str1)
        a=TwoComplement(Str1,N)
        return "-"+str(int(a,2))
        

#driver function or main function          
if __name__  =="__main__":
    input1= input()
    input2= input()
    bitsize1=len(input1)
    bitsize2=len(input2)
    #initialising size of accumulator to max of both inputs
    N=max(bitsize1,bitsize2)
    #conditions to handlle positive and negative numbers
    if input1[0] == '0':
        Input1 = input1
        while ( len(Input1) < N ):
            Input1 = '0' + Input1
    if input1[0] == '1':
        Input1 = input1
        while ( len(Input1) < N ):
            Input1 = '1' + Input1
    if input2[0] == '0':
        Input2 = input2
        while ( len(Input2) < N ):
            Input2 = '0' + Input2
    if input2[0] == '1':
        Input2 = input2
        while ( len(Input2) < N ):
            Input2 = '1' + Input2
    #final function to call Booth,s algorithm
    print(BoothsAlgo(Input1,Input2,N))
    print (value(BoothsAlgo(Input1,Input2,N)))
