def merge_files(fname1: str, fname2: str) -> str:
    try:
        with open(fname1, 'r') as f1, open(fname2, 'r') as f2, open('file_result.txt', 'w') as fr:

            last_a = True
            b_var = int(f2.readline())

            while True:
                if last_a:
                    try:
                        a_var = int(f1.readline())
                    except ValueError:
                        t = f2.readlines()
                        t.insert(0, str(b_var) + '\n')
                        fr.write(''.join(t))
                        del t
                        break
                    if a_var < b_var:
                        fr.write(str(a_var) + '\n')
                    else:
                        fr.write(str(b_var) + '\n')
                        last_a = False
                else:
                    try:
                        b_var = int(f2.readline())
                    except ValueError:
                        t = f1.readlines()
                        t.insert(0, str(a_var) + '\n')
                        fr.write(''.join(t))
                        del t
                        break
                    if b_var < a_var:
                        fr.write(str(b_var) + '\n')
                    else:
                        fr.write(str(a_var) + '\n')
                        last_a = True
    except FileNotFoundError:
        print("No such file!")

    else:
        return 'file_result.txt'


merge_files('1.txt', '2.txt')
