# Learn LINEAR REGRESSION theory

# y_i = b_0 + b_1*x_i + e_i
#
#
#   e_i = random error [Need to minimize]
#
#   Simple linear regression[SLR]: Minimizing errors
#           (a) Signed Errors Cancel out
#
#   SLR: Ordinary Least Squares [OLS]
#       [...]
#       b_1 = sum{(xi-xbar)*(yi-ybar)}/sum{(xi-xbar)^2}
#       b_0 = ybar - b_1 * xbar
#
#   Thus, regression model equation:
#       yhat = b_0 + b_1*x
#               yhat == y_prediction_from_model

#   TODO: See difference between y-bar and y-hat


# determining b_0 and b_1 example:
#
# question: 
#       Find b_0 and b_1 for correlation between temperature (degC) and converstion (%)
#                          +----------------+----------------+
#                          | Temp, T (degC) | Conversion (%) |
#                          +----------------+----------------+
#                          |      200       |      0.35      |
#                          |      220       |      0.45      |
#                          |      240       |      0.52      |
#                          |      260       |      0.61      |
#                          +----------------+----------------+

import numpy as np
import matplotlib.pyplot as plt

T = np.array([200, 220, 240, 260])
C = np.array([0.35, 0.45, 0.52, 0.61])
plt.scatter(T,C)

b_1 = np.sum((T - np.mean(T)) * (C - np.mean(C))) / np.sum((T - np.mean(T))**2)
b_0 = np.mean(C) - b_1*np.mean(T)

print(b_0, b_1)


C_predicted = b_0 + b_1 * T
plt.plot(T, C_predicted, color="red")

plt.xlabel("Temperature, T (degC)")
plt.ylabel("Converstion (%)")
plt.title("Regression model")
plt.legend(["Data Points", "Regression line"])
plt.show()



#   SLR: SSR/ SSE/ SST/ R^2
#
#   SSR = sum{(yhat_i - ybar_i)^2}
#   SSE = sum{(y_i - yhat_i)^2}
#   SST = SSR + SSE
#   R^2 = SSR/SST = (SST-SSE)/SST = 1- (SSE/SST)
#
#   Regression line fits better => SSE inc. => Deviation dec. => R^2 inc.

SSR = np.sum((C_predicted - np.mean(C))**2)
SSE = np.sum((C - C_predicted)**2)
SST = SSR + SSE
R_square = 1-(SSE/SST)

print("R^2 = " + str(R_square))


# NOTE: Don't blindly rely on R^2
#
#       MAE = (1/n)* sum{y_i - yhat_i}              [want minimized]
#       RMSE - sqrt{ (1/n)* sum{y_i - yhat_i} }     [want Maximized]
#
#   Residual analysis:
#       residual = y_i - yhat_i                     [want minimized]





# Multiple Linear Regression [MLR]:
#
#       y = b_0 + b_1*x_1 + b_2*x_2 +...+ b_p*x_p + e
#
#   Matrix form:
#           Y = B*X + E
#
#                       Y = Output vector
#                       X = Design matrix
#                       B = Coefficent vector
#                       E = Error term
#
#   Target: Minimize E
#
#
#
#   MLR: Determining B
#
#   [...] => B = (X^t * X)^-1 * X^t * Y <--> inv(Xt * X) * Xt * Y



temperature_deg_c = np.array([180, 200, 200, 220, 220, 240, 240, 260, 260])
pressure_bar = np.array([5,5,10,5,10,5,15,10,15])
residence_time_min = np.array([10,10,15,20,10,25,15,20,25])
ones = np.ones(temperature_deg_c.shape[0])

X = np.column_stack((ones, temperature_deg_c, pressure_bar, residence_time_min))

Y = np.array([0.284,0.338,0.641,0.678,0.953,0.986,0.821,0.942,0.998])

B_np_method = np.linalg.lstsq(X, Y)[0]

B_manual = np.linalg.inv(X.T @ X) @ X.T @ Y

print("B (auto) = ", B_np_method)
print("B (manual) = ", B_manual)

Y_predicted = X @ B_np_method
residuals = Y - Y_predicted
plt.figure()
plt.scatter(X[:,1], residuals)
plt.axhline(y=0, color="r", linestyle="--")
plt.show()



# using csv files


import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"data_files/class_6__05_09_2026_file.csv")
X_pd_method = df[["Temp (C)","Pressure (bar)","Residence Time (min)"]]
Y_pd_method = df["Conversion (%)"]
model = LinearRegression()

model.fit(X_pd_method,Y_pd_method)

X_pd_method_predicted = model.predict(X_pd_method)
accuracy = model.score(X_pd_method, Y_pd_method)

print("Predicted X using sklearn = ", X_pd_method_predicted)
print("Accuracy score of prediction = ", accuracy)

