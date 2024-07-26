class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '').split('+')[0]
            unique.add(f'{local}@{domain}')
        return len(unique)
        