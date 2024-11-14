import math

def h(x, i, theta):
    return theta[0] + theta[1]*x[i][0] + theta[2]*x[i][1]

# Sigmoid function.
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Cost function (binary cross-entropy loss).
def J(x, theta, y):
    Sum = 0
    epsilon = 1e-15
    m = len(x)
    for i in range(m):
        sig = sigmoid(h(x, i, theta))
        sig = max(min(sig, 1 - epsilon), epsilon)
        Sum += y[i] * math.log(sig) + (1 - y[i]) * math.log(1 - sig)
    return -(Sum / m)

# Derivative of the cost function for a specific theta[j].
def dJ(theta, x, y, j):
    Sum = 0
    m = len(x)
    for i in range(m):
        if j == 0:
            Sum += (sigmoid(h(x, i, theta)) - y[i])  # No x[i][j] for theta[0]
        else:
            Sum += (sigmoid(h(x, i, theta)) - y[i]) * x[i][j-1]  # Adjust index for other theta values
    return Sum / m

# Logistic regression using gradient descent.
def LogReg(x, y, theta):
    learningRate = 0.1
    print("yello welcome to logistic regression thing.")
    minErr = float('inf')
    minthetas = theta[:]
    
    for _ in range(100):
        error = J(x, theta, y)
        if error < minErr:
            minErr = error
            minthetas = theta[:]
        
        # Gradient descent update rule for all theta values.
        for j in range(len(theta)):
            if j == 0:
                # Update for theta[0] (intercept term)
                theta[j] -= learningRate * sum((sigmoid(h(x, k, theta)) - y[k]) for k in range(len(x))) / len(x)
            else:
                # Update for other theta[j] values
                theta[j] -= learningRate * dJ(theta, x, y, j)
            
    return minErr, minthetas


# Dataset
theta = [0.0, 0.0, 0.0]  # Initialize the parameters
x = [
    [10.0, 100.0],  # rent(thousands), income(thousands)
    [5.0, 120.0],
    [12.0, 20.0],
    [5.0, 500.0],
    [50.0, 100.0]
]
y = [1, 1, 0, 1, 0]

# Call the logistic regression function
final_error, final_theta = LogReg(x, y, theta)
print("Final theta values:", final_theta)
print("Final error:", final_error)

print(sigmoid(final_theta[0] + final_theta[1] * 10.0 + final_theta[2] * 100.0))
