# import numpy as np
import pandas as pd
from utility import master
# import matplotlib.pyplot as plt
#
#
# def estimate_coef(x, y):
#     # number of observations/points
#     n = np.size(x)
#
#     # mean of x and y vector
#     m_x = np.mean(x)
#     m_y = np.mean(y)
#
#     # calculating cross-deviation and deviation about x
#     SS_xy = np.sum(y * x) - n * m_y * m_x
#     SS_xx = np.sum(x * x) - n * m_x * m_x
#
#     # calculating regression coefficients
#     b_1 = SS_xy / SS_xx
#     b_0 = m_y - b_1 * m_x
#
#     return b_0, b_1
#
#
# def plot_regression_line(x, y, b):
#     # plotting the actual points as scatter plot
#     plt.scatter(x, y, color="m",
#                 marker="o", s=30)
#
#     # predicted response vector
#     y_pred = b[0] + b[1] * x
#
#     # plotting the regression line
#     plt.plot(x, y_pred, color="g")
#
#     # putting labels
#     plt.xlabel('x')
#     plt.ylabel('y')
#
#     # function to show plot
#     plt.show()
#
#
# def main():
#     # observations / data
#     x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
#
#     # estimating coefficients
#     b = estimate_coef(x, y)
#     print("Estimated coefficients:\nb_0 = {} \
# 		\nb_1 = {}".format(b[0], b[1]))
#
#     # plotting regression line
#     plot_regression_line(x, y, b)
#
#
# if __name__ == "__main__":
#     df = pd.read_csv(r'C:\Users\riaji\PycharmProjects\deposit_project\bank_revenue.csv')
#     df["TTM"] = df["TTM"].str.replace(",", "").astype(np.int64)
#     df["Interest Income"] = df["Interest Income"].str.replace(",", "").astype(np.int64)
#     df['Non Interest Income'] = df['TTM'] - df['Interest Income']
#     df['Max Rate'] = None
#     for bank in master:
#         df.loc[df['Bank Name'] == bank.name, 'Max Rate'] = bank.rate
#     df.sort_values(by='TTM', inplace=True)
#     # x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     # y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
#     df['TTM'] = df['TTM'].astype(str).str[:-8].astype(int)
#     print(df['TTM'].values)
#
#     x = df['TTM'].values
#     y = df['Max Rate'].values
#
#     # estimating coefficients
#     b = estimate_coef(x, y)
#     print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))
#
#     # plotting regression line
#     plot_regression_line(x, y, b)
#     print(df)
#     # main()


# USING SKLEARN
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv(r'C:\Users\riaji\PycharmProjects\deposit_project\bank_revenue.csv')
df["TTM"] = df["TTM"].str.replace(",", "").astype(np.int64)
df["Interest Income"] = df["Interest Income"].str.replace(",", "").astype(np.int64)
df['Non Interest Income'] = df['TTM'] - df['Interest Income']
df['Max Rate'] = None
for bank in master:
    df.loc[df['Bank Name'] == bank.name, 'Max Rate'] = bank.rate
df.sort_values(by='TTM', inplace=True)
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
df['TTM'] = df['TTM'].astype(str).str[:-8].astype(int)
df['Interest Income'] = df['Interest Income'].astype(str).str[:-8].astype(int)

# For multiple regression
x = df[['TTM', 'Interest Income']].values
y = df['Max Rate'].values

# For linear regression
# x = np.array(df['Interest Income'].values)
# x = x.reshape(-1, 1)
# y = df['Max Rate'].values

# Assume you have independent variables X and a dependent variable y

# Create an instance of the LinearRegression class
reg = LinearRegression()

# Fit the model to the data
reg.fit(x, y)

# Print the coefficients of the model
print(reg.coef_)

