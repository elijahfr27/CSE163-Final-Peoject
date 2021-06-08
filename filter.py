import pandas as pd
import os


def build_csv(filename):
    data = pd.read_csv(filename, dtype={(0, 4, 5, 7, 8, 10): int, range(15, 30): int, (1,2,3,6,9,11,12,13,14): str})
    return data


def main():
    datasets = dict()

    for filename in os.listdir('data'):
        path = os.path.join('data', filename)
        with open(path) as f:
            data = pd.read_csv(f)
            short_name = filename[: - 4].split('_')
            datasets[short_name[2]] = filename

    for key, value in datasets.items():
        print(key)


if __name__ == '__main__':
    main()
