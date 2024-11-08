//o(nlogn) and o(n)
class HuffmanNode:
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left =None
        self.right = None

def build_huffman_tree(freq_map):
    nodes = [HuffmanNode(char,freq) for char,freq in freq_map.items()]
    while len(nodes) >1:
        nodes.sort(key=lambda x:x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = HuffmanNode(None,right.freq+left.freq)
        merged.left = left
        merged.right = right
        nodes.append(merged)
    return nodes[0]

def build_codes(node,current_node="",codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = current_node
        build_codes(node.left, current_node+"0",codes)
        build_codes(node.right,current_node+"1",codes)
    return codes

def huffman_encoding(data):
    if not data:
        return "",{}

    freq_map = {char :data.count(char) for char in set(data)}
    root = build_huffman_tree(freq_map)
    codes = build_codes(root)
    encoded_data = ''.join(codes[char] for char in data)
    
    return encoded_data, codes

def huffman_decoding(encoded_data, codes):
    reverse_codes = {v: k for k,v in codes.items()}
    current_code = ""
    decoded_data = ""
    for bit in encoded_data:
        current_code+=bit
        if current_code in reverse_codes:
            decoded_data += reverse_codes[current_code]
            current_code = ""
    return decoded_data

inp = input("enter a string")
encoded_data,codes = huffman_encoding(inp)
op = huffman_decoding(encoded_data,codes)
print(inp)
print(encoded_data)
print(op)
print(codes)