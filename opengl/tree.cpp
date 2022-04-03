#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

class Choice
{
  //+++++++++++++++++++++++
  public:
  //+++++++++++++++++++++++

  Choice(const char* _name)
  {
   name = _name;
  }

  //-----------------------

  const string getName()
  {
    return name;
  }
  //-----------------------


 
  
  //+++++++++++++++++++++++
  private:
  //+++++++++++++++++++++++
  std::string name;
  //-----------------------
  //-----------------------

};

int enter_a_number() {
  printf("enter a number: ");
  int choice;
  scanf("%d", &choice);
  return choice;
}

Choice main_menu()
{
  std::vector<Choice> choices;

  auto treelon = Choice("treelon");
  choices.push_back(treelon);

  auto cyborg = Choice("cyborg");
  choices.push_back(cyborg);

  int x = 0;
  for(auto it = choices.begin(); it != choices.end(); it++)
  {
    printf("%d): %s\n", x, it->getName().c_str());
    x++;
  }
  int choice = enter_a_number();
  return choices[choice];
}

int main()
{
  printf("welcome to tree\n");
  Choice choice = main_menu();
  if(choice.getName().compare(string("treelon")) == 0) {
    system("./Treelon");
  } else if (choice.getName().compare(string("cyborg")) == 0) {
    system("./Cyborg");
  } else {
  }
}
