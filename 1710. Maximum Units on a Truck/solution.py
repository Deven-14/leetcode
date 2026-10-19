class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        i, n = 0, len(boxTypes)

        while truckSize and i < n:
            no_of_boxes, no_of_units_per_box = boxTypes[i]
            t = min(no_of_boxes, truckSize)
            units += t * no_of_units_per_box
            truckSize -= t
            i += 1
        
        return units


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0

        for boxType in boxTypes:
            no_of_boxes, no_of_units_per_box = boxType
            t = min(no_of_boxes, truckSize)
            units += t * no_of_units_per_box
            truckSize -= t
        
        return units


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0

        for boxType in boxTypes:
            if truckSize == 0:
                break
            
            no_of_boxes, no_of_units_per_box = boxType
            t = min(no_of_boxes, truckSize)
            units += t * no_of_units_per_box
            truckSize -= t
        
        return units


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0

        for no_of_boxes, no_of_units_per_box in boxTypes:
            if truckSize == 0:
                break
            
            t = min(no_of_boxes, truckSize)
            units += t * no_of_units_per_box
            truckSize -= t
        
        return units



class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0

        for no_of_boxes, no_of_units_per_box in boxTypes:
            if truckSize == 0:
                break
            
            if truckSize > no_of_boxes:
                units += no_of_boxes * no_of_units_per_box
                truckSize -= no_of_boxes
            else:
                units += truckSize * no_of_units_per_box
                truckSize = 0
        
        return units


