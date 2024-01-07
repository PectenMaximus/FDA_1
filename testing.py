#Collatz
#def collatz(num):
    #while(num!=1): 
       #if(num%2==0):
          #num=num//2
          #print(num)
       #else:
          #num=3*num+1
          #print(num)

   
#numx= int(1000)
#collatz(numx)

import numpy as np
import matplotlib.pyplot as plt 

def event(n,prob_ty,size):    
    Outcome = np.random.binomial(n,prob_ty,size)    
    return Outcome

Trials = 20
prob_ty = 0.5
Outcome = np.random.binomial(Trials,prob_ty)
print(Outcome)

Prob_expt=[np.equal(Outcome,i).mean() for i in range(Trials)]

plt.plot(Prob_expt,'r--')
plt.xlabel('Heads Returned')
plt.ylabel('Probability of Occurrence',)
plt.show()
