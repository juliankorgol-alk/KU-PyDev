"""Kolokwium I – PRZYKŁAD 3 (algorytm): Kompresja RLE i anagramy."""


def compress(text):
    """Kodowanie długości serii (Run-Length Encoding): "aaabcc" -> "a3b1c2"."""
    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        count = 0
        while i < len(text) and text[i] == char:
            count += 1
            i += 1
        result += f"{char}{count}"
    return result


def decompress(code):
    """Odwrotność compress: "a3b1c2" -> "aaabcc". Liczba może mieć kilka cyfr: "x12"."""
    result = ""
    i = 0
    while i < len(code):
        char = code[i]
        i += 1
        digits = ""
        while i < len(code) and code[i].isdigit():
            digits += code[i]
            i += 1
        result += char * int(digits)
    return result


def are_anagrams(first, second):
    """Czy teksty składają się z tych samych liter? Pomija wielkość liter i spacje."""
    first_letters = sorted(first.lower().replace(" ", ""))
    second_letters = sorted(second.lower().replace(" ", ""))
    return first_letters == second_letters