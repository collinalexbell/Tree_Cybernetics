/*
 * KCC: Kuberlogs C++ Console
 */
#include <iostream>
#include <vector>
#include <string>
#include <dirent.h>

using namespace std;

static bool endsWith(const std::string& str, const std::string& suffix)
{
      return str.size() >= suffix.size() && 0 == str.compare(str.size()-suffix.size(), suffix.size(), suffix);
}

vector<string> get_all_filenames_with_ext(string ext)
{
  vector<string> rv;
  if (auto dir = opendir("./"))
  {
    while (auto f = readdir(dir))
    {
      if (!f->d_name || f->d_name[0] == '.')
        continue; // Skip everything that starts with a dot
      string fname = f->d_name;
      if(endsWith(fname, ".cpp"))
      {
      rv.push_back(f->d_name);
      }
    }
    closedir(dir);
  }
  return rv;
}

int main(int argc, char** argv)
{
  vector<string> filenames;
  if(argc >= 2)
  {
    if(string(argv[1]).compare("ls") == 0)
    {
      filenames = get_all_filenames_with_ext(".cpp");
      for(auto it = filenames.begin(); 
          it != filenames.end();
          it++)
      {
        cout << *it << endl;
      }
    }
  }
}
