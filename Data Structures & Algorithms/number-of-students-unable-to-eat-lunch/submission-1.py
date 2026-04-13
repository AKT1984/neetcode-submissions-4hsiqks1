class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        count = [0,0]
        for s in students:
            count[0] += not s
            count[1] += s
        
        for s in sandwiches:
            if count[s] > 0:
                res -=1
                count[s] -= 1
            else:
                break
        return res
            