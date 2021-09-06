import numpy as np
import openmesh as om
from math import ceil

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

	print()
	print(VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n)

	GC = faceGeometricCenter(mesh, faceHandler)
	
	#iluminação ambiente
	iA = lAmbiente*kA

	#iluminação difusa
	N = mesh.calc_face_normal(faceHandler)
	L = (lPontualCord - GC)/np.linalg.norm(lPontualCord - GC)
	N_dot_L = np.dot(N,L)

	if N_dot_L <= 0:
		#print(f'amb: {np.append(iA,1)}')
		return np.append(iA,1)

	iD = lPontual*kD*N_dot_L

	#iluminação especular
	R =np.dot(2*np.dot(L,N),N)-L
	S = (VRP-GC)/np.linalg.norm(VRP-GC)
	R_dot_S = np.dot(R,S)

	if R_dot_S <= 0:
		#print(f'a+d: {np.append(iA+iD,1)}')
		return np.append(iA+iD,1)

	iE = lPontual*kS*(R_dot_S**n)

	#print(f'all: {np.append(iA+iD+iE,1)}')
	return np.append(iA+iD+iE,1)

def applyConstantShading(mesh, VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n):

	for fh in mesh.faces():
		#print(constantShading(mesh, fh, VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n))
		color = constantShading(mesh, fh, VRP, lAmbiente, lPontual, lPontualCord, kA, kD, kS, n)
		color = np.clip(color,0,255)
		mesh.set_color(fh, color)

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