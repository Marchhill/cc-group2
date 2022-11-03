import matplotlib.pyplot as plt
import pandas as pd
import sys

def main(argv):
    if len(argv) < 1:
        print("ERROR: expecting timestamp")

    dirpath = "./experiments/"+argv[0]

    def plotGraph(fileName):
        df = pd.read_csv(dirpath+"/measurements/"+fileName+".csv")
        df.set_index('Workers', inplace=True)

        ax = df.plot.bar(rot=0)
        plt.ylabel("Time (s)")
        ax.get_legend().remove()
        plt.show()
        plt.savefig(dirpath+"/graphs/"+fileName+".pdf")
    
    for name in ['data-100MB', 'data-200MB', 'data-500MB']:
        plotGraph(name)
    

if __name__ == "__main__":
    main(sys.argv[1:])