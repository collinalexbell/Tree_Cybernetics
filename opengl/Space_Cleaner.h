#ifndef SPACE_CLEANER_H
#define SPACE_CLEANER_H

#include <istream>
#include <iostream>

class Space_Cleaner {
  std::ostream *command_stream = &std::cout;

public:
  void run() {
    sweep();
    dishes();
  }
  void dishes() {
    *command_stream << "dishes" << std::endl;
  }
  void sweep() {
    *command_stream << "sweep" << std::endl;
  }
  void set_command_stream(std::ostream* s) {
    command_stream = s;
  }
  std::ostream *get_command_stream() {
    return command_stream;
  }
};

#endif
