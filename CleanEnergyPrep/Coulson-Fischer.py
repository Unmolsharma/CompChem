import numpy as np

# Define the basis functions for VBT
def basis_functions(a, b, lambd):
    phi_1 = a + lambd * b
    phi_2 = b + lambd * a
    return phi_1, phi_2

# Calculate the total electronic wavefunction in CF theory
def coulson_fischer_wavefunction(phi_1, phi_2):
    wavefunction = np.abs(phi_1 * np.conj(phi_2)) - np.abs(np.conj(phi_1) * phi_2)
    return wavefunction

# Calculate the expanded CF wavefunction in terms of a and b
def expanded_wavefunction(phi_1, phi_2, lambd):
    term1 = (1 + lambd**2) * (np.abs(phi_1 * np.conj(phi_2)) - np.abs(np.conj(phi_1) * phi_2))
    term2 = 2 * lambd * (np.abs(phi_1 * np.conj(phi_1)) - np.abs(phi_2 * np.conj(phi_2)))
    wavefunction = term1 + term2
    return wavefunction

# Calculate the full VBT description of the wavefunction
def full_vbt_wavefunction(phi_1, phi_2, epsilon, mu):
    term1 = epsilon * (np.abs(phi_1 * np.conj(phi_2)) - np.abs(np.conj(phi_1) * phi_2))
    term2 = mu * (np.abs(phi_1 * np.conj(phi_1)) - np.abs(phi_2 * np.conj(phi_2)))
    wavefunction = term1 + term2
    return wavefunction

# Example usage
a = np.array([1, 0])  # Atomic 1s orbital a
b = np.array([0, 1])  # Atomic 1s orbital b
lambd = 0.5  # Delocalization parameter

# Calculate the basis functions
phi_1, phi_2 = basis_functions(a, b, lambd)

# Calculate the Coulson-Fischer wavefunction
cf_wavefunction = coulson_fischer_wavefunction(phi_1, phi_2)

# Calculate the expanded wavefunction in terms of a and b
expanded_wavefunction = expanded_wavefunction(phi_1, phi_2, lambd)

# Calculate the full VBT wavefunction
epsilon = 0.8
mu = 0.2
vbt_wavefunction = full_vbt_wavefunction(phi_1, phi_2, epsilon, mu)

# Print the results
print("Coulson-Fischer wavefunction:", cf_wavefunction)
print("Expanded wavefunction:", expanded_wavefunction)
print("Full VBT wavefunction:", vbt_wavefunction)
