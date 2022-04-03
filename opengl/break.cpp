#include <stdio.h>
#include <stdlib.h>
#include <chrono>
#include <thread>

void clear() {
  system("clear");
}

void sleep() {
  std::this_thread::sleep_for(std::chrono::seconds(2));
}


int main(){
  while(true){
    clear();
    printf("\n\n\n\n\n\n\n\n\n");
    printf("  ");
    //printf("             ");
    printf("I am finding a ruler (in fucking metric)\n");
    printf("             ");
    for(int i=0; i<20; i++){
      printf(".");
      fflush(stdout);
      sleep();
    }
    clear();
  }
}
