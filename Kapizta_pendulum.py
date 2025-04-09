import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as intgr

#Graph
def equations(X, t, alpha, omega):    # calculate time derivatives
    theta, eta = X    # parse variables
    d_theta = eta
    d_eta = (1 - alpha * omega**2 * np.cos(omega*t)) * np.sin(theta)
    return [d_theta, d_eta]    # assemble derivatives into an array

alpha = 0.1    # amplitude of pivot << 1
omega = 30.    # omega >> 1

theta0 = 0.1    # initial position
eta0 = 0.0    # initial speed

T = 10.    # total time to solve for
time = np.arange(0, T, 0.01)    # time points to evaluate solution at

sol = intgr.odeint(equations, [theta0, eta0], time, args=(alpha, omega))    # solve equations
theta = sol[:,0]    # theta is the first component of solution


#Animation
plt.rcParams["animation.html"] = "jshtml"
fig, ax = plt.subplots(figsize=(4,4))
ax.set_xlim(-1,1)
ax.set_ylim(-0.5,1.5)
ax.axis('off')
p0, =ax.plot([], [],'-')
p1, =ax.plot([], [], 'o')

def animate(t):
    Zt = alpha * np.cos(omega * time[t])
    Xt = np.sin(theta[t])
    Yt = np.cos(theta[t])
    p0.set_data([Xt, 0], [Yt, Zt])
    p1.set_data([Xt], [Yt])

mov=anim.FuncAnimation(fig, animate, frames=len(time), interval=10)
plt.show()
plt.close()







