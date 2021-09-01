import numpy as np
import matplotlib.tri as tri

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
    adjacency_pow = np.eye(n)

    while counter < n**2 - n:
        adjacency_pow = np.matmul(adjacency, adjacency_pow)
        alter = np.logical_and(adjacency_pow != 0, distance_tag == 0)
        adjacency_pow[alter] = 1
        np.fill_diagonal(alter,False)
        distance[alter] = power
        distance_tag[alter] = 1
        counter += str(alter.tolist()).count("True")
        power += 1  
        
    return distance
