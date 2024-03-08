from FigureReader import FigureReader
reader01 = FigureReader("input01.txt")
reader02 = FigureReader("input02.txt")
reader03 = FigureReader("input03.txt")

figures01 = reader01.read()
figures02 = reader02.read()
figures03 = reader03.read()


max_area_fig01, max_per_fig1 = reader01.largest(figures01)
max_area_fig02, max_per_fig02 = reader02.largest(figures02)
max_area_fig03, max_per_fig03 = reader03.largest(figures03)

print("input01.txt:")
print("max area:", max_area_fig01)
print("Figure with max perimeter:", max_per_fig1)


print("input02.txt:")
print("max area:", max_area_fig02)
print("max perimeter:", max_per_fig02)

print("input03.txt:")
print("max area:", max_area_fig03)
print("max perimeter:", max_per_fig03)