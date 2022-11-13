log_file = 'Seminar_8/log.txt'

def log(data):
    with open (log_file,'a') as f:
        f.write(f'{data}\n')