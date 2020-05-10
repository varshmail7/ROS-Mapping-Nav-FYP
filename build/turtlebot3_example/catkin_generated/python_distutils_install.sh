#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/varsh/mybot_ws/src/turtlebot3/turtlebot3_example"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/varsh/mybot_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/varsh/mybot_ws/install/lib/python2.7/dist-packages:/home/varsh/mybot_ws/build/turtlebot3_example/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/varsh/mybot_ws/build/turtlebot3_example" \
    "/usr/bin/python2" \
    "/home/varsh/mybot_ws/src/turtlebot3/turtlebot3_example/setup.py" \
    build --build-base "/home/varsh/mybot_ws/build/turtlebot3_example" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/varsh/mybot_ws/install" --install-scripts="/home/varsh/mybot_ws/install/bin"
