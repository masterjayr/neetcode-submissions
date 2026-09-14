class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            
            res.append(src)
        dfs("JFK")
        return res[::-1]

        