CONST_UP_HALF = 1
CONST_LOW_HALF = -1

class BinarySearch:
    def __init__(self):
        pass

    def isBigger(self, value, pivot):
        if value > pivot:
            return 1
        elif value < pivot:
            return -1
        else:
            return 0

    def generate_half_array(self, array_input, pivot_position, half):
        if half == CONST_UP_HALF:
            output = array_input[pivot_position + 1:]
        else:
            output = array_input[0:pivot_position]
        return output

    def binary_search_iterative(self, array_input, value):
        offset= 0
        array_len = len(array_input)
        half_array = []
        while array_len >= 1:
            pivot = int(array_len/2)
            half_present = self.isBigger(value, array_input[pivot])
            if half_present == 0:
                return pivot + offset
            else:
                if half_present > 0:
                    offset += (pivot + 1)
                half_array = self.generate_half_array(array_input, pivot, half_present)
                array_input = half_array
                array_len = len(array_input)
        return -1









