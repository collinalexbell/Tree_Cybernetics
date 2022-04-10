#include <iostream>
#include <string>
#include <unistd.h>
#include "./3d.h"

using namespace std;

string get_tree_ascii() {
  string tree = 

"                                  # #### ####                             \n"
"                                ### \/#|### |/####                        \n"
"                               ##\/#/ \||/##/_/##/_#                      \n"
"                             ###  \/###|/ \/ # ###                        \n"
"                           ##_\_#\_\## | #/###_/_####                     \n"
"                          ## #### # \ #| /  #### ##/##                    \n"
"                           __#_--###`  |{,###---###-~                     \n"
"                                     \ }{                                 \n"
"                                      }}{                                 \n"
"                                      }}{                                 \n"
"                                 ejm  {{}                                 \n"
"                                , -=-~{ .-^- _                            \n"
"                                      `}                                  \n"
"                                       {                                  \n";
  return tree;
}

class AsciiShell {
  public:
    AsciiShell() {}
};

class AsciiShellFactory {
  AsciiShell root = AsciiShell();
  bool first_fetch = true;
  void onFirstFetchOfRoot() {
    cout << get_tree_ascii();
    cout << endl << endl << "Welcome to Treelon" << endl;
  }
  public:
    AsciiShell makeShell() {
      if(first_fetch){
        onFirstFetchOfRoot();
        first_fetch = false;
      }
      return root;
    }
};

int main() {
  cout << "main()" << endl;
  unsigned int ms;
  auto shellFactory = AsciiShellFactory();
  usleep(1000000);
  auto shell = shellFactory.makeShell();
  usleep(1000000);
  shell = shellFactory.makeShell();
  init_3d();
}
