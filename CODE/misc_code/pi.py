import random
import math
import matplotlib.pyplot as plt


# Function to estimate π in multiple dimensions
def estimate_pi(num_points: int, max_dimension: int):
    estimates = {}  # Dictionary to store estimates for each dimension

    for dim in range(2, max_dimension + 1):
        inside_sphere = 0

        for _ in range(num_points):
            # Generate a random point with 'dim' dimensions
            point = [random.random() for _ in range(dim)]

            # Calculate the distance from the origin (hypersphere)
            distance_from_origin = math.sqrt(sum([x**2 for x in point]))

            # Check if the point is inside the unit hypersphere
            if distance_from_origin <= 1:
                inside_sphere += 1

        # Volume ratio to estimate π in different dimensions
        volume_ratio = inside_sphere / num_points

        # Adjust the volume ratio to estimate π
        # In 2D, we multiply by 4, in 3D by 6 (and it generalizes further)
        pi_estimate = volume_ratio * (2**dim)

        # Store the result for the current dimension
        estimates[dim] = pi_estimate

    return estimates


# Parameters
num_points = 100000  # Number of random points per dimension
max_dimension = 18  # Maximum dimension to estimate π for

# Estimate π for each dimension
pi_estimates = estimate_pi(num_points, max_dimension)

# Prepare data for the graph
dimensions = list(pi_estimates.keys())
pi_values = list(pi_estimates.values())

# Plotting the results
plt.figure(figsize=(8, 5))
plt.plot(dimensions, pi_values, marker="o", linestyle="-", color="b")
plt.axhline(y=math.pi, color="r", linestyle="--", label=f"True π = {math.pi:.5f}")
plt.title(f"Estimation of π in 2 to {max_dimension} dimensions")
plt.xlabel("Dimension")
plt.ylabel("Estimated value of π")
plt.xticks(range(2, max_dimension + 1))
plt.legend()
plt.grid(True)
plt.show()
