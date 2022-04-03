#include <iostream> 
#include <string>
#include <stdlib.h>
#include <chrono>
#include <thread>

using namespace std;

string face(string eye_direction) {

  string eye;
  if(eye_direction == "left") {
    eye = "     .'    '-.(o ) (o ).-'    `.      \n";
  } else if (eye_direction == "right") {
    eye = "     .'    '-.( o) ( o).-'    `.      \n";
  } else if (eye_direction == "stare") {
    eye = "     .'    '-.( o) (o ).-'    `.      \n";
  }
  string top =
"              .'\\   /`.              \n"
"            .'.-.`-'.-.`.             \n"
"       ..._:   .-. .-.   :_...        \n";

//"    .'    '-.(xx) (xx).-'    `.      \n"
  string bottom = 
"    :  _    _ _`~(_)~`_ _    _  :     \n"
"   :  /:   ' .-=_   _=-. `   ;\\  :   \n"
"   :   :|-.._  '     `  _..-|:   :    \n"
"    :   `:| |`:-:-.-:-:'| |:'   :     \n"
"     `.   `.| | | | | | |.'   .'      \n"
"       `.   `-:_| | |_:-'   .'        \n"
"    jgs  `-._   ````    _.-'          \n"
"             ``-------''              \n";

  string footer = 
" ------------------------------------ \n"
"            Yin   ~   Tree.Cyborg     \n"
" ------------------------------------ \n"
" ------------------------------------ \n"
" -----1.  A                  -------- \n"
" -----2.  B                  -------- \n"
" -----3.  C (cyborg,cybernet)-------- \n"
" ------------------------------------ \n"
" ------------------------------------ \n";

  return top + eye + bottom + footer;
}

string left() {
  return face("left");
}

string right() {
  return face("right");
}

string stare() {
  return face("stare");
}

void clear() {
  system("clear");
}

void sleep() {
  std::this_thread::sleep_for(std::chrono::seconds(4));
}

int main() {
  while(true) {
    cout << left() << endl;
    sleep();
    clear();
    cout << right() << endl;
    sleep();
    clear();
    cout << stare() << endl;
    sleep();
    clear();
    cout << right() << endl;
    sleep();
    clear();
  }
}
