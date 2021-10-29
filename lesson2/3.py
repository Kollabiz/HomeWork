words = ['в', '5', 'часов', '17', 'минут', 'тепмпература', 'воздуха', 'была', '+5', 'градусов']

idx = 0
while idx < len(words):
    word = words[idx]
    if word != '"':
        if word.upper() == word:
            start = word[0]
            if start != '+' and start != '-':
                start = ''
            else:
                word = word[1:]
            ext_word = '{0:02d}'.format(int(word))
            ext_word = f'{start}{ext_word}'
            words[idx] = ext_word
            words.insert(idx, '"')
            words.insert(idx + 2, '"')
            idx += 1
        else:
            words[idx] = ' {} '.format(words[idx])
    idx += 1

print(''.join(words))