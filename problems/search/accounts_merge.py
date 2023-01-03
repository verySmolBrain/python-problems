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