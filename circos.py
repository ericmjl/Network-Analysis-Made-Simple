import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import math

from matplotlib.path import Path

class CircosPlot(object):
	def __init__(self, nodes, edges, radius, nodecolor='black', figsize=(8,8), ax=None, fig=None):
		self.nodes = nodes # List of nodes without attributes
		self.edges = edges # List of edges without attributes
		self.nodecolor = nodecolor
		self.radius = radius
		if fig == None:
			self.fig = plt.figure(figsize=figsize)
		else:
			self.fig = fig
		if ax == None:
			self.ax = self.fig.add_subplot(111)
		else:
			self.ax = ax
		self.node_radius = self.radius*0.05
		self.ax.set_xlim(-radius*1.05, radius*1.05)
		self.ax.set_ylim(-radius*1.05, radius*1.05)
		self.ax.xaxis.set_visible(False)
		self.ax.yaxis.set_visible(False)
		for k in self.ax.spines.keys():
			self.ax.spines[k].set_visible(False)


	def draw(self):
		self.add_nodes()
		self.add_edges()

	def add_nodes(self):
		r = self.radius
		node_r = self.node_radius
		for node in self.nodes:
			theta = self.node_theta(node)
			x, y = get_cartesian(r, theta)
			node_patch = patches.Ellipse((x,y), node_r, node_r, facecolor=self.nodecolor, lw=0)
			self.ax.add_patch(node_patch)


	def draw_edge(self, node1, node2):
		start_theta = self.node_theta(node1)
		end_theta = self.node_theta(node2)
		middle_theta = (start_theta + end_theta)/2.0
		delta_theta = abs(end_theta - start_theta)
		middle_r = self.radius * (1 - delta_theta / np.pi) 

		# verts = [get_cartesian(self.radius, start_theta), get_cartesian(middle_theta, middle_r), get_cartesian(self.radius,end_theta)]
		verts = [get_cartesian(self.radius, start_theta), (0,0), get_cartesian(self.radius,end_theta)]
		codes = [Path.MOVETO, Path.CURVE3, Path.CURVE3]

		path = Path(verts, codes)

		patch = patches.PathPatch(path, lw=1, facecolor='none')
		self.ax.add_patch(patch)


	def node_theta(self, node):
		''' Maps node to Angle '''
		i = self.nodes.index(node)
		theta = i*2*np.pi/len(self.nodes)

		return theta

	def add_edges(self):
		for start, end in self.edges:
			self.draw_edge(start, end)


def get_cartesian(r, theta):
	x = r*np.sin(theta)
	y = r*np.cos(theta)

	return x, y