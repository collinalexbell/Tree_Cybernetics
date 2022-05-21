cmake_minimum_required(VERSION 3.10)

project(Tree)

find_package(Catch2 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)

set(CMAKE_CXX_STANDARD 20)

include(Catch)
include(FetchContent)
FetchContent_Declare(cpr GIT_REPOSITORY https://github.com/libcpr/cpr.git GIT_TAG 67e12da316754ff3c6c91b50aafb2658438f3c1e) # the commit hash for 1.7.0
FetchContent_MakeAvailable(cpr)

FetchContent_Declare(
    googletest
      URL
      https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
      )
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(Tree_Cybernetics Tree_Cybernetics.cpp)
add_executable(meditate meditate.cpp)
add_executable(Treelon Treelon.cpp 3d.cpp opengl/glad/glad.c)
add_executable(Cyborg Cyborg.cpp)
add_executable(Purpose Purpose.cpp)
target_include_directories(Treelon PUBLIC "./opengl/glad")
target_link_libraries(Treelon GL glfw X11 Xrandr Xi dl)
