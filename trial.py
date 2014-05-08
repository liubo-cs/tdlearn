from experiments import *
from experiments import baird


def main():
    name = "baird" # the name of the experiment (in brackets above)
    measure = "RMSPBE" # Root Mean squared projected bellman error, alternatives: RMSE, RMSBE 
    plot_experiment(name, measure)

main()


