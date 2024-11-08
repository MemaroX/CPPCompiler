import re

# Define token categories
keywords = {"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
            "float", "for", "goto", "if", "inline", "int", "long", "register", "restrict", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while",
            "alignas", "alignof", "and", "and_eq", "asm", "bitand", "bitor", "bool", "catch", "char16_t", "char32_t",
            "class", "compl", "const_cast", "decltype", "delete", "dynamic_cast", "explicit", "export", "false",
            "friend", "mutable", "namespace", "new", "noexcept", "not", "not_eq", "nullptr", "operator", "or", "or_eq",
            "private", "protected", "public", "reinterpret_cast", "static_assert", "static_cast", "template", "this",
            "thread_local", "throw", "true", "try", "typeid", "typename", "using", "virtual", "wchar_t", "xor", "cin",
            "cout", "xor_eq", "include"}

operators = {"+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "^", "~",
             "<<", ">>", "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "?", ":", "->", ".", ".*",
             "->*", "new", "delete", "sizeof", "typeid", "throw", "const_cast", "dynamic_cast", "reinterpret_cast",
             "static_cast"}

special_characters = {"{", "}", "(", ")", "[", "]", ";", ",", ".", "->", "::", "#"}

# Define token patterns with distinct patterns for single-line and multi-line comments
token_patterns = [
    ("COMMENT", r'//[^\n]*|/\*[\s\S]*?\*/'),  # Distinguish single-line and multi-line comments
    ('WHITESPACE', r'\s+'),
    ("KEYWORD", r'\b(' + '|'.join(keywords) + r')\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
    ('OPERATOR', r'[\+\-\*/%=&|<>!]+'),
    ('CHARACTER_CONSTANT', r"'.'"),
    ('NUMERIC_CONSTANT', r'\b\d+(\.\d+)?\b'),
    ('SPECIAL_CHARACTER', r'|'.join(re.escape(p) for p in special_characters))
]

# Combine patterns into a regex
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
