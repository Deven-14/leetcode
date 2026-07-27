class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path in paths:
            directory, *files = path.split()
            for file in files:
                i = file.index('(')
                file_path, file_content = file[:i], file[i + 1:-1]
                content_to_paths[file_content].append(f"{directory}/{file_path}")
        
        return list(dup_paths for dup_paths in content_to_paths.values() if len(dup_paths) > 1)


# * 93%
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path in paths:
            directory, *files = path.split()
            for file in files:
                i = file.index('(')
                file_path, file_content = file[:i], file[i + 1:-1]
                content_to_paths[file_content].append(f"{directory}/{file_path}")
        
        return [dup_paths for dup_paths in content_to_paths.values() if len(dup_paths) > 1]


# * 99%
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)

        for path in paths:
            directory, *files = path.split(' ') # * ' ' made the difference
            for file in files:
                i = file.index('(')
                file_path, file_content = file[:i], file[i + 1:-1]
                content_to_paths[file_content].append(f"{directory}/{file_path}")
        
        return [dup_paths for dup_paths in content_to_paths.values() if len(dup_paths) > 1]