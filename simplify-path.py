def simplifyPath(path: str):
    path_list = path.split('/')
    path_stack = []

    for c in path_list:
        if c:
            if c == '.':
                continue
            elif c == '..':
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(c)

    return "/"+"/".join(path_stack)


path = ''
# path = "/a/../../b/../c//.//"
# path = "/a//b////c/d//././/.."
print(simplifyPath(path))
