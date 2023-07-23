import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import Compose, ToTensor, Normalize
from torchvision.utils import make_grid
import matplotlib.pyplot as plt

# 0) Prepare data
transform = Compose([ToTensor(), Normalize(mean=(0.5,), std=(0.5,))])

train_dataset = MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = MNIST(root='./data', train=False, download=True, transform=transform)

# Create DataLoader
batch_size = 64
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size)

# 1) Model
class Model(nn.Module):
    def __init__(self, n_input_features):
        super(Model, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

model = Model(train_dataset[0][0].numel())

# 2) Loss and optimizer
num_epochs = 10
learning_rate = 0.01
criterion = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# 3) Training loop
for epoch in range(num_epochs):
    for inputs, labels in train_loader:
        inputs = inputs.view(inputs.size(0), -1)  # flatten the input images
        labels = labels.unsqueeze(1).float()  # reshape labels to match output size
        # Forward pass and loss
        y_pred = model(inputs)
        loss = criterion(y_pred, labels)

        # Backward pass and update
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 1 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')

# Evaluate on the test dataset
with torch.no_grad():
    total = 0
    correct = 0
    for inputs, labels in test_loader:
        inputs = inputs.view(inputs.size(0), -1)  # flatten the input images
        labels = labels.unsqueeze(1).float()  # reshape labels to match output size
        outputs = model(inputs)
        predicted = torch.round(outputs)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    accuracy = correct / total
    print(f'Test accuracy: {accuracy:.4f}')

# Visualize some predictions
examples = iter(test_loader)
example_data, example_targets = examples.next()

model.eval()
with torch.no_grad():
    example_data = example_data.view(example_data.size(0), -1)  # flatten the input images
    example_predictions = torch.round(model(example_data))

plt.figure(figsize=(12, 6))
plt.imshow(make_grid(example_data[:12], nrow=6).permute(1, 2, 0))
plt.title('Actual: ' + str(example_targets[:12]) + ' Predicted: ' + str(example_predictions[:12]))
plt.axis('off')
plt.show()
