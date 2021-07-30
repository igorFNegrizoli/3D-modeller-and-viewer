import openmesh as om
from math import sin, cos
import numpy as np

def translate(mesh, dx=0, dy=0, dz=0):
	for vh in mesh.vertices():
		mesh.point(vh)[0] += dx
		mesh.point(vh)[1] += dy
		mesh.point(vh)[2] += dz
	return mesh

def escalate(mesh, Sx=1, Sy=1, Sz=1):
	for vh in mesh.vertices():
		mesh.point(vh)[0] *= Sx
		mesh.point(vh)[1] *= Sy
		mesh.point(vh)[2] *= Sz
	return mesh

def rotX(mesh, angle):
	for vh in mesh.vertices():
		coord = np.copy(mesh.point(vh))
		mesh.point(vh)[1] = coord[1]*cos(angle) - coord[2]*sin(angle)
		mesh.point(vh)[2] = coord[1]*sin(angle) + coord[2]*cos(angle)
		coord = mesh.point(vh)
	return mesh

def rotY(mesh, angle):
	for vh in mesh.vertices():
		coord = np.copy(mesh.point(vh))
		mesh.point(vh)[0] = coord[0]*cos(angle) + coord[2]*sin(angle)
		mesh.point(vh)[2] = coord[2]*cos(angle) - coord[0]*sin(angle)
	return mesh	

def rotZ(mesh, angle):
	for vh in mesh.vertices():
		coord = np.copy(mesh.point(vh))
		mesh.point(vh)[0] = coord[0]*cos(angle) - coord[1]*sin(angle)
		mesh.point(vh)[1] = coord[0]*sin(angle) + coord[1]*cos(angle)
	return mesh