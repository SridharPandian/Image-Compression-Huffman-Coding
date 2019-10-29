import numpy as np
import heapq

class HeapNode:
    def __init__(self, pixel, prob):
        self.pixel = pixel
        self.prob = prob
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.prob < other.prob

    def __eq__(self, other):
        if (other == None):
            return -1
        if (not isinstance(other, HeapNode)):
            return -1
        return self.prob == other.prob

class Huffman_Coding:
    def __init__(self, code_dict):
        self.code_dict = code_dict
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_heap(self, Code_dict):
        for key in Code_dict:      
            node = HeapNode(key, Code_dict[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged_node = HeapNode(None, node1.prob + node2.prob)

            merged_node.left = node1
            merged_node.right = node2

            heapq.heappush(self.heap, merged_node)

    def make_codes_helper (self, root, current_code):
        if root is None:
            return 
        if root.pixel != None:
            self.codes[root.pixel] = current_code
            self.reverse_mapping[current_code] = root.pixel
            return 

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes (self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def compress (self):
        self.make_heap(self.code_dict)
        self.merge_nodes()
        self.make_codes()
        return self.codes, self.reverse_mapping