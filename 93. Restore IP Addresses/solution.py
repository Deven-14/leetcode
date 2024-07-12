class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip_addresses = []
        ip_address = []
        n = len(s)

        def backtrack(i = 0, j = 0):
            if i == 4:
                if j == n:
                    ip_addresses.append(".".join(ip_address))
                return
            
            if j >= n:
                return

            if s[j] == "0":
                ip_address.append(s[j])
                backtrack(i+1, j+1)
                ip_address.pop()
                return
            
            for k in range(1, 4):
                bits = s[j:j+k]
                if int(bits) > 255:
                    return
                ip_address.append(bits)
                backtrack(i+1, j+k)
                ip_address.pop()

        backtrack()

        return ip_addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip_addresses = []
        ip_address = []
        n = len(s)

        def backtrack(i = 0, j = 0):
            if i == 4:
                if j == n:
                    ip_addresses.append(".".join(ip_address))
                return
            
            if j >= n:
                return

            if s[j] == "0":
                ip_address.append(s[j])
                backtrack(i+1, j+1)
                ip_address.pop()
                return
            
            for k in range(j+1, min(n+1, j+4)):
                bits = s[j:k]
                if int(bits) > 255:
                    return
                ip_address.append(bits)
                backtrack(i+1, k)
                ip_address.pop()

        backtrack()

        return ip_addresses
