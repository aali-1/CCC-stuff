#include <bits/stdc++.h>
using namespace std;
int N,sq;
int counter;

int main() {
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);
  while(true){
    cin>>N;
    counter=0;
    if(N==0)
      break;
    else{
      sq=N*N;
      for(int i=0;i<=N;i++){
        for(int j=1;j<=N;j++){
          if((i*i)+(j*j)<=sq){
            counter++;
          }
        }
      }
      printf("%d\n",counter*4+1);
    }
  }
} 