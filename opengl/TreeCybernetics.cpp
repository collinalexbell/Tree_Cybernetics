#include <functional>
#include <string>
#include <memory>
#include <iostream>

using namespace std;

class Focus {
  string description;
  function<void()> focus_function;
  public:
    Focus(function<void()> focus_function, string description){
      this->description = description;
      this->focus_function = focus_function;
    }
    Focus(const Focus &focus) {
      description = focus.description;
      focus_function = focus.focus_function;
    }

    void run_focus_function() {
      focus_function();
    }
};

class Corporation {

  shared_ptr<Focus> current_focus;
  string purpose;

  public:
  Corporation(string purpose) {
    this->purpose = purpose;
  }

  void focus(Focus current_focus) {
    this->current_focus = shared_ptr<Focus>(new Focus(current_focus));
  }

  shared_ptr<Focus> get_current_focus() {
    auto rv = current_focus;
    return rv;
  }
};

void build_three_onix(){
  cout << "build three onix" << endl;
}

Corporation TreeCybernetics() {
  auto purpose = "Collin Bell will have $10,000,000 in his possession by January 15, 2022, his 30th birthday. He will earn the money by producing and providing cybernetics to people & corpoations using Tree Cybernetics as the legal vehicle for earning the $$$.";

  auto TreeCybernetics = Corporation(purpose);
  string focus_description = "Build the best Onyx: (robot arms+trelon) for myself, Matt, and Amit by Jan 7th.";
  auto focus = Focus(build_three_onix, focus_description);
  TreeCybernetics.focus(focus);

  return TreeCybernetics;
}

int main() {
  auto t = TreeCybernetics();
  t.get_current_focus()->run_focus_function();
}
