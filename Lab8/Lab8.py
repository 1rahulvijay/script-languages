import pandas as pd
from pandas import DataFrame
import statsmodels.api as sm
import sys


# url https://www.kaggle.com/youneseloiarm/global-indices-in-us-markets

# task 2,3,4
def read_data_from_csv(fname):
    if fname.endswith('.csv'):
        print("File format right and its opening")
    else:
        print("Wrong file format, Try Again")
        sys.exit()
    data = pd.read_csv(fname)
    print(data)
    print(data.head())
    print(data.describe())

    x = DataFrame(data, columns=['High'])
    y = DataFrame(data, columns=['Low'])

    model = sm.OLS(y, x).fit()
    print(model.summary())

# Task 5,6
def sum_args(fname, args):
    data = pd.read_csv(fname)
    model_w = data.groupby('Volume', as_index=False).agg({"Adj Close": "sum"})
    if("-o" in args):
        print("Genrating databc.csv file")
        model_w.to_excel('DATABC')
    else:
        print("printing summary stats")
        model_w.to_excel('DATABC.xlsx')
        print(model_w)
        print(data.info())


# TASK 7
def display_help():
    print(":::::::::::::HELP:::::::::::::")
    print("input format: python <filename>.csv ")
    print("add -o <spreadsheet filename>.xlsx to record results in a spreadsheet, \n leave out if you wish to just see results here.")


def run():
    args = list(sys.argv)
    if ("-h" in args):
        display_help()
        sys.exit()
    fname = 'Dow_30.csv'
    read_data_from_csv(fname)
    sum_args(fname, args)


if __name__ == "__main__":
    run()
