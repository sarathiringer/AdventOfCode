import numpy as np

with open('input_9.txt') as f:
    inputs = np.array([[int(i) for i in line.strip().split()[0]] for line in f])

padded = np.pad(inputs, 1, 'constant',  constant_values=9)   
nr_rows = padded.shape[0]
nr_cols = padded.shape[1]

low_points = []
for i in range(1,nr_rows-1):
    for j in range(1, nr_cols-1):
        elem = padded[i][j]
        up = padded[i][j-1]
        left = padded[i-1][j]
        right = padded[i+1][j]
        down = padded[i][j+1]
        if elem<left and elem<right and elem<up and elem<down:
            low_points.append(elem)

print("Low points: ", str(low_points))
risk_level = sum(low_points) + len(low_points)
print("Risk level: ", str(risk_level))
        
# Developed together with my awesome friends in EqualitySquad
