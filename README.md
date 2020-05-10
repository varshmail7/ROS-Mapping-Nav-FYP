# FYP-Robot
# SETTING UP THE PACKAGES  
1.Download the folders and place it in your catkin workspace. If you don't have one pls refer here : http://wiki.ros.org/catkin/Tutorials/create_a_workspace  
2. Configure bashrc  
In the home folder, locate the file called .bashrc. If it does not show, press Ctrl+H to see it.
Add the following lines to it. (Assuming your workspace is called mybot_ws)

```
source ~/mybot_ws/devel/setup.bash
export TURTLEBOT3_MODEL=burger
``` 
3. Open terminal and enter:
```
cd ~/mybot_ws
catkin build
```
In case catkin build throws an error, do the following:
```
catkin clean
catkin build
```
OK so now all the packages are set up.  

# Altering the map intervals

Navigate to mybot_control/scripts/CreateMapPoint.py inside the src folder of the workspace  
In line 37:
```
if map_sub.header.stamp.secs-timeRef>2.5:
```
2.5 signifies the time interval between map points. Pls change this number as needed.  

# Setting up Map Folders

1. In the home folder, create a folder called newmap.  
2. Navigate to /mybot_control/launch/mybot_map.launch inside the workspace.  
In line 10:
```
  <node name="image_saver" pkg="image_view" type="image_saver" args="_filename_format:=/home/varsh/newmap/image%04i.jpg" output="screen">
```
Change the path in args to your username instead of varsh.


# MAPPING
Open terminal and enter:
```
roslaunch turtlebot3_gazebo turtlebot3_room3x3.launch
```
 A jail cell type enviroment will open. Ensure that the turtlebot has the camera and not the LIDAR on top of it.  
 
Open another terminal window and enter:
```
roslaunch mybot_control mybot_map.launch
```
Now this will start the image saver and the rosbag recorder that will save the map images and the positions respectively - once the robot starts moving. This will also display the robot keyboard controls. The initial speed will be set to 0.5 linear and 1.0(?) angular.  

Press x to decrease the linear speed to ~0.1 and press c to decrease angular speed to ~0.5.

Now u are all set to drive.

# ACCESSING THE FILES

All the images should be stored in the newmap folder.

To access the map point positions:  
1. Navigate to home folder and go to the folder .ros
2. Locate the bag file stored here. (Will have time & date as its name)
3. Open terminal in this folder and type
```
rosbag info 2020-05...(your bagfile name)
```
Ensure that the number of messages stored is the same as the number of images saved.

# SENDING EMAIL 

pls take printout of bag file and and images and go2 postofice and post them 2 me


  
