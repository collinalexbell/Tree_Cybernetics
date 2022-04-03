#include<iostream>
#include<string>
using namespace std;

struct Target_Revenue {
  Target_Revenue(int dollars, string earn_by): dollars(dollars), earn_by(earn_by){}
  int dollars;
  string earn_by;
};

class Tree_Cybernetics {
  Target_Revenue *init_capital = NULL;
  public: 
  Tree_Cybernetics() {
    cout << "Booting Tree_Cybernetics" << endl;
  }
  void set_init_capital(int dollars, string earn_by) {
    init_capital = new Target_Revenue(
        dollars,
        earn_by
        );
  }
  ~Tree_Cybernetics() {
    delete init_capital;
  }
  void where_are_we_going() {
    cout << init_capital->dollars << "$ by " << init_capital->earn_by << endl;
  }
};



int main() {
  string user = "kuberlog";
  std::cout << "Tree_Cybernetics" << std::endl;
  Tree_Cybernetics kuberlogs_company;
  kuberlogs_company.set_init_capital(
      120000,"2022-04-30"
      );

  kuberlogs_company.where_are_we_going();
}
