import torch
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
torch.manual_seed(42)

# Define the grid parameters
num_points = 100
r_min, r_max = 0.5, 5.0
grid = torch.linspace(r_min, r_max, num_points)

# Updated potential function to handle tensors
def potential(r):
    return -torch.div(1.0, r.unsqueeze(-1))

# Define the Fock matrix calculation
def calculate_fock_matrix(grid, potential):
    num_points = grid.size(0)
    fock = torch.zeros((num_points, num_points))

    for i in range(num_points):
        for j in range(num_points):
            r_ij = torch.abs(grid[j] - grid[i])
            fock[i, j] = potential(grid[i]) + 2 * potential(r_ij)

    return fock

# Define the main function
def main():
    fock_matrix = calculate_fock_matrix(grid, potential)

    
    print("Fock matrix:")
    print(fock_matrix)

if __name__ == "__main__":
    main()
