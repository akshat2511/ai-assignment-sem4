// Using Genetic Algorithm (GA) and Python programming to solve the 5-queen problem. In
// this problem, the goal is to place five queens on a 5x5 chessboard such that no two queens
// threaten each other. The GA should follow the steps including chromosome design, initialization,
// fitness evaluation, selection, crossover, mutation, and updating generations. Additionally, you
// need to comment on the average fitness value of the population after each iteration.

#include<iostream>
using namespace std;
int main(){
    cout<<"enter the locations of queens on 5*5 matrix:"<<endl;
    int a[5];
    int b[5]={1,2,3,4,5};
    for(int i=0;i<5;i++){
        cin>>a[i];
    }
    //checking if any queen can attack another
    int k=0;
    while(1){
        
    for (int i=0;i<k;i++){
        int temp;
        temp=a[i];
        a[i]=b[i];
        b[i]=temp;
    }
    k++;
    }


}
