#include<iostream>
#include<string>
using namespace std;

struct Target_Revenue {
  Target_Revenue(int dollars, string earn_by): dollars(dollars), earn_by(earn_by){}
  int dollars;
  string earn_by;
};

class Product {
  string name;
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
  int sales_to_target(Target_Revenue target) {
    int units_sold = target.dollars/unit_profit;
    return units_sold;
  }
};

class Tree_Cybernetics {
  Target_Revenue *init_capital = NULL;
  Product *init_product = NULL;
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

  void set_init_product(string name, int revenue, int profit) { 
    init_product = new Product(name, revenue, profit);
  }
  ~Tree_Cybernetics() {
    delete init_capital;
    delete init_product;
  }
  void where_are_we_going() {
    cout << init_capital->dollars << "$ by " << init_capital->earn_by << endl;
  }
  void run_menu() {
    string choice;
    cout << "1) Where are we going?" << endl;
    cout << "2) Sales to target?" << endl;
    cin >> choice;
    if(choice == "1"){
      where_are_we_going();
    }
    if(choice == "2"){
      cout << init_product->sales_to_target(*init_capital) << endl;
    }
  }
};



int main() {
  string user = "kuberlog";
  std::cout << "Tree_Cybernetics" << std::endl;
  Tree_Cybernetics kuberlogs_company;
  kuberlogs_company.set_init_capital(
      120000,"2022-04-30"
      );

  kuberlogs_company.set_init_product(
      "cybernetics factory",
      40,
      40
      );
  kuberlogs_company.run_menu();
}
