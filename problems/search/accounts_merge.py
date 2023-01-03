class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails, toDelete = {}, []

        for i, acc in enumerate(accounts):
            accounts[i][1:] = sorted(list(set(accounts[i][1:])))
            duplicate = next((emails[e] for e in acc[1:] if e in emails), None)
            for e in acc[1:]:
                if duplicate is None:
                    emails[e] = i
                elif e not in emails:
                    emails[e] = duplicate
                    bisect.insort(accounts[duplicate], e, lo = 1)
            if duplicate is not None: toDelete.append(i)
        
        deleted = 0
        for i in toDelete:
            del accounts[i - deleted]
            deleted += 1

        return accounts

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails, visited, res = defaultdict(list), [False] * len(accounts), []

        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                emails[e].append(i)
        
        def dfs(i):
            if visited[i]: return set()
            visited[i], new_emails = True, set()

            for e in accounts[i][1:]:
                new_emails.add(e)
                for n in emails[e]:
                    new_emails = new_emails | dfs(n)
            
            return new_emails
        
        for i, acc in enumerate(accounts):
            if visited[i]: continue
            res.append([acc[0]] + sorted(dfs(i)))
        
        return res