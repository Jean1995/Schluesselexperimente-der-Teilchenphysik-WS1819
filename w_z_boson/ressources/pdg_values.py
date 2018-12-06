
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2
import numpy as np

year = np.array([
    1984,
    1988,
    #LEP geht in Betrieb
    1990,
    1992,
    1994,
    1995,
    1996,
    1997,
    1998,
    1999,
    2000,
    #hier ändert sich das letzte mal der Wert für das Z Boson (LEP abgestellt?)
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    #Tevatron macht dicht
    2012,
])

# "our fit"
m_w = np.array([
    80.9,
    81.0,
    80.6,
    80.22,
    80.22,
    80.33,
    80.33,
    80.36,
    80.41,
    80.42,
    80.43,
    80.43,
    80.423,
    80.425,
    80.425,
    80.425,
    80.403,
    80.403,
    80.398,
    80.398,
    80.399,
    80.399,
    80.385
    ])

m_w_error = np.array([
    1.5,
    1.3,
    0.4,
    0.26,
    0.26,
    0.15,
    0.15,
    0.12,
    0.1,
    0.05,
    0.05,
    0.04,
    0.039,
    0.038,
    0.038,
    0.038,
    0.029,
    0.029,
    0.025,
    0.025,
    0.023,
    0.023,
    0.015
    ])

m_z = np.array([
    95.6,
    92.4,
    91.161,
    91.173,
    91.187,
    91.187,
    91.187,
    91.187,
    91.187,
    91.187,
    91.1882,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876,
    91.1876
    ])

m_z_error = np.array([
    1.4,
    1.8,
    0.031,
    0.02,
    0.007,
    0.007,
    0.007,
    0.007,
    0.007,
    0.007,
    0.0022,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021,
    0.0021
])

plt.errorbar(year, m_w, yerr=m_w_error, fmt='.', capthick=2)
plt.ylabel(r'$M_W \,/\, GeV$')
plt.xlabel('Jahr')
plt.tight_layout()
plt.savefig('mw.pdf')

plt.clf()
plt.errorbar(year, m_z, yerr=m_z_error, fmt='.', capthick=2)
plt.ylabel(r'$M_Z \,/\, GeV$')
plt.xlabel('Jahr')
plt.tight_layout()
plt.savefig('mz.pdf')
