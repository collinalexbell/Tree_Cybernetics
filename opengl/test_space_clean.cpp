
#include <gtest/gtest.h>
#include "Space_Cleaner.h"

using namespace std;

// Demonstrate some basic assertions.
TEST(SpaceCleaner, sweep) {
  stringstream io;
  Space_Cleaner c;
  c.set_command_stream(&io);
  c.sweep();
  char command[256];
  io.getline(command, 256);
  EXPECT_STREQ(command, "sweep");
}

// Demonstrate some basic assertions.
TEST(SpaceCleaner, dishes) {
  stringstream io;
  Space_Cleaner c;
  c.set_command_stream(&io);
  c.dishes();
  char command[256];
  io.getline(command, 256);
  EXPECT_STREQ(command, "dishes");
}

TEST(SpaceCleaner, run) {
  stringstream io;
  Space_Cleaner c;
  c.set_command_stream(&io);
  c.run();
  char sweep[256];
  char dishes[256];

  io.getline(sweep, 256);
  io.getline(dishes, 256);
  EXPECT_STREQ(sweep, "sweep");
  EXPECT_STREQ(dishes, "dishes");
}
