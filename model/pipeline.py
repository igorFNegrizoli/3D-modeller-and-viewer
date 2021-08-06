import copy
import openmesh as om
import numpy as np

def normalize(n):
	norm = np.linalg.norm(n)

	if norm == 0:
		print("WARNING: norm == 0")
	else:
		n = n / norm

	return n

def getVisibleFaces(mesh, VRP, P):
	#Returns only the visible faces of the mesh

	visibleMesh = copy.deepcopy(mesh)

	n = normalize(VRP - P)

	#check wich faces are not visible and delete them
	for fh in visibleMesh.faces():
		faceNormal = np.sum(visibleMesh.calc_face_normal(fh)*n)
		if faceNormal <= 0:
			visibleMesh.delete_face(fh)

	#call garbage collector
	visibleMesh.garbage_collection()

	return visibleMesh

def sru2src(VRP, P, viewUp=np.array([0,1,0])):
	#returns the SRU to SRC matrix

	n = normalize(VRP - P)

	v = viewUp - (np.sum(viewUp*n)*n)
	v = normalize(v)

	u = np.cross(v, n)

	m = np.eye(4)
	m[0,:3] = u
	m[1,:3] = v
	m[2,:3] = n

	#Optimize multiplication by the translation matrix
	m[0,3] = -np.dot(VRP, u)
	m[1,3] = -np.dot(VRP, v)
	m[2,3] = -np.dot(VRP, n)

	return m
