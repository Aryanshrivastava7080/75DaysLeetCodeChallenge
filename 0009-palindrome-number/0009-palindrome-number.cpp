class Solution {
public:
    bool isPalindrome(int x) {
        long ans=0;
        int target=x;
        
        if(target<0) return false;
        while(x!=0){
            int digit = x%10;
            ans = ans*10+digit;
            x=x/10;
        }
        if(ans==target) return true;
        else
        return false;

    }
};