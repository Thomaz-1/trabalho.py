import matplotlib.pyplot as plt
import numpy as np
erro1 = []
erro2 = []
erro3 = []
x0 = 1/1024
x = 8
c = 0
logdx = []
while True:
    if x0 > 4:
        break
    dx = 1 + np.log(x)
    log = np.log(x)
    log_dx = np.log(x+x0)
    ''''calculo da derivada regressiva'''
    log_ant = np.log(x-x0)
    fx_ant = (x * log - (x-x0) * log_ant) / x0
    err2 = abs(fx_ant - dx)
    log_err2 = np.log(err2)
    erro2.insert(c, log_err2)
    ''''calculo da derivada progressiva'''
    fx_pos = ((x+x0) * log_dx - (x * log)) / x0
    err1 = abs(dx - fx_pos)
    log_err1 = np.log(err1)
    erro1.insert(c, log_err1)
    ''''calculo da derivada central'''
    fx_central = ((x+x0) * log_dx - (x-x0) * log_ant)/(2 * x0)
    err3 = abs(fx_central - dx)
    log_erro3 = np.log(err3)
    erro3.insert(c, log_erro3)
    ''''adição ao contador e novo intervalo'''
    c = c + 1
    logdx.insert(c, np.log(x0))
    x0 = x0*2
''''plot do grafico'''
plt.style.use('ggplot')
plt.ylabel('log|erro|')
plt.xlabel('log(ΔX)')
plt.plot(logdx, erro1, color='red')
plt.plot(logdx, erro2, color='blue')
plt.plot(logdx, erro3, color='yellow')
plt.show()
