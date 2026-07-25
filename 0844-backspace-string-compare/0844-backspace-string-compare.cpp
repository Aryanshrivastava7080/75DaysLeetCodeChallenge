class Solution {
public:
    string build(string s){

        stack<char>st;

        string ans="";

        for(char f : s){

            if(f!='#'){
                st.push(f);
            }
            else if(!st.empty()) {
                st.pop();
            }  
        }
         while(!st.empty()){
                  ans += st.top();
                 st.pop();
}
 reverse(ans.begin(), ans.end());
 return ans;
    }
    
    bool backspaceCompare(string s, string t) {

       return build(s)==build(t);
    }
};