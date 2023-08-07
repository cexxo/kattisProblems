/*
Vector functions (https://open.kattis.com/problems/vectorfunctions)
Your task is to implement the following C++ functions:

#include "vectorfunctions.h"

// Reverse a vector.
// Note that it is sent as a reference, so you should
// reverse the same vector that was sent in.
void backwards(vector<int>& vec){
        ...
}

// Return every other element of the vector, starting with the first.
// You should return a new vector with the answer.
// You are not allowed to modify the vector, even though it is
// sent as a reference. Therefore, the parameter is declared "const".
vector<int> everyOther(const vector<int>& vec){
        ...
}

// Return the smallest value of a vector.
int smallest(const vector<int>& vec){
        ...
}

// Return the sum of the elements in the vector.
int sum(const vector<int>& vec){
  ...
}

// Return the number of odd integers, that are also on an
// odd index (with the first index being 0).
int veryOdd(const vector<int>& vec){
  ...
}
The vectors sent has between 1 and 100 000 elements. Each 
number in the vector is between -2000 and 2000.
TEMPLATE:
You can download the above template as the file 
vectorfunctions.cpp in the Attachments menu. When submitting 
your solution, send in only this file.
TESTING:
To test your program, you can download the file 
vectorfunctions.h in the menu to the left, which contains 
examples that test your code. Place it in the same folder as 
your program when compiling.
*/
#include "vectorfunctions.h"

// Reverse a vector.
// Note that it is sent as a reference, so you should
// reverse the same vector that was sent in.
void backwards(vector<int>& vec){
        vector<int> temp(vec.size());
        for (int i = 0; i<vec.size();i++){
            temp[i] = vec[vec.size()-1-i];
        }
        for (int i = 0; i<vec.size();i++){
            vec[i] = temp[i];
        }
}

// Return every other element of the vector, starting with the first.
// You should return a new vector with the answer.
// You are not allowed to modify the vector, even though it is
// sent as a reference. Therefore, the parameter is declared "const".
vector<int> everyOther(const vector<int>& vec){
        vector<int> temp;
        for (int i=0;i < vec.size();i++){
            if(i%2==0){
                temp.push_back(vec[i]);
            }
        }
        return temp;
}

// Return the smallest value of a vector.
int smallest(const vector<int>& vec){
        int minimum = 100000000;
        for (int i = 0; i <vec.size();i++){
            if(vec[i] < minimum){
                minimum = vec[i];
            }
        }
        return minimum;
}

// Return the sum of the elements in the vector.
int sum(const vector<int>& vec){
  int total = 0;
  for(int i = 0; i< vec.size();i++){
      total += vec[i];
  }
  return total;
}

// Return the number of odd integers, that are also on an
// odd index (with the first index being 0).
int veryOdd(const vector<int>& vec){
    int count = 0;
  for(int i = 0; i< vec.size();i++){
      if(i%2 != 0 && vec[i]%2!= 0){
          count++;
      }
  }
  return count;
}