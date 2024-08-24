import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def random_unit_vector():
    phi = np.random.uniform(0, 2 * np.pi)
    theta = np.random.uniform(0, np.pi)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])

def generate_random_tube(radius, length=1):
    direction = random_unit_vector()
    center = np.random.uniform(-1, 1, 3) 
    start_point = center - (length / 2) * direction
    end_point = center + (length / 2) * direction
    return start_point, end_point, direction

def tubes_intersect(tube1, tube2, radius):
    start1, end1, dir1 = tube1
    start2, end2, dir2 = tube2
    
    d = start2 - start1
    
    cross_dir = np.cross(dir1, dir2)
    cross_norm = np.linalg.norm(cross_dir)
    
    if cross_norm == 0:
        dist = np.linalg.norm(np.cross(start2 - start1, dir1)) / np.linalg.norm(dir1)
        return dist <= 2 * radius
    
    dist = np.abs(np.dot(d, cross_dir)) / cross_norm
    
    return dist <= 2 * radius

def simulate_kakeya(num_tubes=100, radius=0.05, length=1):
    tubes = [generate_random_tube(radius, length) for _ in range(num_tubes)]
    intersections = 0
    
    for i in range(num_tubes):
        for j in range(i + 1, num_tubes):
            if tubes_intersect(tubes[i], tubes[j], radius):
                intersections += 1
    
    return tubes, intersections

def plot_tubes(tubes, title="Kakeya Conjecture Visualization"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    lines = []
    for tube in tubes:
        start, end, _ = tube
        lines.append([start, end])
    
    lc = Line3DCollection(lines, color='blue')
    ax.add_collection(lc)
    
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    
    ax.set_title(title)
    plt.show()

if __name__ == "__main__":
    num_tubes = int(input("Enter Number of Tubes: "))
    radius = float(input("Enter Radius: "))
    length = int(input("Enter Length: "))
    tubes, intersections = simulate_kakeya(num_tubes=num_tubes, radius=radius, length=length)
    print(f"Number of tubes: {num_tubes}")
    print(f"Number of intersections: {intersections}")
    
    plot_tubes(tubes)
