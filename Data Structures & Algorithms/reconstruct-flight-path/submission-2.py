class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for src, dst in sorted(tickets):
            adj[src].append(dst)

        res = []

        def dfs(src):
            while adj[src]:
                dest = adj[src].pop(0)
                dfs(dest)

            res.append(src)
        dfs("JFK")
        return res[::-1]

        