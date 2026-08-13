public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var groups = new Dictionary<string, List<string>>();
        for (int i = 0; i < strs.Length; i++)
        {
            string str_s = String.Concat($"{strs[i]}".OrderByDescending(x => x));

            if (!groups.ContainsKey(str_s))
            {
                var values = new List<string>();
                values.Add(strs[i]);
                groups.Add(str_s, values);
            }
            else
            {
                var values = groups[str_s];
                values.Add(strs[i]);
            }
        }

        var result = new List<List<string>>();
        foreach (var group in groups)
        {
            result.Add(group.Value);
        }
        return result;
    }
}
