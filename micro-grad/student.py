from pyClass import Value  # your Value class
from Visualize import draw_dot  # your Graphviz function

p = Value(9, label='p')
q = Value(3, label='q')
expr = ((p + q) * (p - q)) / q

dot = draw_dot(expr)
dot.render('graph')  # generates graph.png
