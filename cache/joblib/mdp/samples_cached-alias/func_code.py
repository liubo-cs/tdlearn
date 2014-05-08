# first line: 17
@memory.cache(hashfun={"mymdp": repr, "policy": repr}, ignore=["verbose"])
def samples_cached(mymdp, policy, n_iter=1000, n_restarts=100,
                   no_next_noise=False, seed=1., verbose=0.):
    assert(seed is not None)
    states = np.ones([n_restarts * n_iter, mymdp.dim_S])
    states_next = np.ones([n_restarts * n_iter, mymdp.dim_S])
    actions = np.ones([n_restarts * n_iter, mymdp.dim_A])
    rewards = np.ones(n_restarts * n_iter)
    np.random.seed(seed)

    restarts = np.zeros(n_restarts * n_iter, dtype="bool")
    k = 0

    with ProgressBar(enabled=(verbose > 2.)) as p:
        while k < n_restarts * n_iter:
            restarts[k] = True
            for s, a, s_n, r in mymdp.sample_transition(
                    n_iter, policy, with_restart=False, seed=None):
                states[k, :] = s
                states_next[k, :] = s_n
                rewards[k] = r
                actions[k, :] = a

                k += 1
                p.update(k, n_restarts * n_iter)
                if k >= n_restarts * n_iter:
                    break
    return states, actions, rewards, states_next, restarts
