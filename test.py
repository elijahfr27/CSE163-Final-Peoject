import pandas as pd
import matplotlib.pyplot as plt
import os
from IPython.display import display
import filter


def main():
    data = filter.build_csv('data\\14-15_grad.csv')
    print(data.columns)


if __name__ == '__main__':
    main()
