from Triangle import Triangle
from Parallelogram import Parallelogram
from Rectangle import Rectangle
from Trapeze import Trapeze
from Circle import Circle


class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:
                # print(line)
                data = line.split()
                # print(data)
                type = data[0]
                try:
                    if type == "Triangle":
                        a, b, c = [float(el) for el in data[1:]]
                        triangle = Triangle(a, b, c)
                        figures.append(triangle)
                    elif type == "Rectangle":
                        a, b = [float(el) for el in data[1:]]
                        rectangle = Rectangle(a, b)
                        figures.append(rectangle)
                    elif type == "Parallelogram":
                        a, b, h = [float(el) for el in data[1:]]
                        parallelogram = Parallelogram(a, b, h)
                        figures.append(parallelogram)
                    elif type == "Circle":
                        r = float(data[1])
                        circle = Circle(r)
                        figures.append(circle)
                    elif type == "Trapeze":
                        a, b, c, d = [float(el) for el in data[1:]]
                        trapeze = Trapeze(a, b, c, d)
                        figures.append(trapeze)
                except AssertionError:
                # except IOError:
                    pass

        return figures

    @staticmethod
    def largest(figures):
        if not figures:
            return None, None

        max_area = 0
        max_perimeter = 0
        max_area_figure = None
        max_perimeter_figure = None

        for figure in figures:
            area = figure.area()
            perimeter = figure.perimeter()

            if area > max_area:
                max_area = area
                max_area_figure = figure

            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_perimeter_figure = figure

        return max_area_figure, max_perimeter_figure


