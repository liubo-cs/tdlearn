# first line: 90
@memory.cache(hashfun={"mymdp": repr, "policy": repr, "policy_traj": repr}, ignore=["verbose"])
def samples_distribution(mymdp, policy, phi, policy_traj=None, n_subsample=1,
                         n_iter=1000, n_restarts=100, n_next=20, seed=1, verbose=True):
    assert(n_subsample == 1)  # not implemented, do that if you need it
    states = np.ones([n_restarts * n_iter, mymdp.dim_S])
    if policy_traj is None:
        policy_traj = policy
    states_next = np.ones([n_restarts * n_iter, mymdp.dim_S])
    feat = np.zeros((n_restarts * n_iter, phi.dim))
    feat_next = np.zeros_like(feat)
    rewards = np.ones(n_restarts * n_iter)
    np.random.seed(seed)

    k = 0
    s = mymdp.start()
    c = 0
    with ProgressBar(enabled=verbose) as p:
        for k in xrange(n_restarts * n_iter):
            if mymdp.terminal_f(s) or c >= n_iter:
                s = mymdp.start()
                c = 0
            p.update(k, n_restarts * n_iter, "Sampling MDP Distribution")
            s0, a, s1, r = mymdp.sample_step(
                s, policy=policy, n_samples=n_next)
            states[k, :] = s0
            feat[k, :] = phi(s0)
            fn = apply_rowise(phi, s1)
            feat_next[k, :] = np.mean(fn, axis=0)
            states_next[k, :] = np.mean(s1, axis=0)
            rewards[k] = np.mean(r)
            _, _, s, _ = mymdp.sample_step(s, policy=policy_traj, n_samples=1)
            c += 1

    return states, rewards, states_next, feat, feat_next
