class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()
        for s in emails:
            i, local = 0, ""
            while s[i] != "@" and s[i] != "+":
                if s[i] != ".":
                    local += s[i]
                i += 1
            while s[i] != "@":
                i += 1
            domain = s[i+1 :]
            st.add(local + domain)
        return len(st)