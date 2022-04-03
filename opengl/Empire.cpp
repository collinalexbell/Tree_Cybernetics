/* Empire.cpp
 * ===========================================================================
 * quined(resume) {
 *
   * Collin Bell->@kuberlog
   * ===========================================================================
   * profession : imperial-cyberneticist
   * aspiration : galactic emperor de le space colony "The Order of Cyberneticians" 
   * vocation   : software engineer = 10X = (80 hour wks + personal software tools)
     *
     * ----------
     * Jobs & Projects
     * ----------
       *
       * =======================================================================
       J  Avise Inc 
       *  >> setting
       *  - Sept 2021 - Now
       *  - company founded by pelaton founder
       *  - accounting startup
       *  >> role
       *  - software engineer
       *  - fullstack Typescript
       *  - React component designer
       *
       * =======================================================================
       J  1904Labs
       *  >> setting
       *  - Jan 2020 - Aug 2021
       *  - St. Louis
       *  >> role
       *  - modern software engineer
       *  - Typescript, Scala, Postgres, AWS
       *  - servant leader of the 
       *    imperial-cyberneticist order {
       *      - teach clases
       *      - do robotics demos
       *      - lecture
       *      - manual labor tasks on campus
       *      - python meetup presentation
       *      - start a corporation and share 
       *        exprience with the labs
       *    }
       *
       * ======================================================================
       P   `sudo` project: https://github.com/sudo-project/sudo
       *    >> setting
       *    - open source
       *    >> role
       *    - contributor
       *    - documentation update only
       *    - pain point with advanced usage required readme update
       *    - look at my contribution in the log
       *      ```
       *      git clone https://github.com/sudo-project/sudo.git 
       *      cd sudo
       *      git log 054939c1e
       *      ```
       * ======================================================================
       p    colli_bell YouTube channel
       *    >> setting
       *    - YouTube
       *    - Reddit Links
       *    - 4Chan
       *    >> role
       *    - producer
       *    - software engineer frontman
       *    - produce open source on stream
       *    - robotics designs
       *    - openscad
       *    - 3d c++
       *    - CLI tools
       *    - Embedded APIs for robotics & cybernetics
       *
     *
   *  }
 */

#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;

int main() {
  int choice;
  cout << "Empire" << endl;
  cout << "   1) Vehicles" << endl;
  cin >> choice;
  if(choice == 1){
    auto fs = fstream("vehicle.txt", fstream::in | fstream::out);
    char txt[1024];
    while(!fs.eof()) {
      fs.getline(txt, 1024);
      cout << txt << endl;
    }
    fs.close();
  } else {
    cout << "choose a valid option" << endl;
    main();
  }
}
