import copy
import openmesh as om
import numpy as np

def getVisibleFaces(mesh, VRP, P):
	visibleMesh = copy.deepcopy(mesh)

	#calculate n
	n = VRP-P
	norm = np.linalg.norm(n)

	if norm == 0:
		print("WARNING: norm == 0")
	else:
		n = n / norm

	#check wich faces are not visible and delete them
	for fh in visibleMesh.faces():
		faceNormal = np.sum(visibleMesh.calc_face_normal(fh)*n)
		if faceNormal <= 0:
			visibleMesh.delete_face(fh)

	#call garbage collector
	visibleMesh.garbage_collection()

	return visibleMesh
