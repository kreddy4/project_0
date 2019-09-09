x=str(input('first binary no:'))
y=str(input('second binary no:'))

countx=len(x)
county=len(y)

def half_adder(a,b):
    carry=a and b
    sum=a ^ b
    return sum,carry

def full_adder(cin,a,b):
    sum1,carry1=half_adder(a,b)
    sum2,carry2=half_adder(sum1,cin)
    cout=carry1 or carry2
    return sum2,cout

p='u'
if (countx>3 or county>3):
    print("input has more than three bits")
else:
    if(x[countx-1]=='u' or y[county-1]=='u'):
        first_bit,carry1=p,0
    else:
        first_bit,carry1=half_adder(int(x[countx-1]),int(y[county-1])%10)
    if(x[countx-2]=='u' or y[county-2]=='u'):
        second_bit,carry2=p,0
    else:
        second_bit,carry2=full_adder(carry1,int(int(x[countx-2])),int(int(y[county-2])))
    if(x[countx-3]=='u' or y[county-3]=='u'):
        third_bit,carry=p,0
    else:
        third_bit,carry=full_adder(carry2,int(int(x[countx-3])),int(int(y[county-3])))
    print(carry,third_bit,second_bit,first_bit)
