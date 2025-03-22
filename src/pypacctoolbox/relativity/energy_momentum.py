from ..base.registry import registry

from sympy import Symbol, sqrt

def beta_velocity(velocity = Symbol("v")) :
    c = Symbol("c")
    return velocity/c

def gamma_beta(beta = Symbol("beta", positive=True)) :
    return 1/sqrt(1-beta**2)

def gamma_E_m(E = Symbol("E"), m0 = Symbol("m0")) :
    return E/m0

def energy_gamma_mass(gamma = Symbol("gamma"), m0 = Symbol("m0")):
    c = Symbol("c")
    return gamma*m0*c**2

def momentum_gammma_mass_velocity(gamma = Symbol("gamma"), m0 = Symbol("m0"), v = Symbol("v")) :
    c = Symbol("c")
    return gamma*m0*v

registry.add_expression("relativity", "beta_velocity", Symbol("beta"), beta_velocity(), "Relativistic beta from velocity")
registry.add_expression("relativity","gamma_beta", Symbol("gamma"), gamma_beta(), "Relativistic gamma from beta")
registry.add_expression("relativity","gamma_E_m", Symbol("gamma"), gamma_E_m(), "Relativistic gamma from energy and mass")
registry.add_expression("relativity", "energy_gamma_mass", Symbol("E"), energy_gamma_mass(), "Energy from gamma and mass")
