import re

# Token türleri
TOKEN_TYPES = {
    'IDENTIFIER': r'[a-zA-Z]+',
    'NUMBER': r'\d+',
    'OPERATOR': r'[+\-*/]',
    'EQUALS': r'=',
    'QUESTION': r'\?',
    'DELIMITER': r',',
    'PAREN': r'[\(\)]',
}

# Lexer fonksiyonu
def lexer(code):
    tokens = []
    index = 0
    while index < len(code):
        match = None
        for token_type, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(code, index)
            if match:
                value = match.group(0)
                tokens.append({
                    'type': token_type,
                    'value': value,
                    'start': index,
                    'end': index + len(value)
                })
                index += len(value)
                break
        if not match:
            if code[index].isspace():
                index += 1
                continue
            raise ValueError(f"Invalid character: {code[index]}")
    return tokens
