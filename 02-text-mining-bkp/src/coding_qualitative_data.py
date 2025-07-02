def example_coding(texts, code_map):
    # Simples mapeamento de códigos para textos
    coded = {}
    for code, keywords in code_map.items():
        coded[code] = [t for t in texts if any(k in t for k in keywords)]
    return coded
