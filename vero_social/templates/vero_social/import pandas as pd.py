import pandas as pd



def series_example():
    serie1 = pd.Series([1,2,3,4], name="serie_")
    print(serie1)


if __name__ == "__main__":
    series_example()