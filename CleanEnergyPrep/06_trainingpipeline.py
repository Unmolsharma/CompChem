import torch
import torch.nn as nn

x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
Y = torch.tensor([2, 4, 6, 8], dtype=torch.float32)

w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

# Model prediction
def forward(x):
    return w * x

print(f'Prediction before Training: f(5) = {forward(5):.3f}')

# Training
learning_rate = 0.01
n_iters = 100

loss = nn.MSELoss()
optimizer = torch.optim.SGD([w], lr=learning_rate)

for epoch in range(n_iters):
    # Prediction forward pass
    y_pred = forward(x)

    # Loss
    l = loss(Y, y_pred)

    # Gradients = backward pass
    l.backward()  # dl/dw

    # Update weights
    optimizer.step()

    # Zero gradients
    optimizer.zero_grad()

    if epoch % 10 == 0:
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.8f}')

print(f'Prediction after Training: f(5) = {forward(5):.3f}')
