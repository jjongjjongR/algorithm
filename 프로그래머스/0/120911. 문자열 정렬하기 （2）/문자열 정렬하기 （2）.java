import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        String lower = my_string.toLowerCase();
        
        char[] charArr = lower.toCharArray();
        
        Arrays.sort(charArr);
        
        answer = new String(charArr);
        
        return answer;
    }
}