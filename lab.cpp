#include <iostream>
#include <vector>
using namespace std;


int main()
{
    int dimension;
    cin >> dimension;

    int obs[dimension][dimension];
    cout<<"enter 1 if there is an obstacle 3 for goal and 2 for starting "<<endl;
    for (int i = 0; i < dimension; i++)
    {
        for (int j = 0; j < dimension; j++)
        {cout<<i+1<<","<<j+1<<endl;
        cin>>obs[i][j];
            
        }
    }
    


    return 0;
}