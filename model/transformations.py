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

def getGeometricCenter(mesh):
	maxCoord = np.copy(mesh.point(next(mesh.vertices())))
	minCoord = np.copy(maxCoord)

	for vh in mesh.vertices():
		coord = mesh.point(vh)

		if coord[0] < minCoord[0]: minCoord[0] = coord[0]
		if coord[1] < minCoord[1]: minCoord[1] = coord[1]
		if coord[2] < minCoord[2]: minCoord[2] = coord[2]
		if coord[0] > maxCoord[0]: maxCoord[0] = coord[0]
		if coord[1] > maxCoord[1]: maxCoord[1] = coord[1]
		if coord[2] > maxCoord[2]: maxCoord[2] = coord[2]

	return np.array([
		(maxCoord[0] + minCoord[0])/2,
		(maxCoord[1] + minCoord[1])/2,
		(maxCoord[2] + minCoord[2])/2
		])

def rotX(meshIn, angle):

	GC = getGeometricCenter(meshIn)
	mesh = translate(meshIn, -GC[0], -GC[1], -GC[2])

	for vh in mesh.vertices():
		coord = np.copy(mesh.point(vh))
		mesh.point(vh)[1] = coord[1]*cos(angle) - coord[2]*sin(angle)
		mesh.point(vh)[2] = coord[1]*sin(angle) + coord[2]*cos(angle)
		coord = mesh.point(vh)

	return translate(mesh, GC[0], GC[1], GC[2])

def rotY(meshIn, angle):

	GC = getGeometricCenter(meshIn)
	mesh = translate(meshIn, -GC[0], -GC[1], -GC[2])

	for vh in mesh.vertices():
		coord = np.copy(mesh.point(vh))
		mesh.point(vh)[0] = coord[0]*cos(angle) + coord[2]*sin(angle)
		mesh.point(vh)[2] = coord[2]*cos(angle) - coord[0]*sin(angle)

	return translate(mesh, GC[0], GC[1], GC[2])	

def rotZ(meshIn, angle):

	GC = getGeometricCenter(meshIn)
	mesh = translate(meshIn, -GC[0], -GC[1], -GC[2])
	
	for vh in mesh.vertices():
		coord = np.copy(mesh.point(vh))
		mesh.point(vh)[0] = coord[0]*cos(angle) - coord[1]*sin(angle)
		mesh.point(vh)[1] = coord[0]*sin(angle) + coord[1]*cos(angle)

	return translate(mesh, GC[0], GC[1], GC[2])