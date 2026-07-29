class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {

//         vector<int>ans;

//         for(int i=0; i<nums1.size(); i++){

//             int j=0;

//             //now search in nums2 position 

//             while(nums1[i]!=nums2[j]){
//                 j++;
//             }

//             int nxtgreater= -1;

//             //right side traverse

//             for(int k=j+1; k<nums2.size(); k++){

//                 if(nums2[k]>nums2[j]){
//                     nxtgreater = nums2[k];
//                     break;
//                 }

//             }
//             ans.push_back(nxtgreater);
//         }
//         return ans;
//     }
// };
        unordered_map<int, int> mp;
        stack<int> st;

        // Process nums2 from right to left
        for (int i = nums2.size() - 1; i >= 0; i--) {

            while (!st.empty() && st.top() <= nums2[i]) {
                st.pop();
            }

            if (st.empty())
                mp[nums2[i]] = -1;
            else
                mp[nums2[i]] = st.top();

            st.push(nums2[i]);
        }

        vector<int> ans;

        for (int num : nums1) {
            ans.push_back(mp[num]);
        }
        return ans;
    }
};
