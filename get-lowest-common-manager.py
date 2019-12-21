class Node(object):
    def __init__(self, name):
        self.name = name
        self.directReports = []
        
def helper(node, r1, r2):
    if not node:
        return None
    if node == r1 or node == r2:
        return node
    
    results = []
    for reporter in node.directReports:
        reporter_node = helper(reporter, r1, r2)
        if reporter_node:
            results.append(reporter_node)
    if len(results) == 1:
        return results[0]
    if len(results) == 2:
        return node
    return None
    
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return helper(topManager, reportOne, reportTwo)


def createNodes(names):
    result = {}
    for name in names:
        result[name] = Node(name)
    return result

# nodes = createNodes(['a','b','c','d','e','f','g','h','i'])
# nodes['a'].directReports = [nodes['b'], node['c']]
# nodes['b'].directReports = [nodes['d'], node['e']]
# nodes['d'].directReports = [nodes['h'], node['i']]
# nodes['c'].directReports = [nodes['f'], node['g']]