import math

# Function for cumulative distribution function of standard normal
def cdf(x, mean=0, std=1):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

# Given values
mu = 30
sigma = 4

# 1. P(x < 40)
p1 = cdf(40, mu, sigma)

# 2. P(x > 21) = 1 - P(x <= 21)
p2 = 1 - cdf(21, mu, sigma)

# 3. P(30 < x < 35) = P(x < 35) - P(x < 30)
p3 = cdf(35, mu, sigma) - cdf(30, mu, sigma)

# Print results with 3 decimal places
print(f"{p1:.3f}")
print(f"{p2:.3f}")
print(f"{p3:.3f}")
