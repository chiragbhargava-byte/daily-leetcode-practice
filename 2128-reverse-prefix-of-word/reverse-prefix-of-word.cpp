class Solution {
public:
    string reversePrefix(string s, char ch) {
        int index = -1;

        for(int i=0; i<s.length(); i++){
            if(s[i] == ch){
                index = i;
                break;
            }
        }

       int i=0, j=index;

       while(i<j){
            swap(s[i], s[j]);

            i++;
            j--;
       } 

       return s;
    }
};