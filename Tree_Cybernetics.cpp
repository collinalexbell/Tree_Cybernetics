#include<iostream>
#include<string>
#include<vector>
using namespace std;

struct Target_Revenue {
  Target_Revenue(int dollars, string earn_by): dollars(dollars), earn_by(earn_by){}
  int dollars;
  string earn_by;
};

class Product {
  string name;
  string description;
  int unit_revenue;
  int unit_cost;
  int unit_profit;
  public:
  Product(string name, int revenue, int profit) {
    this->name = name;
    unit_revenue = revenue;
    unit_profit = profit;
    unit_cost =  revenue-profit;
  }
  void describe() {
    cout << name << " :\n" << description << endl;
  }
  void add_description(string description){
    this->description = description;
  }
  int sales_to_target(Target_Revenue target) {
    int units_sold = target.dollars/unit_profit;
    return units_sold;
  }
};

struct Goal {
  int wavelength;
  string name;
  string description;
  void show() {
    cout << "{" << endl;
    cout << "  name: " << name << endl;
    cout << "  description: " << description << endl;
    cout << "  wavelength: " << wavelength << endl;
    cout << "}" << endl;
  }

};

class Tree_Cybernetics {
  Target_Revenue *init_capital = NULL;
  Product *init_product = NULL;
  vector<Goal> goals;
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

  void set_init_product(string name, string description, int revenue, int profit) { 
    init_product = new Product(name, revenue, profit);
    init_product->add_description(description);
  }
  ~Tree_Cybernetics() {
    delete init_capital;
    delete init_product;
  }
  
  void where_are_we_going() {
    cout << init_capital->dollars << "$ by " << init_capital->earn_by << endl;
  }

  void add_goal() {
    Goal goal;
    cout << "----------------------------------------" << endl;
    cout << " Add a goal " << endl;
    cout << "----------------------------------------" << endl;
    cout << "  name: ";
    cin >> goal.name;
    cout << "----------------------------------------" << endl;
    cout << "  description: ";
    cin >> goal.description;
    cout << "----------------------------------------" << endl;
    cout << "  wavelength (in seconds): ";
    cin >> goal.wavelength;
    cout << "----------------------------------------" << endl;
    goals.push_back(goal);
    goal.show();
  }

  void run_menu() {
    string choice;
    cout << "1) Where are we going?" << endl;
    cout << "2) Sales to target?" << endl;
    cout << "3) Describe the product" << endl;
    cout << "4) Add Goal" << endl;
    cin >> choice;
    if(choice == "1"){
      where_are_we_going();
    }
    if(choice == "2"){
      cout << init_product->sales_to_target(*init_capital) << endl;
    }
    if(choice == "3"){
      init_product->describe();
    }
    if(choice == "4"){
      add_goal();
    }
  }
};



int main() {
  string user = "kuberlog";
  std::cout << "Tree_Cybernetics" << std::endl;
  Tree_Cybernetics kuberlogs_company;
  kuberlogs_company.set_init_capital(
      120000,"2022-09-01"
      );

  kuberlogs_company.set_init_product(
      "cybernetics factory",
      "an rpg about a young entrepreneur wishing to build and run many cybernetics factories at a profit to fund their industrialist dreams",
      40,
      40
      );
  kuberlogs_company.run_menu();
}
