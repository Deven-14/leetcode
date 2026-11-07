class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        match ruleKey:
            case 'type':
                ruleIdx = 0
            case 'color':
                ruleIdx = 1
            case 'name':
                ruleIdx = 2

        return sum(1 for item in items if item[ruleIdx] == ruleValue)