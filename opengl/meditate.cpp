#include <stdio.h>
#include <chrono>
#include <thread>
#include <iostream>

int main(int argc, char** argv) {

  int target;
  if(argc < 2) { 
    target = 60 * 10; 
  } else {
    target = strtol(argv[1], NULL, 10);
  }

  int x = 0;
  printf("meditate");
  while(x != target) {
    x++;
    printf(".");
    fflush(stdout);
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }
  printf("\ndone");
}
