
all: Holon_Factory.exe Tree_Cybernetics.exe
Tree_Cybernetics.exe: Tree_Cybernetics.cpp
	g++ Tree_Cybernetics.cpp -o Tree_Cybernetics.exe -Wfatal-errors

