class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.node_map = {}
        # dummy values
        self.head = ListNode(-1, -1)  # next holds real value
        self.tail = ListNode(-1, -1)  # prev holds real value

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.node_map:
            return -1

        node = self.node_map[key]

        self._remove(node)
        self._add(node)

        return node.val

    def put(self, key, value):
        if key in self.node_map:
            old_node = self.node_map[key]
            self._remove(old_node)

        # create new node
        node = ListNode(key, value)
        # if it exists, override it
        # if it doesn't exist, create it
        self.node_map[key] = node
        self._add(node)

        if len(self.node_map) > self.capacity:
            # Remove LRU
            node_to_delete = self.head.next
            self._remove(node_to_delete)
            del self.node_map[node_to_delete.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)