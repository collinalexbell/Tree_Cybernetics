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
# For Windows: Prevent overriding the parent project's compiler/linker
# settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

add_executable(-tree- tree.cpp)
add_executable(meditate meditate.cpp)
add_executable(break break.cpp)
add_executable(http http.cpp)
add_executable(kcc kcc.cpp)
add_executable(Treelon Treelon.cpp 3d.cpp glad/glad.c)
add_executable(Cyborg Cyborg.cpp)
add_executable(Empire Empire.cpp)
add_executable(Alpha Alpha.cpp)
add_executable(Purpose Purpose.cpp)
add_executable(space_clean space_clean.cpp)
add_executable(test_space_clean test_space_clean.cpp)
target_link_libraries(test_space_clean gtest_main)
include(GoogleTest)
gtest_discover_tests(test_space_clean)
target_include_directories(Treelon PUBLIC "./glad")
target_link_libraries(Treelon GL glfw X11 Xrandr Xi dl)
target_compile_features(kcc PRIVATE cxx_std_17)
target_link_libraries(http PRIVATE cpr::cpr)
