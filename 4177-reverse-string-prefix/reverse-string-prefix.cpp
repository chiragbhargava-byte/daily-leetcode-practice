class Solution {
public:
    string reversePrefix(string s, int k) {
        int actual_k = min(k, (int)s.length());

        int i=0, j=actual_k - 1;
        while(i<j){
            swap(s[i], s[j]);

            i++;
            j--;
        }

        return s;
    }
};