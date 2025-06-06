class ParseError(Exception):
    pass

# parser fonksiyonu
def parse(tokens):
    pos = 0
    variables = {}

    def expect(token_type, token_value=None):
        nonlocal pos
        if pos >= len(tokens) or tokens[pos]['type'] != token_type:
            raise ParseError(f"Expected '{token_type}'.")
        if token_value is not None and tokens[pos]['value'] != token_value:
            raise ParseError(f"Expected '{token_value}'.")
        pos += 1

    def parse_expression():
        nonlocal pos
        val = parse_term()
        while pos < len(tokens) and tokens[pos]['type'] == 'OPERATOR' and tokens[pos]['value'] in ('+', '-'):
            op = tokens[pos]['value']
            pos += 1
            right = parse_term()
            if op == '+':
                val += right
            else:
                val -= right
        return val

    def parse_term():
        nonlocal pos
        val = parse_factor()
        while pos < len(tokens) and tokens[pos]['type'] == 'OPERATOR' and tokens[pos]['value'] in ('*', '/'):
            op = tokens[pos]['value']
            pos += 1
            right = parse_factor()
            if op == '*':
                val *= right
            else:
                val /= right
        return val

    def parse_factor():
        nonlocal pos
        if pos >= len(tokens):
            raise ParseError("Unexpected end of input.")
        tok = tokens[pos]
        if tok['type'] == 'NUMBER':
            pos += 1
            return int(tok['value'])
        elif tok['type'] == 'IDENTIFIER':
            pos += 1
            if tok['value'] in variables:
                return variables[tok['value']]
            else:
                raise ParseError(f"Undefined variable: '{tok['value']}'")
        elif tok['type'] == 'PAREN' and tok['value'] == '(':
            pos += 1
            val = parse_expression()
            expect('PAREN', ')')
            return val
        else:
            raise ParseError(f"Unexpected token: '{tok['value']}'")

    results = []
    while pos < len(tokens):
        if pos + 2 < len(tokens) and tokens[pos]['type'] == 'IDENTIFIER' and tokens[pos + 1]['type'] == 'EQUALS':
            var_name = tokens[pos]['value']
            pos += 2
            val = parse_expression()
            variables[var_name] = val
            if pos < len(tokens) and tokens[pos]['type'] == 'DELIMITER':
                pos += 1
        else:
            val = parse_expression()
            if pos >= len(tokens) or tokens[pos]['type'] != 'EQUALS':
                raise ParseError(f"Expected '=' for value: {val}")
            pos += 1
            if pos >= len(tokens) or tokens[pos]['type'] != 'QUESTION':
                raise ParseError("Expected '?'")
            pos += 1
            results.append(f"? = {val}")
            if pos < len(tokens) and tokens[pos]['type'] == 'DELIMITER':
                pos += 1

    return results