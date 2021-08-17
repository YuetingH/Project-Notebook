import matplotlib.tri as tri
import numpy as np

def matrixPow(Matrix,n):
    """
    Calculate nth power of matrix
    """
    if(type(Matrix)==list):
        Matrix=np.array(Matrix)
    if(n==1):
        return Matrix
    else:
        return np.matmul(Matrix,matrixPow(Matrix,n-1))

def triplot_distance(xy):
    """
    Measure distance between each pair of points by the number of lines between them under triangulation

    Input: 
        xy: data, [n,2]
    Return: 
        distance: triplot distance between each pair of points, [n,n]
    """
    x = xy[:,0]
    y = xy[:,1]
    n = len(xy)
    triang = tri.Triangulation(x, y) # triang.triangles: store connected points index

    # Construct adjacency matrix
    adjacency = np.zeros(n**2).reshape(n,n).astype(np.int)

    for i in range(len(triang.triangles)):
        for m in range(3):
            for z in range(3):
                if m != z:
                    adjacency[triang.triangles[i,m],triang.triangles[i,z]] = 1

    # Calculate distance
    distance = np.zeros(n**2).reshape(n,n)
    distance_tag = np.zeros(n**2).reshape(n,n)

    power = 1
    counter = 0

    while counter < n**2 - n:
        adjacency_pow = matrixPow(adjacency,power)
        alter = np.logical_and(adjacency_pow != 0, distance_tag == 0)
        np.fill_diagonal(alter,False)
        distance[alter] = power
        distance_tag[alter] = 1
        counter += str(alter.tolist()).count("True")
        power += 1  
    return distance

xy = np.asarray([
	[-0.101, 0.872], [-0.080, 0.883], [-0.069, 0.888], [-0.054, 0.890],
	[-0.045, 0.897], [-0.057, 0.895], [-0.073, 0.900], [-0.087, 0.898],
	[-0.090, 0.904], [-0.069, 0.907], [-0.069, 0.921], [-0.080, 0.919],
	[-0.073, 0.928], [-0.052, 0.930], [-0.048, 0.942], [-0.062, 0.949],
	[-0.054, 0.958], [-0.069, 0.954], [-0.087, 0.952], [-0.087, 0.959],
	[-0.080, 0.966], [-0.085, 0.973], [-0.087, 0.965], [-0.097, 0.965],
	[-0.097, 0.975], [-0.092, 0.984], [-0.101, 0.980], [-0.108, 0.980],
	[-0.104, 0.987], [-0.102, 0.993], [-0.115, 1.001], [-0.099, 0.996],
	[-0.101, 1.007], [-0.090, 1.010], [-0.087, 1.021], [-0.069, 1.021],
	[-0.052, 1.022], [-0.052, 1.017], [-0.069, 1.010], [-0.064, 1.005],
	[-0.048, 1.005], [-0.031, 1.005], [-0.031, 0.996], [-0.040, 0.987],
	[-0.045, 0.980], [-0.052, 0.975], [-0.040, 0.973], [-0.026, 0.968],
	[-0.020, 0.954], [-0.006, 0.947], [ 0.003, 0.935], [ 0.006, 0.926],
	[ 0.005, 0.921], [ 0.022, 0.923], [ 0.033, 0.912], [ 0.029, 0.905],
	[ 0.017, 0.900], [ 0.012, 0.895], [ 0.027, 0.893], [ 0.019, 0.886],
	[ 0.001, 0.883], [-0.012, 0.884], [-0.029, 0.883], [-0.038, 0.879],
	[-0.057, 0.881], [-0.062, 0.876], [-0.078, 0.876], [-0.087, 0.872],
	[-0.030, 0.907], [-0.007, 0.905], [-0.057, 0.916], [-0.025, 0.933],
	[-0.077, 0.990], [-0.059, 0.993]])
x = np.degrees(xy[:, 0])
y = np.degrees(xy[:, 1])

print(triplot_distance(xy))