#include <bits/stdc++.h>
using namespace std;
int N,ls[1000000],delta,i,j;

int main() {
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);
  int maximum=0;
  cin>>N;
  for(int i=0;i<N;i++)
  cin>>ls[i];
  sort(ls,ls+N);
  vector<int> v(ls,ls+N);
  for(int x=0;x<N;x++){
    for(int y=x+1;y<N;y++){
      delta=ls[y]-ls[x];
      j=ls[y]+delta;
      i=lower_bound(v.begin(),v.end(),j)-v.begin();
      if(i<N && ls[i]==j){
        if(delta==0){
          j=upper_bound(v.begin(),v.end(),j)-v.begin();
          if(j-i==3){
            maximum=max(maximum,3*(ls[x]+delta));
          }
        }
        else{
          maximum=max(maximum,3*(ls[x]+delta));
        }
      }
    }
  }
  printf("%d",maximum);
} 