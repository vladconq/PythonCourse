from subprocess import Popen, PIPE


def process_count(username: str) -> int:
    count = 0
    with Popen(['ps', 'aux'], stdout=PIPE) as sub_proc:
        sub_proc.stdout.readline()
        for line in sub_proc.stdout:
            if line.split(b' ')[0] == username.encode():
                count += 1
        return count


def total_memory_usage(root_pid: int) -> int:
    with Popen(['ps', 'v', '-p', str(root_pid)], stdout=PIPE) as out:
        out = out.communicate()[0].split(b'\n')
        vsz_index = out[0].split().index(b'RSS')
        try:
            mem = int(float(out[1].split()[vsz_index]) / 1024)
        except IndexError:
            return -1
        return mem
