class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        
        i = 0
        max_radius = 0
        
        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
            
            dist = abs(heaters[i] - house)
            max_radius = max(max_radius, dist)
            
        return max_radius