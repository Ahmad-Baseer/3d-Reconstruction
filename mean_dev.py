import json
import numpy as np
from scipy.spatial import distance

with open("euclidean_distances.json", "r") as file:
        data = json.load(file)

# Extract shot_distances and vector_distances
shot_distances = data[0]["shot_distances"]
vector_distances = data[1]["vector_distances"]

# Calculate ratios
ratios = []
# for key in shot_distances:
#     shot_dist = shot_distances[key]
#     # Extracting the index of the shot from the key
#     shot_index = int(key.split('-')[0].split('.')[0])
#     # Generating the corresponding key for the vector_distances
#     vector_key = f"{shot_index - 1}-{shot_index}"
#     vector_dist = vector_distances[vector_key]
#     ratio = shot_dist / vector_dist
#     ratios.append(ratio)
#     print("RATIO:", ratios)
for i in range(1, len(shot_distances) + 1):
    key_shot = "{:02d}.jpg-{:02d}.jpg".format(i, i + 1)
    key_vector = "{:d}-{:d}".format(i - 1, i)
    ratio = shot_distances[key_shot] / vector_distances[key_vector]
    ratios.append(ratio)

# Calculate mean and standard deviation
mean_ratio = np.mean(ratios)
std_dev_ratio = np.std(ratios)

print("Mean of ratios:", mean_ratio)
print("Standard deviation of ratios:", std_dev_ratio)