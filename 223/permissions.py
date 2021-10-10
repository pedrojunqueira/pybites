permission_values = {
    "r": 4,
    "w": 2,
    "x": 1,
    "-": 0,
}


def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
    its octal representation.

    In Unix you have user, group and other permissions,
    each can have read (r), write (w), and execute (x)
    permissions expressed by r, w and x.

    Each has a number:
    r = 4
    w = 2
    x = 1

    So this leads to the following input/ outputs examples:
    rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
    rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
    r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    user = rwx[:3]
    group = rwx[3:6]
    other = rwx[6:]
    user_octal = 0
    group_octal = 0
    other_octal = 0
    for u, g, o in zip(user, group, other):
        user_octal += permission_values[u]
        group_octal += permission_values[g]
        other_octal += permission_values[o]
    return f"{user_octal}{group_octal}{other_octal}"
