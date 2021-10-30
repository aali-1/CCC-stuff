#include <iostream>
int arr[20];
int prinnt(int arr[])
{
  for (int j = 0; j < 5; j++)
    {
      printf ("%d ",arr[j]);
    }
  printf("\n");
  return 0;
}
int main()
{
  int N = 5;
  for (int i = 0; i < N; i++)
  {
    scanf("%d", &arr[i]);
  }
  while(N>0){
    for(int k = 0; k < 4; k++){
      if (arr[k]>arr[k+1]){
        int ui = arr[k+1];
        arr[k+1]=arr[k];
        arr[k]=ui;
        prinnt(arr);
      }
    }
    N--;
  }
}