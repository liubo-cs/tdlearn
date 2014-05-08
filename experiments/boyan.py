# -*- coding: utf-8 -*-
"""
Boyan Chain Experiment
"""
__author__ = "Christoph Dann <cdann@cdann.de>"

import td
import examples
from task import LinearDiscreteValuePredictionTask
import numpy as np
import features

n = 14
n_feat = 4
mdp = examples.BoyanChain(n, n_feat)
phi = features.spikes(n_feat, n)
gamma = .95
p0 = np.zeros(n_feat)
task = LinearDiscreteValuePredictionTask(mdp, gamma, phi, p0)

# define the methods to examine
gtd2 = td.GTD2(alpha=0.5, beta=0.5, phi=phi)
gtd2.name = "GTD2"
gtd2.color = "#0F6E08"

gtd = td.GTD(alpha=0.5, beta=0.5, phi=phi)
gtd.name = "GTD"
gtd.color = "#6E086D"

methods = []


'''
BEGIN COMPARISON
'''

alpha = .5
mu = 1.
gtd = td.GTD2(alpha=alpha, beta=mu * alpha, phi=phi)
gtd.name = r"GTD2 $\alpha$={} $\mu$={}".format(alpha, mu)
gtd.color = "#6E086D"
methods.append(gtd)



alpha = 0.2
mu = 0.0001
#lam = 1.
#tdc = td.TDCLambda(lam=lam, alpha=alpha, beta=alpha * mu, phi=phi)
tdc = td.TDC(alpha=alpha, beta=alpha * mu, phi=phi, gamma=gamma)
tdc.name = r"TDC $\alpha$={} $\mu$={}".format(alpha, mu)
tdc.color = "r"
methods.append(tdc)


'''
my code here
'''
alpha = .5
mu = 1.
gtd = td.GTD2MP(alpha=alpha, beta=mu * alpha, phi=phi)
gtd.name = r"GTD2-MP $\alpha$={} $\mu$={}".format(alpha, mu)
gtd.color = "orange"
methods.append(gtd)

alpha = 0.2
mu = 0.0001
tdc = td.TDCMP(alpha=alpha, beta=mu * alpha, phi=phi)
tdc.name = r"TDC-MP $\alpha$={} $\mu$={}".format(alpha, mu)
tdc.color = "k"
methods.append(tdc)

'''
ENDOF my code 
'''


'''
alpha = .5
mu = 2.
gtd = td.GTD(alpha=alpha, beta=mu * alpha, phi=phi)
gtd.name = r"GTD $\alpha$={} $\mu$={}".format(alpha, mu)
gtd.color = "#6E086D"
methods.append(gtd)

alpha = 0.2
lam = 1.
td0 = td.LinearTDLambda(alpha=alpha, lam=lam, phi=phi)
td0.name = r"TD({}) $\alpha$={}".format(lam, alpha)
methods.append(td0)

alpha = td.RMalpha(10., 0.5)
lam = 0.
td0 = td.LinearTDLambda(alpha=alpha, lam=lam, phi=phi)
td0.name = r"TD({}) $\alpha={}t^{{-{} }}$".format(lam, alpha.c, alpha.mu)
methods.append(td0)

alpha = td.DabneyAlpha()
lam = 0.
td0 = td.LinearTDLambda(alpha=alpha, lam=lam, phi=phi)
td0.name = r"TD({}) $\alpha$=aut.".format(lam)
methods.append(td0)

lam = .8
eps = 10000
lstd = td.RecursiveLSTDLambda(lam=lam, eps=eps, phi=phi)
lstd.name = r"LSTD({})".format(lam)
methods.append(lstd)

lam = .0
eps = 100
lstd = td.RecursiveLSTDLambda(lam=lam, eps=eps, phi=phi)
lstd.name = r"LSTD({})".format(lam)
methods.append(lstd)

lam = .8
alpha = 1.
lspe = td.RecursiveLSPELambda(lam=lam, alpha=alpha, phi=phi)
lspe.name = r"LSPE({}) $\alpha$={}".format(lam, alpha)
methods.append(lspe)

lam = .0
alpha = .01
beta = 1000
mins = 0
lstd = td.FPKF(lam=lam, alpha=alpha, beta=beta, mins=mins, phi=phi)
lstd.name = r"FPKF({}) $\alpha={}$ $\beta={}$".format(lam, alpha, beta)
lstd.ls = "--"
methods.append(lstd)

brm = td.RecursiveBRMDS(phi=phi)
brm.name = "BRMDS"
brm.color = "b"
brm.ls = "--"
methods.append(brm)

brm = td.RecursiveBRM(phi=phi)
brm.name = "BRM"
brm.color = "b"
methods.append(brm)

alpha = 0.5
rg = td.ResidualGradientDS(alpha=alpha, phi=phi)
rg.name = r"RG DS $\alpha$={}".format(alpha)
rg.ls = "--"
methods.append(rg)

alpha = 0.5
rg = td.ResidualGradient(alpha=alpha, phi=phi)
rg.name = r"RG $\alpha$={}".format(alpha)
methods.append(rg)

eta = 0.001
reward_noise = 0.001
P_init = 1.
ktd = td.KTD(phi=phi, gamma=1., P_init=P_init, theta_noise=None, eta=eta,
             reward_noise=reward_noise)
ktd.name = r"KTD $\eta$={}, $\sigma^2$={} $P_0$={}".format(
    eta, reward_noise, P_init)
#methods.append(ktd)

sigma = 1.
gptdp = td.GPTDP(phi=phi, sigma=sigma)
gptdp.name = r"GPTDP $\sigma$={}".format(sigma)
gptdp.ls = "--"
#methods.append(gptdp)

lam = .8
sigma = 1e-5
gptdp = td.GPTDPLambda(phi=phi, tau=sigma, lam=lam)
gptdp.name = r"GPTDP({}) $\sigma$={}".format(lam, sigma)
gptdp.ls = "--"
#methods.append(gptdp)
'''

l = 20
n_eps = 100
episodic = True
error_every = 1
name = "boyan"
n_indep = 20
title = "1. 14-State Boyan Chain".format(n, n_indep)
criterion = "RMSPBE"
criteria = ["RMSPBE", "RMSBE", "RMSE"]

gs_errorevery = 1

if __name__ == "__main__":
    from experiments import *
    mean, std, raw = run_experiment(n_jobs=1, **globals())
    save_results(**globals())
    plot_errorbar(**globals())
