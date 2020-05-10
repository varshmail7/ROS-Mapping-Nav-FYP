#!/usr/bin/env python

import pandas
import rospy
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from mybot_description.msg import MapPoint

path = []

def createAdjacencyMatrix(df):
    l=len(df)

    ar3=[]
    ar2=[]
    r=0
    r2=0
    r3=0
    for i in range(l-1):
      for j in range(l-1):
        if(j==i+1):
          x1=df.x[i]
          x2=df.x[j]
          y1=df.y[i]
          y2=df.y[j]
          ed  = ((x1-x2)**2 + (y1-y2)**2)**0.5
          r=r+np.sum(ed)
        if(j==i+2):
          x1=df.x[i]
          x2=df.x[j]
          y1=df.y[i]
          y2=df.y[j]
          ed  = ((x1-x2)**2 + (y1-y2)**2)**0.5
          r2=r2+np.sum(ed)
    r=r/l
    r2=r2/l
    r3=(r+r2)/2
    print r3


    arr = np.zeros([l-1,l-1])
    for i in range(l-1):
      for j in range(l-1):
          x1=df.x[i]
          x2=df.x[j]
          y1=df.y[i]
          y2=df.y[j]
          ed  = ((x1-x2)**2 + (y1-y2)**2)**0.5
          if(ed==0 or ed>r3):
              ed = 100
          arr[i,j] = ed
    return arr


#Class to represent a graph
class Graph:

    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self,dist,queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index


    # Function to print shortest path
    # from source to j using parent array
    def printPath(self, parent, j):

        #Base Case : If j is source
        if parent[j] == -1 :
            return
        self.printPath(parent , parent[j])
        path.append(j)


    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent,src,dest):

        # for i in range(1, len(dist)):
        self.printPath(parent,dest)


    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''
    def dijkstra(self, graph, src,dest):

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        #Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)

        #Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist,queue)

            # remove min element
            queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u


        # print the constructed distance array
        self.printSolution(dist,parent,src,dest)


df=pandas.read_json("/home/varsh/mapfile.json")
g= Graph()
pub = rospy.Publisher('mybot/currentMapPoint', MapPoint, queue_size=10)
graph = createAdjacencyMatrix(df)
mapPoint = MapPoint()
src = input("src: ")
dest = input("dest: ")
# Print the solution
g.dijkstra(graph,src,dest)
for i in path:
    mapPoint.position.x = df.x[i]
    mapPoint.position.y = df.y[i]
    mapPoint.position.z = df.z[i]
    mapPoint.angleOfApproach = df.angleOfApproach[i]
    mapPoint.mapPointID = df.mapPointID[i]
    print mapPoint
