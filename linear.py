import math
def hypo(q0,q1,x):
    return (q0+(q1*x))
def cost(q0,q1,x,y,m):
    j=0
    for i in range(m):
        if(i==0):
            continue
        h=hypo(q0,q1,x[i])
        j=j+math.pow((h-y[i]),2)
    return (j/m)
def derivative(q0,q1,x,y,m,flag):
    j=0
    if(flag==0):
        for i in range(m):
            if(i==0):
                continue
            j=j+(q0+q1*x[i]-y[i])
        j=(j*2)/m
    if(flag==1):
        for i in range(m):
            if(i==0):
                continue
            j=j+(q0+q1*x[i]-y[i])*x[i]
        j=(j*2)/m
    #print(j)
    return j
def grad(q0,q1,x,y,m,size):
    a0=a1=0
    p=100
    while True:
        a0=q0-0.0000003*derivative(q0,q1,x,y,m,0)
        a1=q1-0.0000003*derivative(q0,q1,x,y,m,1)
        q0=a0
        q1=a1
        #print(q0,q1);
        if(abs((derivative(q0,q1,x,y,m,0))-p)<0.0001):
            break
        p=abs(derivative(q0,q1,x,y,m,0))      
    price=hypo(q0,q1,size)
    return price
size=int(input('enter the size of the house'))
x=[100,200,300,400,500,600,700]
y=[100000,200000,300000,400000,500000,600000,700000]
price=grad(0,0,x,y,7,size)
print('\n\n\n\n\n\n%0.2f'% (price+0.5))


    
        
        
        
            
            
        
        
