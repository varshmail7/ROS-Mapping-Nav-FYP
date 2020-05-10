#! /usr/bin/env python
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
import rospy
import numpy
import actionlib
import pandas
import numpy as np
from collections import defaultdict
from mybot_description.msg import MapPoint
from mybot_description.msg import NavigateAction, NavigateActionGoal, NavigateActionResult, NavigateResult

path = []
odom_pub = rospy.Publisher('/odom',Odometry,queue_size=10)
df=pandas.read_json("/home/varsh/newmap/newmap.json")
graph = []
    # pub = rospy.Publisher('mybot/currentMapPoint', MapPoint, queue_size=10)

def createAdjacencyMatrix(df):
    l=len(df)

    ar3=[]
    ar2=[]
    r1=[]
    r2=[]
    for i in range(l):
      for j in range(l):
        if(j==i+1):
          x1=df.x[i]
          x2=df.x[j]
          y1=df.y[i]
          y2=df.y[j]
          ed  = ((x1-x2)**2 + (y1-y2)**2)**0.5
          r1.append(ed)
        if(j==i+2):
          x1=df.x[i]
          x2=df.x[j]
          y1=df.y[i]
          y2=df.y[j]
          ed  = ((x1-x2)**2 + (y1-y2)**2)**0.5
          r2.append(ed)

    level1 = np.array(r1)
    level2 = np.array(r2)

    threshold = ((np.sum(level1)/len(r1)) + (np.sum(level2)/len(r2)))/2
    # threshold = 0.0001

    arr = np.zeros([l,l])
    for i in range(l):
      for j in range(l):
          if(i==j):
              arr[i,j] = 0
          else:
            x1=df.x[i]
            x2=df.x[j]
            y1=df.y[i]
            y2=df.y[j]
            ed  = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if(ed>threshold):
                ed = float("Inf")
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

def navigate_client(mapPoint):
    client = actionlib.SimpleActionClient('navigate', NavigateAction)
    rospy.loginfo("Waiting for Server")
    client.wait_for_server()

    send = NavigateActionGoal()
    send.goal.goal_pose.position.x = round(mapPoint.position.x,4)
    send.goal.goal_pose.position.y = round(mapPoint.position.y,4)
    send.goal.goal_pose.position.z = round(mapPoint.position.z,4)
    send.goal.goal_pose.angleOfApproach = mapPoint.angleOfApproach
    send.goal.goal_pose.mapPointID = mapPoint.mapPointID
    # Fill in the goal here
    client.send_goal(send.goal)
    client.wait_for_result()
    return client.get_result()

def find_neighbors(graph,pt):
    neighbors = []
    col = len(graph[0])
    for i in range(col):
        if graph[pt][i] !=float('Inf'):
            neighbors.append(i)
    return neighbors

def df2MapPoint(i,df,steer=0):
    mapPoint = MapPoint()
    mapPoint.position.x = df.x[i]
    mapPoint.position.y = df.y[i]
    mapPoint.position.z = steer
    mapPoint.angleOfApproach = df.angleOfApproach[i]
    mapPoint.mapPointID = df.mapPointID[i]
    return mapPoint

def nav(src,dest):
    g= Graph()
    mapPoint = MapPoint()
    scores =[]
    # Print the solution
    g.dijkstra(graph,src,dest)
    print path
    if len(path)==0:
        return 0
    # pub = rospy.Publisher('mybot/currentImage', Image, queue_size=10)
    for i in path:
        mapPoint = df2MapPoint(i,df)
        print "go to"
        print mapPoint
        result = navigate_client(mapPoint)
        if result.status == 1:
            print "Reached node"
            print mapPoint.mapPointID
            if mapPoint.mapPointID == dest:
                return 1
            # pub.publish(result.goal_image)
        else:
            print "List of neighbors"
            neighbors = find_neighbors(graph,mapPoint.mapPointID)
            for i in neighbors:
                print i
                mapPoint = df2MapPoint(i,df,1)
                result = navigate_client(mapPoint)
                scores.append(result.decision_score)
            maxScore = max(scores)
            nearestNeigbor = neighbors[scores.index(maxScore)]
            if maxScore > 0.65:
                #publish to odom
                mapPoint = df2MapPoint(nearestNeigbor,df)
                odom = rospy.wait_for_message('/odom', Odometry)
                odom.pose.pose.position.x = mapPoint.position.x
                odom.pose.pose.position.y = mapPoint.position.y
                odom_pub.publish(odom)
                src = nearestNeigbor
                nav(src,dest)
            else:
                #find translation bet current image and map point nearestNeigbor & travel there
                mapPoint = df2MapPoint(nearestNeigbor,df)
                print 'I am lost'
                return 0
                # result = navigate_client(mapPoint,1)
                # src = nearestNeigbor
                # nav(src,dest)

if __name__ == '__main__':
    graph = createAdjacencyMatrix(df)
    print graph.shape
    src = input("src: ")
    dest = input("dest: ")
    # Print the solution
    # pub = rospy.Publisher('mybot/currentImage', Image, queue_size=10)
    try:
        rospy.init_node('navigate_client')
        res = nav(src,dest)
        if res==1:
            print "Success!"
        else:
            print "Sorry, no route found"


    except rospy.ROSInterruptException:
        print("program interrupted before completion")
