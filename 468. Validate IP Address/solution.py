class Solution:
    def validIPv4(self, IPv4):
        bytes4 = IPv4.split(".")
        if len(bytes4) != 4:
            return False
        
        for byte in bytes4:
            if byte == "" or not byte.isdigit():
                return False
            
            x = int(byte)
            match x:
                case x if x < 10:
                    if len(byte) != 1:
                        return False
                case x if x < 100:
                    if len(byte) != 2:
                        return False
                case x if x > 255:
                    return False
        
        return True

    def validIPv6(self, IPv6):
        bytes8 = IPv6.split(":")
        if len(bytes8) != 8:
            return False

        for byte in bytes8:
            if byte == "" or len(byte) < 1 or len(byte) > 4:
                return False
            for char in byte:
                if char.isalpha() and not 'A' <= char.upper() <= 'F':
                    return False
        
        return True


    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP and self.validIPv4(queryIP):
            return "IPv4"

        elif ":" in queryIP and self.validIPv6(queryIP):
            return "IPv6"
        
        return "Neither"
            