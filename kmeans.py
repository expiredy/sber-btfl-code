import copy
import random

def visualisation_3d(cluster_content):	
	import matplotlib.pyplot as plt
	from mpl_toolkits import mplot3d
	import numpy as np


	ax = plt.axes(projection="3d")
	plt.xlabel("x")    
	plt.ylabel("y")

	k = len(cluster_content)
		
	for i in range(k):
		x_coordinates = []
		y_coordinates = []
		z_coordinates = []
		for q in range(len(cluster_content[i])):
			x_coordinates.append(cluster_content[i][q][0])
			y_coordinates.append(cluster_content[i][q][1])
			z_coordinates.append(cluster_content[i][q][2])
		ax.scatter(x_coordinates, y_coordinates, z_coordinates)
	plt.show()



def run_clusterization(array, k):
	def data_distribution(array, cluster): 
		cluster_content = [[] for i in range(k)]
		for i in range(n):
			min_distance = float('inf')
			situable_cluster = -1
			for j in range(k):
				distance = sum([(array[i][q]-cluster[j][q])**2 for q in range(dim)]) ** 0.5
				if distance < min_distance:
					min_distance = distance
					situable_cluster = j
			cluster_content[situable_cluster].append(array[i])
		return cluster_content

	def cluster_update(cluster, cluster_content, dim):
		k = len(cluster)
		for i in range(k): #по i кластерам
			for q in range(dim): #по q параметрам
				updated_parameter = 0
				for j in range(len(cluster_content[i])): 
					updated_parameter += cluster_content[i][j][q]
				if len(cluster_content[i]) != 0:
					updated_parameter = updated_parameter / len(cluster_content[i])
				cluster[i][q] = updated_parameter
		return cluster
	

	n = len(array)  
	dim = len(array[0])  

	cluster = [[0 for i in range(dim)] for q in range(k)] 
	cluster_content = [[] for i in range(k)] 

	for i in range(dim):
		for q in range(k):
			cluster[q][i] = random.randint(0, max_cluster_value) 

	cluster_content = data_distribution(array, cluster)
	privious_cluster = copy.deepcopy(cluster)
	run_learning = True
	while run_learning:
		cluster = cluster_update(cluster, cluster_content, dim)
		cluster_content = data_distribution(array, cluster)
		run_learning = not (cluster == privious_cluster)	
		privious_cluster = copy.deepcopy(cluster)


if __name__ == "__main__":
	smth = []
	run_clusterization(smth, 3)

