class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char>st;

        for(char ch : num){
            while(!st.empty() && st.back()>ch && k>0){
                st.pop_back();
                k--;
            }
            st.push_back(ch);
        }

        while(k>0){
            st.pop_back();
            k--;
        }

        string ans ="";
        for(char ch : st)
           ans += ch;

        int i = 0;
        while(i<ans.size() && ans[i] == '0'){
            i++;
        }

        ans = ans.substr(i);

        return ans.empty() ? "0" : ans;

    }
};