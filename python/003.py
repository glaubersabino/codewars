def pig_it(text):
    print(text)
    text = text.split(' ')
    print(text)
    for k, v in enumerate(text):
        if v not in '!?.,";:~´()-':
            print(f'NÂO TEM ACENTUAÇÂO -> {v}')
            if len(v)> 1:
                new = v[1:] + v[0] + 'ay'
            else:
                new = v + 'ay'
            text[k] = new
    print(' '.join(text))
    return ' '.join(text)

pig_it('Quis custodiet ipsos custodes ?')