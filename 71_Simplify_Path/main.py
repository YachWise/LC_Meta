class Solution(object):
    def simplifyPath(self, path):
        path_list = []
        split_path = path.split('/')
        for directory in split_path:
            if directory == "." or not directory:
                continue
            elif directory == "..":
                if path_list:
                    path_list.pop()
            else:
                path_list.append(directory)

        return "/" + "/".join(path_list)

