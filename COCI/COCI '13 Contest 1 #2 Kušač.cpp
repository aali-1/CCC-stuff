#include <iostream>
#include <numeric>
int main()
{
  int N,M;
  scanf("%d",&N);
  scanf("%d",&M);
  int locm = std::lcm(N,M);
  int idk = ((locm/N)-1)*N;
  int final = idk/(locm/M);
  printf("%d",final);
}