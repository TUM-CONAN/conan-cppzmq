cmake_minimum_required(VERSION 3.15)
cmake_policy(SET CMP0074 NEW)

project(test_package CXX)
set(CMAKE_VERBOSE_MAKEFILE TRUE)

find_package(cppzmq REQUIRED CONFIG)
find_package(ZeroMQ REQUIRED CONFIG)

ADD_EXECUTABLE(${PROJECT_NAME} test_package.cpp)
TARGET_LINK_LIBRARIES(${PROJECT_NAME} PRIVATE cppzmq::cppzmq ZeroMQ::ZeroMQ)

set_target_properties(${PROJECT_NAME}
    PROPERTIES
    	CXX_STANDARD 11
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF
)