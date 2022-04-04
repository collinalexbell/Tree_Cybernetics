#include <iostream>
#include <fstream>
#include <sstream>
#include <unistd.h>

using namespace std;

void goal() {
  ifstream goal_file;
  goal_file.open("definite_purpose");
  stringstream ze_goal;
  ze_goal << goal_file.rdbuf();
  cout << ze_goal.str() << endl;
}

void simulate_neccissary_steps() {
  cout << "Mentally list the neccissary steps to achieve the goal" << endl;
  cout << "Go through each item of the list and simulate doing the task mentally" << endl;
}

void simulate_rise_in_faith() {
  cout << "Everytime I complete a task, I get closer to the goal and the probability that the goal is acheived increases" << endl;
  cout << "This increase in probability can be expreience athentically as a feeling of faith" << endl;
  cout << "Think about what it will be like to finish the next major task and feel the increase in faith it brings" << endl;
}

void simulate_flow() {
  cout << "There is a certian feeling when I am deep in a problem" << endl;
  cout << "Think about a compiler bug where I'm googling feriously to figure it out" << endl;
  cout << "In those moments, time flys and any distraction is overcome as a simple annoyance instead of embraced as an escape" << endl;
  cout << "I need to imagine that I am deep inside a stack and solving a compiler bug" << endl;
  cout << "I need to feel time wiz by and my brain hopping from one task to the next efficiently and effectively" << endl;
}

void simulate_letgo_aka_launch () {
  cout << "Imagine that the Onix products have been prototyped and demo'd" << endl;
  cout << "Imagine the demos that they will produce" << endl;
  cout << "Imagine the Kickstarter page running the demo in the video section" << endl;
  cout << "Imagine the products" << endl;
  cout << "Finally, imagine, pressing Launch and watching the orders roll in" << endl;
}

void simulate_follow_through() {
  cout << "There many applications for Onix" << endl;
  cout << "Think of a new one and watch as I apply Onix to the problem in a live demo" << endl;
  cout << "Think of the demo as taking place in a large park in NYC" << endl;
  cout << "Think of the people in the park and their reaction to the robot" << endl;
  cout << "Think of the excitement one feels watching the video of this experience, like a Casey Neistat vid" << endl;
}

void simulate_success() {
  cout << "Imagine my bank account with the revenue" << endl;
  cout << "Imagine spending the marginal costs" << endl;
  cout << "Imagine my bank account with the profit" << endl;
  cout << "Imagine spending the profits" << endl;
}

void visualize() {
  string nop;
  goal();
  cin >> nop;
  simulate_neccissary_steps();
  cin >> nop;
  simulate_rise_in_faith();
  cin >> nop;
  simulate_flow();
  cin >> nop;
  simulate_letgo_aka_launch();
  cin >> nop;
  simulate_follow_through();
  cin >> nop;
  simulate_success();
  cin >> nop;
}

int main() {
  visualize();
}

/*
<faith>

Probability confidence_of_success() {};
while(finished()) {
  auto probability = confidence_of_success();
  report(probability, cur_state, target);
  sleep(TEST_OF_FAITH_INTERVAL);
}

</faith>

<></><></><></><></><></><></><></><></><></><></>

<autosuggestion>

kuberlogs.routines.add(AutosuggestionRoutine("10MillionCheck"));

class AutosuggestionRoutine {
  Time when;
  Place where;
  Manta what;
}

</autosuggestion>

<></><></><></><></><></><></><></><></><></><></>

<specialized knowledge>

class Ignorance() {};
class Knowledge() {};

class Discovery() {
  Ignorance what_i_didnt_know;
  Knowledge what_i_know_now;
};

class Problem() {
  Discovery solve_problem();
};

</specialized knowledge>

<></><></><></><></><></><></><></><></><></><></>

<imagination>

class IdeaFactory {
  Set theSet;
  Setting theSetting;
  Goal theGoal;

  public:
    Idea generate() {};
    IdeaMetric evaluate(Idea idea) {};
}

</imagination>

<></><></><></><></><></><></><></><></><></><></>

<organized planning>

class Plan {
  vector<string> contingencies;
  Tree<string> tasks;
  vector<Milestone> milestones;
};

</organized planning>

<></><></><></><></><></><></><></><></><></><></>

<decision>
vector<Decision> decisions;
void decision() {
  return follow_through(make_a_decision());
}
</decision>

<></><></><></><></><></><></><></><></><></><></>

<persistence>

enum Emotion {
  VIGOR=0;
}

class Massive_Action_Chain {
  void take_next_action(VIGOR);
};

</persistence>

<></><></><></><></><></><></><></><></><></><></>

<mastermind>

class Mastermind_Alliance {
  void convene();
}

string[] us = {"collin", "amit", "matt"};
auto mastermind = Mastermind_Factory.from_friends(us);

</mastermind>
*/
