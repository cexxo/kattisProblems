#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int main(){
    int n = 0;
    cin >> n;
    char a;
    long counter = 0;
    bool found = false;
    bool first = false;
    vector<char> animals(n);
    vector<int> indeces;
    for(int i = 0;i<n;i++){
        cin >> animals[i];
    }
    for(int i = 0; i<n;i++){
        if(animals[i]=='O'){
            indeces.push_back(i);
        }
    }
    for(int i = 0; i<indeces.size();i++){
        counter += pow(2,(n-indeces[i]-1));
    }
    cout<<counter;
    return 0;
}