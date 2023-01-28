import matplotlib.pyplot as plt
import sys
import numpy as np
epsilon=sys.float_info.epsilon
import math
epsilon=sys.float_info.epsilon
#QUESTION1
def f(n):
    res = n * (((n + 1) / n) - 1) - 1;
    return res;

def g(n):
    d = sys.float_info.epsilon;
    rev = f(n) / d;
    return rev;
#print(g(1000)); # -2.220446049250313e-16
xvals = np.linspace(1,1000,1000) #100 points from 0 to 6 in ndarray
yvals = list(map(g, xvals))
plt.plot(xvals, yvals);
plt.xlabel('n')
# naming the y-axis
plt.ylabel('g(n)')

plt.show();
plt.savefig('q1.png')



nums=[];

for i in range(1, 1000001):
    nums.append(1+(10**6+1-i)*(10**-8))

#NAIVE SUM
def naivesum(nums):
    sum1=(0.0);
    for i in range(0, (len(nums))):
        sum1 = (sum1+(nums[i]));
    sum2=(sum1);


    return sum2;
print(naivesum(nums));
#COMPENSATEDSUM
def  dKahansum(nums):
    summ = 0.0;
    c = 0.0;

    for i in range(0, (len(nums))):
        y = nums[i] - c;
        t = summ + y;
        c = (t - summ) - y;

        summ = (t);


    return summ;
print(dKahansum(nums))
#PAIRWISESUM
def pairwise(nums):
    if len(nums) <= 1:
        s = 0;
        for i in range(0, len(nums)):
            s = s + nums[i];

    else:

        m = math.floor((len(nums)) / 2);

        #for j in range(0,len(nums)):
        s = pairwise(nums[0:m])+pairwise(nums[(m): len(nums)]);



    return (s);

print(pairwise(nums));
