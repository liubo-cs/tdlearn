# first line: 81
@memory.cache
def solve_LQR(lqmdp, n_iter=100000, gamma=1., eps=1e-14):
    """ Solves exactly the Linear-quadratic MDP with
        the value function has the form
        V* = s^T P* s and policy a = theta* s

        returns (theta*, P*)"""


    P = np.matrix(np.zeros((lqmdp.dim_S, lqmdp.dim_S)))
    R = np.matrix(lqmdp.R)
    b = 0.
    theta = np.matrix(np.zeros((lqmdp.dim_A, lqmdp.dim_S)))
    A = np.matrix(lqmdp.A)
    B = np.matrix(lqmdp.B)
    for i in xrange(n_iter):
        theta_n = - gamma * np.linalg.pinv(R + gamma * B.T * P *
                                           B) * B.T * P * A
        P_n, b_n = bellman_operator(lqmdp, P, b, theta, gamma=gamma)  # Q + theta.T * R * theta + gamma * (A+ B * theta).T * P * (A + B * theta)
        if np.linalg.norm(P - P_n) < eps and np.abs(b - b_n) < eps and np.linalg.norm(theta - theta_n) < eps:
            print "Converged estimating V after ", i, "iterations"
            break
        P = P_n
        b = b_n
        theta = theta_n
    return np.asarray(theta), P, b
