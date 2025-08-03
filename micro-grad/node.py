from pyClass import Value  # your Value class
from Visualize import draw_dot  # your Graphviz function

p = Value(9, label='p')
q = Value(3, label='q')
g = Value(2, label='g')
m = p + q
f = m * g
m.label = 'm'
f.label = 'f'
dot = draw_dot(f)
dot.render('graph')  # generates graph.png

print("Everything is set up! Check the graph.png file for the visualization.")