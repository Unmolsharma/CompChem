# 1) design model (input, output size,forward pass)
# 2) Construct loss and optimizer
# 3) Training loop
#   - forward pass: compute prediction
#   - backward pass: gradients 
#   - update weights:



import numpy as np


x = np.array([1,2,3,4], dtype=np.float32)
Y = np.array([2,4,6,8], dtype=np.float32)

w = 0.0

#model prediction
def forward(x):
    return w * x

#loss = MSE
def loss(y,y_predicted):
    return ((y_predicted-y)**2).mean()

# gradient
#MSE = 1/N * (w*x-y)**2 < mean squared error formula
# dj/dw = 1/N 2x(w*x-y) < numerical computed derivative
def gradient (x,y,y_predicted):
    return np.dot(2*x, y_predicted-y).mean()

print(f'Prediction before Training: f(5) = {forward(5):.3f}')

#Training
learning_rate = 0.01
n_iters = 10

for epoch in range (n_iters):
    #prediction forward pass
    y_pred = forward(x)


    #loss
    l = loss (Y,y_pred)

    #gradients
    dw = gradient(x,Y,y_pred)

    #update weights
    w -= learning_rate * dw

    if epoch % 1 == 0:
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.8f}')

print(f'Prediction before Training: f(5) = {forward(5):.3f}')

