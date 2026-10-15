class Solution:
    def reformatNumber(self, number: str) -> str:
        stripped_num = number.replace(' ', '').replace('-', '')
        new_num = []
        
        while len(stripped_num) > 4:
            new_num.append(stripped_num[:3])
            stripped_num = stripped_num[3:]

        if len(stripped_num) == 4:
            new_num.append(stripped_num[:2])
            new_num.append(stripped_num[2:])
        elif len(stripped_num) > 0:
            new_num.append(stripped_num)
        
        return '-'.join(new_num)