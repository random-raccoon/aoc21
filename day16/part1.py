
hex_lookup = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def hex_to_binary(hex_data):
    return ''.join(hex_lookup[c] for c in hex_data)

def binary_to_int(binary_data):
    value = 0
    for c in binary_data:
        value *= 2
        if c == '1':
            value += 1
    return value

class Data:
    def __init__(self, hex_data):
        self.data = hex_to_binary(hex_data)
        self.index = 0

    def read_int(self, num_bits):
        value = binary_to_int(self.data[self.index:self.index+num_bits])
        self.index += num_bits
        return value

class Packet:
    def __init__(self, data: Data):
        start_index = data.index
        self.version = data.read_int(3)
        self.type_id = data.read_int(3)
        self.subpackets = []
        if self.type_id == 4:
            # literal
            self.value = 0
            needs_more_data = True
            while needs_more_data:
                needs_more_data = data.read_int(1) == 1
                self.value *= 16
                self.value += data.read_int(4)
        else:
            # operator
            length_type = data.read_int(1)
            if length_type == 0:
                subpacket_length = data.read_int(15)
                while subpacket_length > 0:
                    subpacket = Packet(data)
                    self.subpackets.append(subpacket)
                    subpacket_length -= subpacket.data_length
            else:
                num_subpackets = data.read_int(11)
                for i in range(num_subpackets):
                    self.subpackets.append(Packet(data))

        self.data_length = data.index - start_index

    def sum_versions(self):
        value = self.version
        for packet in self.subpackets:
            value += packet.sum_versions()
        return value

hex_data = ''
with open('day16/input.txt', 'r') as f:
    hex_data = f.readline().strip()

data = Data(hex_data)
packet = Packet(data)

print(packet.sum_versions())