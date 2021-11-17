#include <bits/stdc++.h>
using namespace std;
long long number;
char func;
int Q;
deque<int> d{};
int main()
{
  cin.sync_with_stdio(0);
  cin.tie(0);
  cin>>Q;
  while(Q--){
    cin >> func >> number;
    if(func==70) //F
      d.push_front(number);
    else if(func==69) //E
      d.push_back(number);
    else{ //R
      if(d.size()==1){
        d.pop_front();
      }
      else
        d.erase(find(d.begin(), d.end(), number));
      
    }
  }
  for(int i:d){
    printf("%d\n",i);
  }
}
