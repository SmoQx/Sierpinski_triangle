import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation


def draw_points(x1, y1, edge_points):
    random_point = random.choice(edge_points)
    x0, y0 = random_point
    xp = (x0 + x1) / 2
    yp = (y0 + y1) / 2

    return xp, yp


def random_point_in_triangle(p1, p2, p3):
    r1 = random.uniform(0, 1)
    r2 = random.uniform(0, 1)
    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2
    r3 = 1 - r1 - r2
    x = r1 * p1[0] + r2 * p2[0] + r3 * p3[0]
    y = r1 * p1[1] + r2 * p2[1] + r3 * p3[1]

    return x, y


def draw_sierp(frame):
    x, y = list_of_points[frame]
    plt.scatter(x, y, marker='o', s=1)
    print(frame)


if __name__ == '__main__':
    list_of_points = []
    fig, ax = plt.subplots()
    points = ((0, 0), (150, 0), (75, 150))
    for point in points:
        plt.scatter(*point, marker="o", s=1)
    first_point = random_point_in_triangle(*points)
    list_of_points.append(first_point)
    for generate in range(1000):
        new_point = draw_points(x1=list_of_points[-1][0], y1=list_of_points[-1][1], edge_points=points)
        list_of_points.append(new_point)
    """for draw in list_of_points:
        plt.scatter(*draw, marker="o", s=1)"""
    #ani = animation.FuncAnimation(fig, draw_sierp, frames=len(list_of_points), interval=0.01)
    plt.show()
