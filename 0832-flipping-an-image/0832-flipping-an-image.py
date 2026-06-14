class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == row[right]:
                    # XOR with 1 flips the bit (0 becomes 1, 1 becomes 0)
                    row[left] = row[right] = row[left] ^ 1
                left += 1
                right -= 1
        return image