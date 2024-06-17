class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")

        new_directories = []
        for directory in directories:
            if directory == "" or directory == ".":
                continue
            elif directory == "..":
                if new_directories:
                    new_directories.pop()
            else:
                new_directories.append(directory)
        
        return "/" + "/".join(new_directories)
