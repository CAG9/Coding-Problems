class Solution:
    def reverseBits(self, n: int) -> int:
        binary_number = str(f"{n:032b}")
        return int(binary_number[::-1], 2)
