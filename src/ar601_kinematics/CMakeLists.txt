cmake_minimum_required(VERSION 2.8.3)
project(ar601_kinematics)

find_package(catkin REQUIRED COMPONENTS roscpp std_msgs message_generation)
find_package(cmake_modules REQUIRED)
find_package(Eigen REQUIRED)
#find_package(PkgConfig)
#pkg_search_module(Eigen3 REQUIRED eigen3)

add_service_files(
  FILES
  IK.srv
  FK.srv
  )

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  INCLUDE_DIRS include
  )

include_directories(include ${catkin_INCLUDE_DIRS} ${EIGEN_INCLUDE_DIRS})
add_definitions(${EIGEN_DEFINITIONS})
add_executable(ar601_ikinematics_node src/iservice.cpp
  )

add_executable(ar601_fkinematics_node src/fservice.cpp
  )

add_dependencies(ar601_ikinematics_node ar601_kinematics_gencpp)
add_dependencies(ar601_fkinematics_node ar601_kinematics_gencpp)

target_link_libraries(ar601_ikinematics_node ${catkin_LIBRARIES})
target_link_libraries(ar601_fkinematics_node ${catkin_LIBRARIES})
