"""
f(x_0)

theta: (n + 1, 1)
x: (n) => (n + 1)
y: (1, 1)
Y: (m, 1)

X: (m, n + 1)
XT : (n + 1, m) . (m, 1) ==> (n + 1, 1)

X . theta
(m, n + 1) (n + 1, 1) ==> (m, 1)

theta_0 + theta_1 x_1 + theta_2 x_2  +  .. theta_n x_n

h(theta, x) = theta.dot(x)



"""