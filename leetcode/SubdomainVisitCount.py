class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        
        for dom in cpdomains:
            count, domain = dom.split()
            count = int(count)
            sub_domains = domain.split('.')

            for i in range(len(sub_domains)):
                subdomain = '.'.join(sub_domains[i:])
                domain_count[subdomain] += count
        
        result = []
        for sub_domain, count in domain_count.items(): # key, val
            result.append(f"{count} {sub_domain}")
        
        return result
            