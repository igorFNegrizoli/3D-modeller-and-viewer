import openmesh as om
import numpy as np
from math import sin, cos, pi

def salvaPoligono(raioBase, raioTopo, nLados, altura, GC = [0,0,0]):
	angleSpacing = 2*pi/nLados
	currRad = 0
	mesh = om.TriMesh()
	vHandle = []
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

	faceHandler = []

	for i in range(0, len(vHandle)-2, 2):

		#DEBUG
		print(f"Adding face with vertices:")
		po = mesh.point(vHandle[i])
		print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		po = mesh.point(vHandle[i+1])
		print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		po = mesh.point(vHandle[i+2])
		print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		print()

		face_vhandles = []
		face_vhandles.append(vHandle[i])
		face_vhandles.append(vHandle[i+1])
		face_vhandles.append(vHandle[i+2])
		mesh.add_face(face_vhandles)

		#DEBUG
		print(f"Adding face with vertices:")
		po = mesh.point(vHandle[i+1])
		print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		po = mesh.point(vHandle[i+2])
		print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		po = mesh.point(vHandle[i+3])
		print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		print()

		face_vhandles = []
		face_vhandles.append(vHandle[i+1])
		face_vhandles.append(vHandle[i+2])
		face_vhandles.append(vHandle[i+3])
		mesh.add_face(face_vhandles)

	#DEBUG
	print(f"Adding face with vertices:")
	po = mesh.point(vHandle[-2])
	print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
	po = mesh.point(vHandle[-1])
	print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
	po = mesh.point(vHandle[0])
	print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
	print()

	face_vhandles = []
	face_vhandles.append(vHandle[-2])
	face_vhandles.append(vHandle[-1])
	face_vhandles.append(vHandle[0])
	mesh.add_face(face_vhandles)

	#DEBUG
	print(f"Adding face with vertices:")
	po = mesh.point(vHandle[-1])
	print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
	po = mesh.point(vHandle[0])
	print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
	po = mesh.point(vHandle[1])
	print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
	print()

	face_vhandles = []
	face_vhandles.append(vHandle[-1])
	face_vhandles.append(vHandle[0])
	face_vhandles.append(vHandle[1])
	mesh.add_face(face_vhandles)

	#DEBUG
	for j in vHandle:
		i = mesh.point(j)
		print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")

	print()
	print("Vertices in each face:")
	for i in faceHandler:
		for vh in mesh.fv(i):
			po = mesh.point(vh)
			print(f"({po[0]:.3f}, {po[1]:.3f}, {po[2]:.3f})")
		print()
	

	#for i in mesh.points():
	#	print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")
	#print()
	#for j in vHandlersLateral:
	#	i = mesh.point(j[0])
	#	print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")
	#	i = mesh.point(j[1])
	#	print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")
	#	print()
	#for j in vHandlersTopo:
	#	i = mesh.point(j)
	#	print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")
	#print()
	#for j in vHandlersBase:
	#	i = mesh.point(j)
	#	print(f"({i[0]:.3f}, {i[1]:.3f}, {i[2]:.3f})")
	

salvaPoligono(10, 5, 4, 20)