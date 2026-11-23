class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        idx_to_emails = defaultdict(set)
        email_to_idx = {}
        for idx, account in enumerate(accounts):
            name, *emails = account
            old_idxs = [email_to_idx[email] for email in emails if email in email_to_idx]
            email_to_idx.update({email: idx for email in emails})
            idx_to_emails[idx].update(emails)
            for oidx in old_idxs:
                idx_to_emails[idx].update(idx_to_emails[oidx])
                email_to_idx.update({email: idx for email in idx_to_emails[oidx]})
                del idx_to_emails[oidx]
        
        return [[accounts[idx][0], *sorted(emails)] for idx, emails in idx_to_emails.items()]


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        idx_to_emails = defaultdict(set)
        email_to_idx = {}
        for idx, account in enumerate(accounts):
            name, *emails = account
            old_idxs = {email_to_idx[email] for email in emails if email in email_to_idx}
            email_to_idx.update({email: idx for email in emails})
            idx_to_emails[idx].update(emails)
            for oidx in old_idxs:
                idx_to_emails[idx].update(idx_to_emails[oidx])
                email_to_idx.update({email: idx for email in idx_to_emails[oidx]})
                del idx_to_emails[oidx]
        
        return [[accounts[idx][0], *sorted(emails)] for idx, emails in idx_to_emails.items()]
    

class DisjointSetUnion:

    def __init__(self, n):
        self.rank = [1] * n
        self.pids = [-1] * n
    
    def find(self, x):
        if self.pids[x] == -1:
            return x
        self.pids[x] = self.find(self.pids[x])
        return self.pids[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return 
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.rank[px] += self.rank[py]
        self.pids[py] = px

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_idx = {}
        dsu = DisjointSetUnion(len(accounts))

        for idx, account in enumerate(accounts):
            name, *emails = account
            old_idxs = {dsu.find(email_to_idx[email]) for email in emails if email in email_to_idx}
            email_to_idx.update({email: idx for email in emails})
            for oidx in old_idxs: 
                dsu.union(oidx, idx)
        
        idx_to_emails = defaultdict(list)
        for email, idx in email_to_idx.items():
            idx_to_emails[dsu.find(idx)].append(email)
        return [[accounts[idx][0], *sorted(emails)] for idx, emails in idx_to_emails.items()]


class DisjointSetUnion:

    def __init__(self, n):
        self.rank = [1] * n
        self.pids = [-1] * n
    
    def find(self, x):
        if self.pids[x] == -1:
            return x
        self.pids[x] = self.find(self.pids[x])
        return self.pids[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return 
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        
        self.rank[px] += self.rank[py]
        self.pids[py] = px

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_idx = {}
        dsu = DisjointSetUnion(len(accounts))

        for idx, account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                if email in email_to_idx:
                    dsu.union(email_to_idx[email], idx)
                else:
                    email_to_idx[email] = idx
        
        idx_to_emails = defaultdict(list)
        for email, idx in email_to_idx.items():
            idx_to_emails[dsu.find(idx)].append(email)
        return [[accounts[idx][0], *sorted(emails)] for idx, emails in idx_to_emails.items()]


class DisjointSetUnion:

    def __init__(self, n):
        self.pids = list(range(n))
    
    def find(self, x):
        if self.pids[x] != x:
            self.pids[x] = self.find(self.pids[x])
        return self.pids[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        self.pids[py] = px

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_idx = {}
        dsu = DisjointSetUnion(len(accounts))

        for idx, account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                if email in email_to_idx:
                    dsu.union(email_to_idx[email], idx)
                else:
                    email_to_idx[email] = idx
        
        idx_to_emails = defaultdict(list)
        for email, idx in email_to_idx.items():
            idx_to_emails[dsu.find(idx)].append(email)
        return [[accounts[idx][0], *sorted(emails)] for idx, emails in idx_to_emails.items()]


    