
all: Holon_Factory.exe Tree_Cybernetics.exe
Holon_Factory.exe: Holon_Factory/Holon_Factory.cpp
	g++ Holon_Factory/Holon_Factory.cpp -o Holon_Factory.exe
Tree_Cybernetics.exe: Tree_Cybernetics.cpp
	g++ Tree_Cybernetics.cpp -o Tree_Cybernetics.exe -Wfatal-errors

