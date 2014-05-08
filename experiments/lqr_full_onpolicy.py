# -*- coding: utf-8 -*-
"""
pole balancing experiment with prefect features and on-policy samples
"""
__author__ = "Christoph Dann <cdann@cdann.de>"
import td
import examples
import numpy as np
import matplotlib.pyplot as plt
import dynamic_prog as dp
import features
import policies
from task import LinearLQRValuePredictionTask
import pickle

gamma = 0.95
sigma = np.array([0.] * 3 + [0.01])
dt = 0.1
mdp = examples.PoleBalancingMDP(sigma=sigma, dt=dt)
phi = features.squared_tri(11)


n_feat = len(phi(np.zeros(mdp.dim_S)))
theta_p, _, _ = dp.solve_LQR(mdp, gamma=gamma)
theta_p = np.array(theta_p).flatten()

policy = policies.LinearContinuous(theta=theta_p, noise=np.zeros((1)))
theta0 = 0. * np.ones(n_feat)

task = LinearLQRValuePredictionTask(
    mdp, gamma, phi, theta0, policy=policy, normalize_phi=True, mu_next=1000)

#phi = task.phi
#print "V_true", task.V_true
#print "theta_true"
#theta_true = phi.param_forward(*task.V_true)
#print theta_true
#task.theta0 = theta_true

methods = []
alpha = 0.0005
mu = .001
gtd = td.GTD(alpha=alpha, beta=mu * alpha, phi=phi)
gtd.name = r"GTD $\alpha$={} $\mu$={}".format(alpha, mu)
gtd.color = "r"
methods.append(gtd)

alpha, mu = 0.005, 0.5
gtd = td.GTD2(alpha=alpha, beta=mu * alpha, phi=phi)
gtd.name = r"GTD2 $\alpha$={} $\mu$={}".format(alpha, mu)
gtd.color = "orange"
methods.append(gtd)

alpha = td.RMalpha(0.01, 0.05)
lam = .0
td0 = td.LinearTDLambda(alpha=alpha, lam=lam, phi=phi, gamma=gamma)
td0.name = r"TD({}) $\alpha$={}".format(lam, alpha)
td0.color = "k"
methods.append(td0)

alpha = .008
lam = .2
td0 = td.LinearTDLambda(alpha=alpha, lam=lam, phi=phi, gamma=gamma)
td0.name = r"TD({}) $\alpha$={}".format(lam, alpha)
td0.color = "k"
methods.append(td0)

lam = 0.0
alpha = 0.007
mu = 0.05
tdc = td.TDCLambda(alpha=alpha, mu = mu, lam=lam, phi=phi, gamma=gamma)
tdc.name = r"TDC({}) $\alpha$={} $\mu$={}".format(lam, alpha, mu)
tdc.color = "b"
methods.append(tdc)

alpha = .1
lam = 0.0
lstd = td.RecursiveLSPELambda(lam=lam, alpha=alpha, phi=phi, gamma=gamma)
lstd.name = r"LSPE({}) $\alpha$={}".format(lam, alpha)
lstd.color = "g"
methods.append(lstd)

lam = 0.0
eps = 10
lstd = td.RecursiveLSTDLambda(lam=lam, eps=eps, phi=phi, gamma=gamma)
lstd.name = r"LSTD({}) $\epsilon$={}".format(lam, eps)
lstd.color = "g"
lstd.ls = "-."
methods.append(lstd)
#
alpha = 0.5
beta=10.
mins=500
lam =.8
lstd = td.FPKF(lam=lam, alpha = alpha, beta=beta, mins=mins, phi=phi, gamma=gamma)
lstd.name = r"FPKF({}) $\alpha$={}".format(lam, alpha)
lstd.color = "g"
lstd.ls = "-."
methods.append(lstd)

alpha = .02
rg = td.ResidualGradientDS(alpha=alpha, phi=phi, gamma=gamma)
rg.name = r"RG DS $\alpha$={}".format(alpha)
rg.color = "brown"
rg.ls = "--"
methods.append(rg)

alpha = .01
rg = td.ResidualGradient(alpha=alpha, phi=phi, gamma=gamma)
rg.name = r"RG $\alpha$={}".format(alpha)
rg.color = "brown"
methods.append(rg)

reward_noise = 1e-1
ktd = td.KTD(phi=phi, gamma=gamma, theta_noise=None, eta=1e-5, P_init=1.,
             reward_noise=reward_noise)
ktd.name = r"KTD $r_n={}$".format(reward_noise)
#methods.append(ktd)

brm = td.BRMDS(phi=phi, eps=10)
brm.name = "BRMDS"
brm.color = "b"
brm.ls = "--"
methods.append(brm)

brm = td.BRM(phi=phi, eps=10)
brm.name = "BRM"
brm.color = "b"
methods.append(brm)

sigma = 0.31
gptdp = td.GPTDP(phi=phi, sigma=sigma)
gptdp.name = r"GPTDP $\sigma$={}".format(sigma)
#methods.append(gptdp)

lam = .2 #suboptimal!!
sigma = .031
gptdp = td.GPTDPLambda(phi=phi, tau=sigma, lam=lam)
gptdp.name = r"GPTDP({}) $\sigma$={}".format(lam,sigma)
gptdp.ls="--"
#methods.append(gptdp)


l = 15000
error_every = 500
n_indep = 200
n_eps = 1
episodic=False
criteria = ["RMSPBE", "RMSBE", "RMSE"]
criterion = "RMSPBE"
name = "lqr_full_onpolicy"
title = "7. Lin. Cart-Pole Balancing On-pol. Perf. Feat."


if __name__ == "__main__":
    from experiments import *
    mean, std, raw = run_experiment(n_jobs=-1, **globals())
    save_results(**globals())
    #plot_errorbar(**globals())
