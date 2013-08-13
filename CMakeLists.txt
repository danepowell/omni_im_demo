cmake_minimum_required(VERSION 2.8.3)
project(omni_im_demo)

find_package(catkin REQUIRED COMPONENTS omni_im)

catkin_package(
  CATKIN_DEPENDS omni_im
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  src/omni_im_demo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

