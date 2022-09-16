import numpy as np
import matplotlib.pyplot as plt

f = 0
g = 1
n = int(input("diga a quantidade de pontos: "))
delta = 0.1/(n-1)
ESP = np.zeros((n, 1))
ESP2 = np.zeros((n, 1))
err = np.zeros((2, 0))
E = np.zeros((n, 1))
S = np.zeros((n, 1))
M = np.zeros((n, n))
R = np.zeros((n, 1))
M[0][0] = 1
M[n - 1][n - 1] = 1
R[0][0] = 100
R[n - 1][0] = 20
while f < n:
    S[f][0] = 0.6 + 8 * delta * f
    E[f][0] = 100 - 80 * (np.log((0.6 + 8 * delta * f) / 0.6) / np.log(1.4 / 0.6))
    ESP[f][0] = delta * f
    f = f + 1
while g < (n-1):
    M[g][g - 1] = ((S[g + 1][0] - S[g - 1][0]) / 4) - S[g][0]
    M[g][g] = 2 * S[g][0]
    M[g][g + 1] = ((S[g - 1][0] - S[g + 1][0]) / 4) - S[g][0]
    E[g][0] = 100 - 80 * (np.log((0.6 + 8 * delta * g) / 0.6) / np.log(1.4 / 0.6))
    g = g+1
Minv = np.linalg.inv(M)
T1 = Minv.dot(R)
err = np.subtract(T1, E)
ESP2 = ESP
log_err = np.log(abs(err))
'''plt.plot(T1, ESP, label='5', linewidth=0.8)'''
plt.plot(ESP2, log_err, label='5')


f = 0
g = 1
n = int(input("diga a quantidade de pontos: "))
delta = 0.1/(n-1)
erro2 = np.zeros((n, 1))
ESP = np.zeros((n, 1))
E = np.zeros((n, 1))
S = np.zeros((n, 1))
M = np.zeros((n, n))
R = np.zeros((n, 1))
M[0][0] = 1
M[n - 1][n - 1] = 1
R[0][0] = 100
R[n - 1][0] = 20
while f < n:
    S[f][0] = 0.6 + 8 * delta * f
    E[f][0] = 100 - 80 * (np.log((0.6 + 8 * delta * f) / 0.6) / np.log(1.4 / 0.6))
    ESP[f][0] = delta * f
    f = f + 1
while g < (n-1):
    M[g][g - 1] = ((S[g + 1][0] - S[g - 1][0]) / 4) - S[g][0]
    M[g][g] = 2 * S[g][0]
    M[g][g + 1] = ((S[g - 1][0] - S[g + 1][0]) / 4) - S[g][0]
    E[g][0] = 100 - 80 * (np.log((0.6 + 8 * delta * g) / 0.6) / np.log(1.4 / 0.6))
    g = g+1
Minv = np.linalg.inv(M)
T2 = Minv.dot(R)
erro2 = np.subtract(T2, E)
err2 = erro2
ESP2 = ESP
log_err2 = np.log(abs(err2))
plt.plot(ESP2, log_err2, label='9')
'''plt.plot(T2, ESP, label='9', linewidth=0.8)'''
print(E)
print(T2)
print(err2)

f = 0
g = 1
n = int(input("diga a quantidade de pontos: "))
delta = 0.1/(n-1)
erro3 = np.zeros((n, 1))
ESP = np.zeros((n, 1))
E = np.zeros((n, 1))
S = np.zeros((n, 1))
M = np.zeros((n, n))
R = np.zeros((n, 1))
M[0][0] = 1
M[n - 1][n - 1] = 1
R[0][0] = 100
R[n - 1][0] = 20
while f < n:
    S[f][0] = 0.6 + 8 * delta * f
    E[f][0] = 100 - 80 * (np.log((0.6 + 8 * delta * f) / 0.6) / np.log(1.4 / 0.6))
    ESP[f][0] = delta * f
    f = f + 1
while g < (n-1):
    M[g][g - 1] = ((S[g + 1][0] - S[g - 1][0]) / 4) - S[g][0]
    M[g][g] = 2 * S[g][0]
    M[g][g + 1] = ((S[g - 1][0] - S[g + 1][0]) / 4) - S[g][0]
    E[g][0] = 100 - 80 * (np.log((0.6 + 8 * delta * g) / 0.6) / np.log(1.4 / 0.6))
    g = g+1
Minv = np.linalg.inv(M)
T1 = Minv.dot(R)
err2 = np.subtract(T1, E)
ESP2 = ESP
log_err2 = np.log(abs(err2))
'''plt.plot(T1, ESP, label='20', linewidth=0.8)'''
plt.plot(ESP2, log_err2, label='20')


f = 0
g = 1
n = int(input("diga a quantidade de pontos: "))
delta = 0.1/(n-1)
erro4 = np.zeros((n, 1))
ESP = np.zeros((n, 1))
E = np.zeros((n, 1))
S = np.zeros((n, 1))
M = np.zeros((n, n))
R = np.zeros((n, 1))
M[0][0] = 1
M[n - 1][n - 1] = 1
R[0][0] = 100
R[n - 1][0] = 20
while f < n:
    S[f][0] = 0.6 + 8 * delta * f
    E[f][0] = 100 - 80 * (np.log((0.6 + 8 * delta * f) / 0.6) / np.log(1.4 / 0.6))
    ESP[f][0] = delta * f
    f = f + 1
while g < (n-1):
    M[g][g - 1] = ((S[g + 1][0] - S[g - 1][0]) / 4) - S[g][0]
    M[g][g] = 2 * S[g][0]
    M[g][g + 1] = ((S[g - 1][0] - S[g + 1][0]) / 4) - S[g][0]
    E[g][0] = 100 - 80 * (np.log((0.6 + 8 * delta * g) / 0.6) / np.log(1.4 / 0.6))
    g = g+1
Minv = np.linalg.inv(M)
T1 = Minv.dot(R)
err4 = np.subtract(T1, E)
ESP2 = ESP
log_err4 = np.log(abs(err4))
'''plt.plot(T1, ESP, label='50', linewidth=0.8)'''
plt.plot(ESP2, log_err4, label='50')
plt.legend()
plt.show()