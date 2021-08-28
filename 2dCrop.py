def getRegion(point, uMin, uMax, vMin, vMax):
	if point[0] < uMin:
		if point[1] < vMin:
			return 0b1001
		elif point[1] >= vMax:
			return 0b0101
		else:
			return 0b0001
	elif point[0] >= uMax:
		if point[1] < vMin:
			return 0b1010
		elif point[1] >= vMax:
			return 0b0110
		else:
			return 0b0010
	else:
		if point[1] < vMin:
			return 0b1000
		elif point[1] >= vMax:
			return 0b0100
		else:
			return 0b0000

def cutBorder(face, uMin, uMax, vMin, vMax):
	points = face[:]
	points.append(face[0])
	resultPoints = []

	for regionCode in [0b0001, 0b0010, 0b0100, 0b1000]:
		#print('-'*10)
		#print(regionCode)
		#print()
		#print(f'points: {points}')

		points.append(points[0])
		resultPoints = []
		for i in range(len(points)-1):
			v1_code = getRegion(points[i], uMin, uMax, vMin, vMax)
			v2_code = getRegion(points[i+1], uMin, uMax, vMin, vMax)

			if (v1_code & regionCode) and not(v2_code & regionCode):
				newPoint = getNewPoint(points[i], points[i+1], uMin, uMax, vMin, vMax, regionCode)
				resultPoints.append(newPoint)
				resultPoints.append(points[i+1])
				#print(f'FD: {newPoint} {points[i+1]}')

			elif not(v1_code & regionCode) and not(v2_code & regionCode):
				resultPoints.append(points[i+1])
				#print(f'DD: {points[i+1]}')

			elif not(v1_code & regionCode) and (v2_code & regionCode):
				newPoint = getNewPoint(points[i], points[i+1], uMin, uMax, vMin, vMax, regionCode)
				resultPoints.append(newPoint)
				#print(f'DF: {newPoint}')

			elif (v1_code & regionCode) and (v2_code & regionCode): continue

			else: print("Error happened at cutLeft")

		#print()
		#print(f'resultPoints: {resultPoints}')
		if resultPoints == []: return []
		points = resultPoints[:]

	return resultPoints

def getNewPoint(p1, p2, uMin, uMax, vMin, vMax, regionCode):

	if regionCode == 0b0001:
		x = uMin
		prop = (x - p1[0])/(p2[0]-p1[0])
		y = p1[1] + prop*(p2[1]-p1[1])
		return [x,y]

	elif regionCode == 0b0010:
		x = uMax
		prop = (x - p1[0])/(p2[0]-p1[0])
		y = p1[1] + prop*(p2[1]-p1[1])
		return [x,y]

	elif regionCode == 0b0100:
		y = vMin
		prop = (y - p1[1])/(p2[1]-p1[1])
		x = p1[0] + prop*(p2[0]-p1[0])
		return [x,y]

	elif regionCode == 0b1000:
		y = vMax
		prop = (y - p1[1])/(p2[1]-p1[1])
		x = p1[0] + prop*(p2[0]-p1[0])
		return [x,y]

	else: print("Error happened at getNewPoint")


if __name__ == '__main__':
	uMin = 0
	vMin = 0
	uMax = 240
	vMax = 240

	#points = [[-1, -1], [0, -1], [240, -1], [-1, 0], [0, 0], [240, 0], [-1, 240], [0, 240], [240, 240]]

	#for i in points:
	#	print(getRegion(i, uMin, uMax, vMin, vMax))

	#cutLeft([[-10,10], [10,5], [10,15]], uMin, uMax, vMin, vMax)
	#if (0b1001 & 0b0001) and not(0b0010 & 0b0001):
	#	print("TOP")
	vertices = [[-10, 10], [-15, 5], [-10, 8]]
	print(vertices)
	print(cutBorder(vertices, uMin, uMax, vMin, vMax))