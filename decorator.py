from datetime import datetime as dt


def loger(file_path='files/logs.txt'):
    def __loger(old_func):
        def new_func(*args, **kwargs):
            date = str(dt.now().date())
            time = str(dt.now().time()).split('.')[0]
            log = f'{date}, {time}, {old_func.__name__}, {list(args)}, {list(kwargs)}'
            with open(file_path, 'a') as f:
                f.write(str(log))
                f.write('\n')
            result = old_func(*args, **kwargs)
            return result
        return new_func
    return __loger


def loger2(old_func, file_path='files/logs.txt'):
    def new_func(*args, **kwargs):
        date = str(dt.now().date())
        time = str(dt.now().time()).split('.')[0]
        log = f'{date}, {time}, {old_func.__name__}, {list(args)}, {list(kwargs)}'
        with open(file_path, 'a') as f:
            f.write(str(log))
            f.write('\n')
        result = old_func(*args, **kwargs)
        return result
    return new_func
