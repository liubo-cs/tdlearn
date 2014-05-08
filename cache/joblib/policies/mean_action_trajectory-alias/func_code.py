# first line: 9
@util.memory.cache(hashfun={"policy": repr})
def mean_action_trajectory(policy, states):
    ret = np.empty((states.shape[0], policy.dim_A))
    for i in xrange(states.shape[0]):
        ret[i] = policy.mean(states[i])
    return ret
