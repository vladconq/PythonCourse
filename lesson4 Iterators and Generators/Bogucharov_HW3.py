import os
import stat


def hardlink_check(directory_path: str) -> bool:
    directory_path = directory_path.lstrip('/')
    try:
        files = os.listdir(directory_path)
        for current_file in files:
            first_file = current_file
            for looking_file in files:
                if first_file != looking_file:
                    second_file = looking_file
                    inode1 = os.stat(directory_path + '/' + first_file)
                    inode2 = os.stat(directory_path + '/' + second_file)
                    if (inode1[stat.ST_INO], inode1[stat.ST_DEV]) == (inode2[stat.ST_INO], inode2[stat.ST_DEV]):
                        return True
                    else:
                        return False
    except FileNotFoundError:
        return False


print(hardlink_check("/dir1"))
print(hardlink_check("/dir2"))
print(hardlink_check("/dir3"))
print(hardlink_check(""))
print(hardlink_check("/foo/bar"))
