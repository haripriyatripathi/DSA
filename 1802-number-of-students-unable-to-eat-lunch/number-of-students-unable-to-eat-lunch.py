class Solution(object):
    def countStudents(self, students, sandwiches):
        # count students who want 0 and 1
        count = [0, 0]

        for s in students:
            count[s] += 1

        # check sandwiches one by one
        for i, s in enumerate(sandwiches):
            if count[s] == 0:
                return len(sandwiches) - i
            count[s] -= 1

        return 0