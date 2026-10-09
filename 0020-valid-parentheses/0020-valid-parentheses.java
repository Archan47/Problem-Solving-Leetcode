class Solution {
    public boolean isValid(String s) {

                Stack<Character> stringStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            if (ch == '(' || ch == '{' || ch == '[') {
                stringStack.push(ch);
            } else {

                if (stringStack.isEmpty()) return false;

                char top = stringStack.pop();

                if ((ch == ')' && top != '(') ||
                        (ch == '}' && top != '{') ||
                        (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }

        return stringStack.isEmpty();

        
    }
}