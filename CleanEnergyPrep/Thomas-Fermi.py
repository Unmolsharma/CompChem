import numpy as np
import matplotlib.pyplot as plt

def thomas_fermi_density(r, mu, V):
    return np.where(mu >= V, ((5/3) * kin * (mu - V))**(3/2), 0)

# Constants
h = 6.62607015e-34  # Planck's constant
me = 9.10938356e-31  # Electron mass
kin = (3 * h**2 / (40 * np.pi**2 * me)) * (3/np.pi)**(2/3)
e = 1.602176634e-19  # Elementary charge

# Potential energy due to the nucleus
def nuclear_potential(r, Z):
    return -Z * e**2 / r

# Potential energy due to electron-electron repulsion
def electron_potential(r, n):
    epsilon = 1e-10  # Small epsilon value
    return 0.5 * e**2 * np.trapz(n / (np.abs(r[:, None] - r) + epsilon), r)

# Solve the Thomas-Fermi equation
def solve_thomas_fermi(r, Z):
    # Initial guess for electron density
    n = np.ones_like(r)

    # Iterate until convergence
    while True:
        V = nuclear_potential(r, Z) + electron_potential(r, n)
        mu = (5/3) * kin * n**(2/3)
        n_new = thomas_fermi_density(r, mu, V)
        
        # Check convergence
        if np.allclose(n, n_new):
            break
        
        n = n_new
    
    return n

# Range of radial values
r = np.linspace(0.01, 10, 100)

# Atomic number of the nucleus
Z = 1

# Solve Thomas-Fermi equation
n = solve_thomas_fermi(r, Z)

# Plot the electron density
plt.plot(r, n)
plt.xlabel('Radius (r)')
plt.ylabel('Electron Density (n)')
plt.title('Thomas-Fermi Model')
plt.show()
