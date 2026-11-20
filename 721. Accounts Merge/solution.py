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