class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        actual_emails = set()
        for email in emails:
            localname, domain = email.split('@')
            localname = localname.split('+')[0]
            localname = localname.replace('.', '')
            actual_emails.add(f"{localname}@{domain}")
        
        return len(actual_emails)


