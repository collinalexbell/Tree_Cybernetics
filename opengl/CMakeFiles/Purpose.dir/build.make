# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kuberlog/Tree_Cybernetics/opengl

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kuberlog/Tree_Cybernetics/opengl

# Include any dependencies generated for this target.
include CMakeFiles/Purpose.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Purpose.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Purpose.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Purpose.dir/flags.make

CMakeFiles/Purpose.dir/Purpose.cpp.o: CMakeFiles/Purpose.dir/flags.make
CMakeFiles/Purpose.dir/Purpose.cpp.o: Purpose.cpp
CMakeFiles/Purpose.dir/Purpose.cpp.o: CMakeFiles/Purpose.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kuberlog/Tree_Cybernetics/opengl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Purpose.dir/Purpose.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Purpose.dir/Purpose.cpp.o -MF CMakeFiles/Purpose.dir/Purpose.cpp.o.d -o CMakeFiles/Purpose.dir/Purpose.cpp.o -c /home/kuberlog/Tree_Cybernetics/opengl/Purpose.cpp

CMakeFiles/Purpose.dir/Purpose.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Purpose.dir/Purpose.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kuberlog/Tree_Cybernetics/opengl/Purpose.cpp > CMakeFiles/Purpose.dir/Purpose.cpp.i

CMakeFiles/Purpose.dir/Purpose.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Purpose.dir/Purpose.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kuberlog/Tree_Cybernetics/opengl/Purpose.cpp -o CMakeFiles/Purpose.dir/Purpose.cpp.s

# Object files for target Purpose
Purpose_OBJECTS = \
"CMakeFiles/Purpose.dir/Purpose.cpp.o"

# External object files for target Purpose
Purpose_EXTERNAL_OBJECTS =

Purpose: CMakeFiles/Purpose.dir/Purpose.cpp.o
Purpose: CMakeFiles/Purpose.dir/build.make
Purpose: CMakeFiles/Purpose.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kuberlog/Tree_Cybernetics/opengl/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Purpose"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Purpose.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Purpose.dir/build: Purpose
.PHONY : CMakeFiles/Purpose.dir/build

CMakeFiles/Purpose.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Purpose.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Purpose.dir/clean

CMakeFiles/Purpose.dir/depend:
	cd /home/kuberlog/Tree_Cybernetics/opengl && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kuberlog/Tree_Cybernetics/opengl /home/kuberlog/Tree_Cybernetics/opengl /home/kuberlog/Tree_Cybernetics/opengl /home/kuberlog/Tree_Cybernetics/opengl /home/kuberlog/Tree_Cybernetics/opengl/CMakeFiles/Purpose.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Purpose.dir/depend

