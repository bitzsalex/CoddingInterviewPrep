class AbsolutePathLength:
    def __init__(self, path:str) -> None:
        self.path = path
        self.path_copy = path
        self.max_path_length = 0
    
    def get_max_path_length(self) -> int:
        # check if the file path has a file, if not return 0
        # check if the file path doesn't begin with either of \n or \n since we are interested \
        # in finding the absolute path length
        if "." not in self.path or self.path.startswith("\n") or self.path.startswith("\t"):
            return 0
        
        self.max_path_length = 0
        self.max_length_calculator(0, 0)
        return self.max_path_length
    
    def change_path(self, path:str) -> None:
        self.path = path
        self.path_copy = path
    
    # README: this function code is from https://github.com/ChenglongChen/LeetCode-3/blob/master/Python/longest-absolute-file-path.py
    def longest_length_path(self):
        max_length = 0
        # a dictionary to hold the depth and it's path_length
        path_length = {0: 0}
        
        # split using \n
        for line in self.path_copy.split('\n'):
            # get the name after striping the \t
            name = line.lstrip('\t')
            # count how many \t are there, i.e., they signify the depth
            depth = len(line) - len(name)
            
            # check if the line contains any file
            if '.' in name:
                # if yes, update the max_length
                max_length = max(max_length, path_length[depth] + len(name))
            else:
                # if no, update the path_length dictionary
                path_length[depth + 1] = path_length[depth] + len(name) + 1
                
        return max_length
        
    # thi is my method
    def max_length_calculator(self, current_tab_count:int, path_length_sofar:int) -> None:
        while self.path:
            name_length = 0
            name = ""
            new_line_index = self.path.find("\n")
            
            if new_line_index != -1:
                name = self.path[0:new_line_index]
                self.path = self.path[new_line_index+1:]
            else:
                name += self.path[0:]
                self.path = ""
            name_length = len(name)
            
            if "." in name:
                path_length = path_length_sofar + name_length
                self.max_path_length = path_length if path_length > self.max_path_length else self.max_path_length
                return
            else:
                while self.path.startswith("\t"):
                    tab_count = 0
                    while self.path[tab_count:tab_count + 1] == "\t":
                        tab_count += 1
                        
                    if tab_count > current_tab_count:
                        self.path = self.path[tab_count:]
                        self.max_length_calculator(tab_count, path_length_sofar + name_length + 1)
                    else:
                        return
    
            
path_finder = AbsolutePathLength("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
path_finder.get_max_path_length(), path_finder.longest_length_path()

path_finder.change_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
path_finder.get_max_path_length(), path_finder.longest_length_path()

path_finder.change_path("dir\n\ta\n\t\taa\n\t\t\taaa\n\t\t\t\tfile1.txt\n\taaaaaaaaaaaaaaaaaaaaa\n\t\tsth.png")
path_finder.get_max_path_length(), path_finder.longest_length_path()