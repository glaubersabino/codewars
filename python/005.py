def make_readable(seconds):
    hrs = seconds // 3600
    minu = seconds // 60 % 60
    sec = seconds % 60

    return f'{hrs:02}:{minu:02}:{sec:02}'

time = make_readable(60)
print(time)
