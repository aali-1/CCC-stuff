#include <iostream>
#include <math.h> 
using namespace std;
int isprime(int x){
  int g = static_cast <int> (floor(sqrt(x)));
  if(x<2){
    return false;
  }
  else{
    for(int i=2;i<=g;i++){
      if(x%i==0){
        return false;
      }
    }
  return true;
  }
}
int main()
{
  long y=20000000000;
  int N;
  scanf("%d",&N);
  for(int j=N;j<y;j++){
    if(isprime(j)==1){
      printf("%d",j);
      break;
    }
  }
}