import torch
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
torch.manual_seed(42)

# Define the grid parameters
number_points = 100
r_min, r_max = 0.5, 5.0
grid = torch.linspace(r_min, r_max, number_points)

# Updated potential function to handle tensors
def potential(r):
    return -torch.div(1.0, r.unsqueeze(-1))

# Define the Hartree-Fock solver
def hartree_fock(grid, potential, num_electrons, max_iterations=100, convergence_threshold=1e-4):
    num_points = grid.size(0)
    num_basis_funcs = num_points  # Assuming one basis function per grid point
    basis_funcs = torch.eye(num_basis_funcs)  # Initial guess for the basis functions
    interaction = torch.zeros(num_points) # Initialize the interaction tensor


    for _ in range(max_iterations):
        old_basis_funcs = basis_funcs.clone()

        # Calculate the electron-electron interaction term
        for i in range(num_points):
            for j in range(num_points):
                r_ij = torch.abs(grid[j] - grid[i])
                interaction[i] += (basis_funcs[j] * basis_funcs[i] * potential(r_ij)).squeeze()

        # Construct the Fock matrix
        fock = torch.zeros((num_basis_funcs, num_basis_funcs))
        for i in range(num_basis_funcs):
            for j in range(num_basis_funcs):
                r_ij = torch.abs(grid[j] - grid[i])
                fock[i, j] = 2 * basis_funcs[j] * basis_funcs[j] * potential(r_ij) + interaction[i]

        try:
            energies, eigenvectors = torch.linalg.eigh(fock, UPLO='U')
        except torch.linalg.LinAlgError as e:
            print(f"Eigenvalue computation failed: {e}")
            return None, None

        # Update the basis functions
        basis_funcs = eigenvectors[:, :num_electrons]

        # Check convergence
        if torch.norm(basis_funcs - old_basis_funcs) < convergence_threshold:
            break

    return energies[:num_electrons], basis_funcs

# Define the main function
def main():
    num_electrons = 2
    energies, basis_funcs = hartree_fock(grid, potential, num_electrons)

    if energies is not None and basis_funcs is not None:
        print(f"Ground state energy: {energies[0]}")

        # Plot the ground state wavefunction
        wavefunctions = basis_funcs.t().numpy()
        for i, wavefunction in enumerate(wavefunctions):
            plt.plot(grid.numpy(), wavefunction, label=f"Electron {i+1}")

        plt.xlabel("Distance")
        plt.ylabel("Wavefunction")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
