import numpy as np
import openmesh as om
from pipeline import normalize

def faceGeometricCenter(mesh, faceHandler):
	maxCoord = np.copy(mesh.point(next(mesh.fv(faceHandler))))
	minCoord = np.copy(maxCoord)

	for vh in mesh.fv(faceHandler):
		point = mesh.point(vh)
		for pos in range(len(point)):
			if point[pos] > maxCoord[pos]: maxCoord[pos] = point[pos]
			if point[pos] < minCoord[pos]: minCoord[pos] = point[pos]

	GC = (maxCoord + minCoord)/2
	return GC

def constantShading(mesh, faceHandler, VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n):

	GC = faceGeometricCenter(mesh, faceHandler)
	
	#iluminação ambiente
	iA = lAmbiente*kA

	#iluminação difusa
	N = mesh.calc_face_normal(faceHandler)
	L = normalize(lPontualCord - GC)
	N_dot_L = np.dot(N,L)

	if N_dot_L <= 0: return iA

	iD = lPontual*kD*N_dot_L

	#iluminação especular
	R =np.dot(2*np.dot(L,N),N)-L
	S = normalize(VRP-GC)
	R_dot_S = np.dot(R,S)

	if R_dot_S <= 0: return iA+iD

	iE = lPontual*kS*(R_dot_S**n)

	return iA+iD+iE

def applyConstantShading(mesh, VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n):

	for fh in meshSRT.faces():
		mesh.set_color(fh, constantShading(mesh, faceHandler, VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n))

if __name__ == '__main__':
	face = [[1,1,0],[2,2,0],[1,2,0]]

	lAmbiente = [120, 120, 120]
	lPontual = [120, 120, 120]
	lPontualCord = [10,10,10]
	kA = [120, 120, 120]
	kD = [120, 120, 120]
	kS = [120, 120, 120]
	n = 2

	constantShading(face, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n)