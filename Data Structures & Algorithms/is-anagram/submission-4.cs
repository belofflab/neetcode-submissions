public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
        { return false; }

        byte[] abyte = Encoding.UTF8.GetBytes(s);
        byte[] tbyte = Encoding.UTF8.GetBytes(t);
        
        Array.Sort(abyte);
        Array.Sort(tbyte);
        
        for (int i = 0; i < abyte.Length; i++)
        {
            if (abyte[i] != tbyte[i])
            {
                return false;
            }
        }
        return true;
    }
}
