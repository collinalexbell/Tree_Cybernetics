#include <memory>

class Work {};
class Result {};

class Kuberlog {

  void meditative_thinking() {
    system("./meditate 60");
  }

  Work write_test() {
    cout << "write a test" << endl;
  }

  Work write_impl() {
    cout << "write an impl" << endl;
  }

  Result run_test() {
  }


  public: 
  void code() {
    meditative_thinking();

    Work new_test;
    unique_ptr<Result> fail_run, pass_run;

    do {
      new_test = write_test();
      fail_run = run_test(new_test); // will require move sematincs, look that up
    } while (fail_run->has_not_failed())

    do {
      write_impl();
      pass_run = run_test(new_test);
    } while (pass_run->has_not_passed())

    do {
      remove_duplication();
      pass_run = run_test(new_test);
    } while (pass_run->has_not_passed())
  }
};

int main () { Kuberlog kuberlog(); }
