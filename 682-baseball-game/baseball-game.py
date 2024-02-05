class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for operation in operations:
            if operation == "D":
                records.append(2*records[-1])
            elif operation == "C":
                records.pop()
            elif operation == "+":
                records.append(records[-1] + records[-2])
            else:
                records.append(int(operation))
        return sum(records)
        