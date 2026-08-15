class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == INT_MIN && divisor == -1){
            return INT_MAX;
        }

        //CHECK NEGATIVE POSITIVE
        bool check = (dividend < 0)^(divisor < 0);

        long long a = abs((long long)dividend);
        long long b = abs((long long)divisor);

        //initialize ans
        long long ans=0;

        //iteration
        while(a>=b){
            long long temp=b;
            long long count=1;

            while(a>=temp+temp){
                temp+=temp;
                count+=count;
            }
            a-=temp;
            ans+=count;
        }
        if(check){
            ans=-ans;
        }else{
            return ans;
        }
        return ans;

    }
};
//        if (dividend == INT_MIN && divisor == -1)
//             return INT_MAX;

//         bool neg = (dividend < 0) ^ (divisor < 0);

//         long long a = abs((long long)dividend);
//         long long b = abs((long long)divisor);

//         long long ans = 0;

//         while (a >= b) {

//             long long temp = b;
//             long long count = 1;

//             while (a >= temp + temp) {
//                 temp += temp;
//                 count += count;
//             }

//             a -= temp;
//             ans += count;
//         }

//         if (neg)
//             ans = -ans;

//         return ans;
//     }
// };