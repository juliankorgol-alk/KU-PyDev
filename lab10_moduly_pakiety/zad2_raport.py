"""Lab 10 – Zadanie 2 (★): Aplikacja korzystająca z własnego pakietu.

Zaimportuj funkcje z pakietu geometria (spróbuj różnych stylów importu!):
    import geometria
    from geometria import plaskie
    from geometria.plaskie import circle_area
"""
import geometria
from geometria import plaskie
from geometria.plaskie import circle_area


def total_area(shapes):
    """Suma pól figur z listy krotek:
        ("koło", r)
        ("prostokąt", a, b)
        ("trójkąt", a, b, c)
    Nieznane figury pomija.
    """
    total = 0
    for shape in shapes:
        name = shape[0]
        if name == "koło":
            total += circle_area(shape[1])
        elif name == "prostokąt":
            total += plaskie.rectangle_area(shape[1], shape[2])
        elif name == "trójkąt":
            total += geometria.triangle_area(shape[1], shape[2], shape[3])
    return total


if __name__ == "__main__":
    print(f"{total_area([('koło', 1), ('prostokąt', 2, 3)]):.2f}")