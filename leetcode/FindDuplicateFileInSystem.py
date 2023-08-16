class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        doubles = []
        for path in paths:
            parts = path.split()
            dir_path, files = parts[0], parts[1:]
            for file in files:
                file_name, content = file.split('(')
                content = content[:-1]
                full_path = dir_path + '/' + file_name
                contents[content].append(full_path)
                if len(contents[content]) == 2:  # Check for duplicates
                    doubles.append(content)
        result = []
        for double in doubles:
            result.append(contents[double])
        return result
# Note for future: Space complexity need to be improved