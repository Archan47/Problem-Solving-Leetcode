class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        if event1[0] <= event2[1] and event2[0] <= event1[1]:
            return True
        else:
            return False
        