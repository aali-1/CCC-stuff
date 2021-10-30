#include <iostream>
#include <string>
using namespace std;
string sentence;
int N = 5;
int main()
{
  cin.sync_with_stdio(0);
  cin.tie(0);
  while (N>0){
    N--;
    int ccnt=0;
    int wcnt=0;
    getline(cin,sentence);
    for(auto x:sentence){
      if(x==' '||x==39){
        if(ccnt>3){
          wcnt++;
        }
        ccnt=0;
      }
      else{
        if(isalpha(x)){
          ccnt++;
        }
      }
    }
    if(ccnt>3){
      wcnt++;
    }
    cout << wcnt<<'\n';
  }
}