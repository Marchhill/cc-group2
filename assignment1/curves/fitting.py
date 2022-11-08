import scipy
import numpy as np
import matplotlib.pyplot as plt
import csv


workloads = [100,200,500]

xs = []
ys = []
for work in workloads:
    with open(f'data/20221107T200816/measurements/data-{work}MB.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            xs.extend(np.tile((work,float(row[0])),(len(row)-1,1)))
            ys.extend(list(map(float,row[1:])))

def time(workload, executors, constant, parallelisable):
    """Calculate the time taken for a given workload

    Args:
        workload: file size
        executors: no. of cores
        constant: just a fixed constant
        parallelisable: [0,1] proportion of code that is paralisable
    """
    return constant * (workload * (1-parallelisable) + workload * parallelisable / executors)

xs = np.array(xs)
ys = np.array(ys)
popt = scipy.optimize.curve_fit(lambda xdata,constant,parallelisable:time(xdata[:,0],xdata[:,1],constant, parallelisable), xs, ys)

print(popt)

work = np.linspace(0, 600, 100)
cores = np.linspace(1,10,50)

X, Y = np.meshgrid(work, cores)

timeVals = time(X,Y,*popt[0])

ax = plt.axes(projection='3d')
ax.plot_wireframe(X,Y,timeVals,rstride=10,cstride=10)
ax.view_init(20,50)

ax.scatter3D(xs[:,0],xs[:,1],ys,c=ys,cmap='cool')
ax.set_xlabel('workload')
ax.set_ylabel('executors')
ax.set_zlabel('time')

plt.savefig('output.png')