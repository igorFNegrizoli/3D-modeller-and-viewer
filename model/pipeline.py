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

def sru2src(VRP, P=np.array([0,0,0]), viewUp=np.array([0,1,0])):
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

def perspProj(dist):
	#returns the perspective transformation matrix

	m = np.eye(4)
	m[2,2] = 1
	m[3,3] = 0
	m[3,2] = -1/dist

	return m

def persp2srt(width, height, uMin, uMax, vMin, vMax):
	xMin = -width/2
	xMax = width/2

	yMin = -height/2
	yMax = height/2
	#print(xMin, xMax, yMin, yMax)

	m = np.eye(4)
	#print((uMax-uMin)/(xMax-xMin))
	m[0,0] = (uMax-uMin)/(xMax-xMin)
	m[1,1] = (vMin-vMax)/(yMax-yMin)
	m[0,3] = (-xMin*(uMax-uMin)/(xMax-xMin))+uMin
	m[1,3] = (yMin*(vMax-vMin)/(yMax-yMin))+vMax

	return m

def buildPipeline(VRP, dist, width, height, uMin, uMax, 
	vMin, vMax, P=np.array([0,0,0]), viewUp=np.array([0,1,0])):
	
	return np.dot(np.dot(persp2srt(width, height, uMin, uMax, vMin, vMax),
		perspProj(dist)), sru2src(VRP, P, viewUp))

def computeVertices(mesh, pipelineMatrix):
	#pass the copied mesh as parameter not the original one
	for vh in mesh.vertices():
		coord = np.append(copy.deepcopy(mesh.point(vh)),1)
		coord = np.dot(pipelineMatrix, coord)
		mesh.point(vh)[0] = coord[0]/coord[3]
		mesh.point(vh)[1] = coord[1]/coord[3]
		mesh.point(vh)[2] = coord[2]

	return mesh