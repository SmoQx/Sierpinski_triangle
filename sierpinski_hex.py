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
    list_of_points2 = []
    list_of_points3 = []
    list_of_points4 = []
    list_of_points5 = []
    list_of_points6 = []
    fig, ax = plt.subplots()
    points = ((3, 3), (6, 3), (4.5, 6),
              (4.5, 6), (7.5, 6), (6, 3),
              (1.5, 6), (4.5, 6), (3, 3),
              (1.5, 6), (4.5, 6), (3, 9),
              (4.5, 6), (3, 9), (6, 9),
              (4.5, 6), (6, 9), (7.5, 6))
    for point in points:
        plt.scatter(*point, marker="o", s=1)
    first_point = random_point_in_triangle(*points[0:3])
    list_of_points.append(first_point)
    first_point2 = random_point_in_triangle(*points[3:6])
    list_of_points2.append(first_point2)
    first_point3 = random_point_in_triangle(*points[6:9])
    list_of_points3.append(first_point3)
    first_point4 = random_point_in_triangle(*points[9:12])
    list_of_points4.append(first_point4)
    first_point5 = random_point_in_triangle(*points[12:15])
    list_of_points5.append(first_point5)
    first_point6 = random_point_in_triangle(*points[15:18])
    list_of_points6.append(first_point6)

    for generate in range(5000):
        new_point = draw_points(x1=list_of_points[-1][0], y1=list_of_points[-1][1], edge_points=points[0:3])
        list_of_points.append(new_point)
        new_point2 = draw_points(x1=list_of_points2[-1][0], y1=list_of_points2[-1][1], edge_points=points[3:6])
        list_of_points2.append(new_point2)
        new_point3 = draw_points(x1=list_of_points3[-1][0], y1=list_of_points3[-1][1], edge_points=points[6:9])
        list_of_points3.append(new_point3)
        new_point4 = draw_points(x1=list_of_points4[-1][0], y1=list_of_points4[-1][1], edge_points=points[9:12])
        list_of_points4.append(new_point4)
        new_point5 = draw_points(x1=list_of_points5[-1][0], y1=list_of_points5[-1][1], edge_points=points[12:15])
        list_of_points5.append(new_point5)
        new_point6 = draw_points(x1=list_of_points6[-1][0], y1=list_of_points6[-1][1], edge_points=points[15:18])
        list_of_points6.append(new_point6)
    for draw1, draw2, draw3, draw4, draw5, draw6 in zip(list_of_points,
                                                        list_of_points2,
                                                        list_of_points3,
                                                        list_of_points4,
                                                        list_of_points5,
                                                        list_of_points6):
        plt.scatter(*draw1, marker="o", s=1)
        plt.scatter(*draw2, marker="o", s=1)
        plt.scatter(*draw3, marker="o", s=1)
        plt.scatter(*draw4, marker="o", s=1)
        plt.scatter(*draw5, marker="o", s=1)
        plt.scatter(*draw6, marker="o", s=1)
    # ani = animation.FuncAnimation(fig, draw_sierp, frames=len(list_of_points), interval=0.01)
    plt.show()
