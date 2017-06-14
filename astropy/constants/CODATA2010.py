# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Astronomical and physics constants in SI units.  See :mod:`astropy.constants`
for a complete listing of constants defined in Astropy.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np

from .constant import Constant


# PHYSICAL CONSTANTS

class Codata2010(Constant):
    default_reference = 'CODATA 2010'

    def __new__(cls, abbrev, name, value, unit, uncertainty,
                reference=default_reference, system=None):
        super().__new__(cls, abbrev, name, value, unit, uncertainty,
                        reference, system)


class EMCodata2010(Codata2010):
    """An electromagnetic constant."""

    @property
    def cgs(self):
        """Overridden for EMConstant to raise a `TypeError`
        emphasizing that there are multiple EM extensions to CGS.
        """

        raise TypeError("Cannot convert EM constants to cgs because there "
                        "are different systems for E.M constants within the "
                        "c.g.s system (ESU, Gaussian, etc.). Instead, "
                        "directly use the constant with the appropriate "
                        "suffix (e.g. e.esu, e.gauss, etc.).")



h = Codata2010('h', "Planck constant", 6.62606957e-34, 'J s',
                    0.00000029e-34, system='si')

hbar = Codata2010('hbar', "Reduced Planck constant",
                    h.value * 0.5 / np.pi, 'J s',
                    h.uncertainty * 0.5 / np.pi,
                    h.reference, system='si')

k_B = Codata2010('k_B', "Boltzmann constant", 1.3806488e-23, 'J / (K)',
                 0.0000013e-23, system='si')

c = Codata2010('c', "Speed of light in vacuum", 2.99792458e8, 'm / (s)', 0.,
               system='si')

G = Codata2010('G', "Gravitational constant", 6.67384e-11, 'm3 / (kg s2)',
               0.00080e-11, system='si')

g0 = Codata2010('g0', "Standard acceleration of gravity", 9.80665, 'm / s2', 0.0,
                system='si')

m_p = Codata2010('m_p', "Proton mass", 1.672621777e-27, 'kg', 0.000000074e-27,
                 system='si')

m_n = Codata2010('m_n', "Neutron mass", 1.674927351e-27, 'kg', 0.000000074e-27,
                 system='si')

m_e = Codata2010('m_e', "Electron mass", 9.10938291e-31, 'kg', 0.00000040e-31,
                 system='si')

u = Codata2010('u', "Atomic mass", 1.660538921e-27, 'kg', 0.000000073e-27,
               system='si')

sigma_sb = Codata2010('sigma_sb', "Stefan-Boltzmann constant", 5.670373e-8,
                      'W / (K4 m2)', 0.000021e-8, system='si')

e = EMCodata2010('e', 'Electron charge', 1.602176565e-19, 'C', 0.000000035e-19,
                 system='si')

eps0 = EMCodata2010('eps0', 'Electric constant', 8.854187817e-12, 'F/m', 0.0,
                    system='si')

N_A = Codata2010('N_A', "Avogadro's number", 6.02214129e23, '1 / (mol)',
                 0.00000027e23, system='si')

R = Codata2010('R', "Gas constant", 8.3144621, 'J / (K mol)', 0.0000075,
               system='si')

Ryd = Codata2010('Ryd', 'Rydberg constant', 10973731.568539, '1 / (m)',
                 0.000055, system='si')

a0 = Codata2010('a0', "Bohr radius", 0.52917721092e-10, 'm', 0.00000000017e-10,
                system='si')

muB = Codata2010('muB', "Bohr magneton", 927.400968e-26, 'J/T', 0.00002e-26,
                 system='si')

alpha = Codata2010('alpha', "Fine-structure constant", 7.2973525698e-3,
                    '', 0.0000000024e-3, system='si')

atm = Codata2010('atmosphere', "Atmosphere", 101325, 'Pa', 0.0,
                 system='si')

mu0 = Codata2010('mu0', "Magnetic constant", 4.0e-7 * np.pi, 'N/A2', 0.0,
                 system='si')

sigma_T = Codata2010('sigma_T', "Thomson scattering cross-section",
                     0.6652458734e-28, 'm2', 0.0000000013e-28, system='si')

b_wien = Constant('b_wien', 'Wien wavelength displacement law constant',
                  2.8977721e-3, 'm K', 0.0000026e-3, 'CODATA 2010', system='si')

# cgs constants
# Only constants that cannot be converted directly from S.I. are defined here.

e_esu = EMCodata2010(e.abbrev, e.name, e.value * c.value * 10.0,
                     'statC', e.uncertainty * c.value * 10.0, system='esu')

e_emu = EMCodata2010(e.abbrev, e.name, e.value / 10, 'abC',
                     e.uncertainty / 10, system='emu')

e_gauss = EMCodata2010(e.abbrev, e.name, e.value * c.value * 10.0,
                     'Fr', e.uncertainty * c.value * 10.0, system='gauss')