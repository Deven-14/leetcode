class Codec:

    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl: str) -> str:
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        
        return 'http://tinyurl.com/' + self.url2code[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.code2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# https://leetcode.com/problems/encode-and-decode-tinyurl/solutions/100268/two-solutions-and-thoughts-by-stefanpoch-r8fk