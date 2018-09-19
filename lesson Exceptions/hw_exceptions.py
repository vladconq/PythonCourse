import fcntl


class pidfile(object):
    def __init__(self, file):
        self.pidfile = open(file, 'a+')

    def __enter__(self):
        try:
            fcntl.flock(self.pidfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('Resource already in use')
        return self.pidfile

    def __exit__(self, exc_type=None, exc_value=None, exc_tb=None):
        self.pidfile.close()