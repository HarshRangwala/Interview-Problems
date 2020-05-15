# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:45:06 2020

@author: Anuj
"""

# By Karthik
from collections import defaultdict
class Solution:
    def build_graph(self, conn):
        conn1 = defaultdict(lambda : list())
        conn2 = defaultdict(lambda : list())
        
        for edge in conn:
            '''
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("EDGE ~~", edge)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            '''
            conn1[edge[0]].append(edge[1])
            conn2[edge[1]].append(edge[0])
            '''
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("conn1 ~~~",conn1)
            print("conn2 ~~~",conn2)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            '''
        return (conn1, conn2)
    def delete_edges(self, edge, i):
        return edge[:i] + edge[i+1:]
    
    def dfs(self, conn1, conn2, visited, server):
        visited.add(server)
        
        for nextServer in conn1[server]:
            if nextServer not in visited:
                visited = self.dfs(conn1, conn2, visited, nextServer)
        
        for nextServer in conn2[server]:
            if nextServer not in visited:
                visited = self.dfs(conn1, conn2, visited, nextServer)
        return visited
    def criticalConnection(self, n , connections):
        result = []
        
        for index in range(len(connections)):
            network = self.delete_edges(connections, index)
            
            conn1 , conn2 = self.build_graph(network)
            
            visited = self.dfs(conn1, conn2, set(), 0)
            
            if len(visited) != n:
                result.append(connections[index])
        
        return result
print(Solution.criticalConnection("", 5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
print(Solution.build_graph("", [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))