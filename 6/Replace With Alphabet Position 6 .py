


def alphabet_position(text):
    return f'{" ".join([str(ord(ch.lower())-96) for ch in text if 97<=ord(ch.lower())<=122])}'
# можно короче
    return f'{" ".join([str(ord(ch) - 96) for ch in text.lower() if ch.isalpha()])}'





st = "The sunset sets at twelve o' clock"
st = 'The narwhal bacons at midnight'

print(alphabet_position(st))
