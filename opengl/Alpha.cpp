#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <regex>
#include <algorithm>

using namespace std;

string example_notation = 
  "example\n"
  "- a\n"
  "- - b\n"
  "- - c\n"
  "- d\n"
  "- e\n"
  "- - f\n"
  "- - - g\n";

string name_from_line(string line) {
  return line;
}

class TaskTree {
  public:
  vector<TaskTree> tasks;
  int level;
  TaskTree *parent;
  string name;

  TaskTree(string _name, TaskTree *_parent, int _level) {
    name = _name;
    parent = _parent;
    level = _level;
  };

  TaskTree(string _name) {
    name = _name;
    parent = this;
    level = 0;
  }

  void add_task(string name){
    tasks.push_back(TaskTree(name));
  }

  vector<TaskTree> get_tasks() {
    return tasks;
  }

  string serialize() {
    return name;
  }

  static int deserialize_level(string node) {
    return count(node.begin(), node.end(), '-');
  }

  static TaskTree deserialize(stringstream &tree_stream) {
    string name;
    string line;
    getline(tree_stream, line);
    TaskTree root(name);
    TaskTree::deserialize(tree_stream, root);
    return root;
  }

  static void deserialize(stringstream &tree_stream, TaskTree node) {
    string line;
    string name;

    // base case
    if(tree_stream.eof()) {
      return;
    }

    // recursive case
    getline(tree_stream, line);

    int level = deserialize_level(line);

    name = name_from_line(line);
    TaskTree next_node = TaskTree(name, &node, level);

    if(next_node.level > node.level) {
      node.tasks.push_back(next_node);
      next_node.parent = &node;
    } else {
      node.parent->tasks.push_back(next_node);
      next_node.parent = node.parent;
    }
    TaskTree::deserialize(tree_stream, next_node);
  }
};

int main(){
  stringstream ss(example_notation);
  TaskTree root = TaskTree::deserialize(ss); 
}

// 400 printers * 30 days * 1unit/24 hours
// 12,000 printed units * 8.3333 profit = 100k$
