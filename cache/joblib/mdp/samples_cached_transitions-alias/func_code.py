# first line: 47
@memory.cache(hashfun={"mymdp": repr, "policy": repr})
def samples_cached_transitions(mymdp, policy, states, seed=2):
    assert(seed is not None)
    n = states.shape[0]
    states_next = np.ones([n, mymdp.dim_S])
    actions = np.ones([n, mymdp.dim_A])
    rewards = np.ones(n)
    np.random.seed(seed)

    for k in xrange(n):
        _, a, s_n, r = mymdp.sample_step(states[k], policy=policy)
        states_next[k, :] = s_n
        rewards[k] = r
        actions[k, :] = a

    return actions, rewards, states_next
