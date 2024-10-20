public class Solution {
    public string MergeAlternately(string word1, string word2) {
        string newString = "";

        int i = 0;
        while(i < word1.Length || i < word2.Length){
            if(i < word1.Length){
                newString += word1[i];
            }
            if (i < word2.Length){
                newString += word2[i];
            }
            i++;
        }

        return newString;
    }
}
