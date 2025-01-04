class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        units = { "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}

        tens = { "10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
        
        hundred = "Hundred"
        thousand = "Thousand"
        million = "Million"
        billion = "Billion"

        def units_place(num_str):
            return [] if num_str == '0' else [units[num_str]]

        def tens_place(num_str):
            if num_str[0] == '0':
                return units_place(num_str[1])
            elif num_str[0] == '1':
                return [tens[num_str]]
            res = [tens[num_str[0]]]
            res.extend(units_place(num_str[1]))
            return res

        def hundreds_place(num_str):
            res = []
            t = units_place(num_str[0])
            if t:
                res.extend(t)
                res.append(hundred)
            res.extend(tens_place(num_str[1:]))
            return res
        
        def thousands_place(num_str):
            res = []
            l = len(num_str)
            if l == 6:
                t = hundreds_place(num_str[0:3])
                if t:
                    res.extend(t)
                    res.append(thousand)
                res.extend(hundreds_place(num_str[3:]))
            elif l == 5:
                t = tens_place(num_str[0:2])
                if t:
                    res.extend(t)
                    res.append(thousand)
                res.extend(hundreds_place(num_str[2:]))
            elif l == 4:
                t = units_place(num_str[0])
                if t:
                    res.extend(t)
                    res.append(thousand)
                res.extend(hundreds_place(num_str[1:]))

            return res
        
        def millions_place(num_str):
            res = []
            l = len(num_str)
            if l == 9:
                t = hundreds_place(num_str[0:3])
                if t:
                    res.extend(t)
                    res.append(million)
                res.extend(thousands_place(num_str[3:]))
            elif l == 8:
                t = tens_place(num_str[0:2])
                if t:
                    res.extend(t)
                    res.append(million)
                res.extend(thousands_place(num_str[2:]))
            elif l == 7:
                t = units_place(num_str[0])
                if t:
                    res.extend(t)
                    res.append(million)
                res.extend(thousands_place(num_str[1:]))

            return res
        
        num_str = str(num)
        res = []
        l = len(num_str)
        if l == 10:
            res.extend(units_place(num_str[0]))
            res.append(billion)
            res.extend(millions_place(num_str[1:]))
        elif 7 <= l <= 9:
            res.extend(millions_place(num_str))
        elif 4 <= l <= 6:
            res.extend(thousands_place(num_str))
        elif l == 3:
            res.extend(hundreds_place(num_str))
        elif l == 2:
            res.extend(tens_place(num_str))
        else:
            return units[num_str]
        
        return " ".join(res)
