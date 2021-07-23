import openmesh as om
import numpy as np
from math import sin, cos, pi
import sys

def salvaPoligono(raioBase, raioTopo, nLados, altura, GC = [0,0,0]):
	angleSpacing = 2*pi/nLados
	currRad = 0
	mesh = om.TriMesh()
	vHandle = []

	#add all vertices to vHandle
	for i in range(nLados):
		vHandle.append(mesh.add_vertex(np.array([
			GC[0] + (cos(currRad) * raioTopo),
			GC[1] + altura/2,
			GC[2] + (sin(currRad) * raioTopo)
			])))
		vHandle.append(mesh.add_vertex(np.array([
			GC[0] + (cos(currRad) * raioBase),
			GC[1] - altura/2,
			GC[2] + (sin(currRad) * raioBase)
			])))

		currRad	+= angleSpacing

	if 'debug_vertices_insertion' in sys.argv:
		for j in vHandle:
			i = mesh.point(j)
			print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")
		print()

	faceHandler = []
	lenVHandle = len(vHandle)

	#calculation geometric centre of base and top to construct base and top w/ triangular faces
	CG_topo = mesh.add_vertex(np.array([
			GC[0] + 0,
			GC[1] + altura/2,
			GC[2] + 0
			]))

	CG_base = mesh.add_vertex(np.array([
			GC[0] + 0,
			GC[1] - altura/2,
			GC[2] + 0
			]))

	#create lateral faces
	for i in range(0, lenVHandle, 2):

		if 'debug_face_insertion' in sys.argv:
			print(f"Adding face with vertices:")
			po = mesh.point(vHandle[(i)%lenVHandle])
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
			po = mesh.point(vHandle[(i+2)%lenVHandle])
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
			po = mesh.point(vHandle[(i+1)%lenVHandle])
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
			print()

		face_vhandles = []
		face_vhandles.append(vHandle[(i)%lenVHandle])
		face_vhandles.append(vHandle[(i+2)%lenVHandle])
		face_vhandles.append(vHandle[(i+1)%lenVHandle])
		mesh.add_face(face_vhandles)

		if 'debug_face_insertion' in sys.argv:
			print(f"Adding face with vertices:")
			po = mesh.point(vHandle[(i+1)%lenVHandle])
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
			po = mesh.point(vHandle[(i+2)%lenVHandle])
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
			po = mesh.point(vHandle[(i+3)%lenVHandle])
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
			print()

		face_vhandles = []
		face_vhandles.append(vHandle[(i+1)%lenVHandle])
		face_vhandles.append(vHandle[(i+2)%lenVHandle])
		face_vhandles.append(vHandle[(i+3)%lenVHandle])
		mesh.add_face(face_vhandles)

		#create base and top faces
		face_vhandles = [CG_topo]
		face_vhandles.append(vHandle[(i+2)%lenVHandle])
		face_vhandles.append(vHandle[i])
		mesh.add_face(face_vhandles)
		
		face_vhandles = [CG_base]
		face_vhandles.append(vHandle[i+1])
		face_vhandles.append(vHandle[(i+3)%lenVHandle])
		mesh.add_face(face_vhandles)

	om.write_mesh(mesh=mesh, filename="polygon.ply")

salvaPoligono(20, 1, 40000, 40)