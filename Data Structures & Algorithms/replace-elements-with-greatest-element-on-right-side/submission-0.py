class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #Start with last element as max
        max = arr[len(arr) - 1]
        for i in reversed(range(0, len(arr) - 1)): # Start from second to last element
            temp = arr[i]
            arr[i] = max
            if temp > max:
                max = temp
        
        arr[len(arr) - 1] = -1
        return arr

            
            
        

        