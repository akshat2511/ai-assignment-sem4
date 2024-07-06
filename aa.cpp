#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t){
	    int arr;
	    int c=0;
	    for(int i=0;i<5;i++){
	        cin>>arr;
	        if(arr==1)c++;
	        
	    }
	    if(c>=4)cout<<"YES\n";
	    else cout<<"NO\n";
	    
	    t--;
	}
	

}
