"""
x       y
100     345
100     350
100     320
200     680

100     335


x       y       y_hat       |y_hat - y|     (y_hat - y)^2
0       0       1           1               1
1       2       3           1               1
2       4       5           1               1
3       6       7           1               1
4       8       9           1               1

0       0       -1          -1 => 1
1       1       1           0
2       2       3           1
                            2

11      22

f(x) = 1 + 1.8x

f(x) = a + bx

Gradient descent
df(x) / dx

theta_0 = theta_0 - dJ/dtheta_0 * (k)
theta_1 = theta_1 - dJ/dtheta_1 * (k)

"""
