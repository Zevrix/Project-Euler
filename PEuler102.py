triangles = []

n = 0

f = open("p102_triangles.txt")

lines = f.read().split('\n')

for line in lines[:-1]:
    coords = line.split(',')
    coord_list = [(int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3])), (int(coords[4]), int(coords[5]))]
    triangles.append(coord_list)

for t in triangles:
    alpha = ((t[1][1] - t[2][1])*(0 - t[2][0]) + (t[2][0] - t[1][0])*(0 - t[2][1]))/((t[1][1] - t[2][1])*(t[0][0] - t[2][0]) + (t[2][0] - t[1][0])*(t[0][1] - t[2][1]))
    beta = ((t[2][1] - t[0][1])*(0 - t[2][0]) + (t[0][0] - t[2][0])*(0- t[2][1])) / ((t[1][1] - t[2][1])*(t[0][0] - t[2][0]) + (t[2][0] - t[1][0])*(t[0][1] - t[2][1]))
    gamma = 1 - alpha - beta
    if gamma > 0 and alpha > 0 and beta > 0:
        n += 1

# used barycentric coordinates
