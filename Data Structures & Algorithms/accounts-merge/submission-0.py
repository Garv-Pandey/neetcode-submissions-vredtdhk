class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_map = defaultdict(set)
        email_name_map = {}

        for account in accounts:
            acc_name, *emails = account

            pivot_email = emails[0]
            # we dont need to connect each email to every other. 
            # minimum condition for dfs to work is there to be a connection. which we get vai pivot_email (star patter connection)
            # this way is more efficient than making connection with each email
            for email in emails:
                adj_map[pivot_email].add(email)
                adj_map[email].add(pivot_email)
                email_name_map[email] = acc_name # all connected emails will have same name so no case of overwriting and losing data
        

        def dfs(email):
            if email in visited:
                return 
            
            visited.add(email)
            dfs_stack.add(email)
            for related_email in adj_map[email]:
                dfs(related_email)

        result = []
        visited = set()
        for email in email_name_map.keys():
            if email in visited:
                continue
            
            dfs_stack = set()
            dfs(email)

            result.append([email_name_map[email], *sorted(list(dfs_stack))])

        return result
