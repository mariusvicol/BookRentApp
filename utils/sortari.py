def merge_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Parcurge lista și compară elementele consecutive. Schimbă-le pozițiile dacă nu sunt în ordine corectă.
    Repetă acest proces până când lista este sortată complet.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half, key=key, cmp=cmp, reverse=reverse)
        merge_sort(right_half, key=key, cmp=cmp, reverse=reverse)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            left_value = key(left_half[i]) if key is not None else left_half[i]
            right_value = key(right_half[j]) if key is not None else right_half[j]

            if (not reverse and cmp(left_value, right_value)) or (
                    reverse and not cmp(left_value, right_value)):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def bingo_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Bingo Sort este un algoritm de sortare simplu care găsește cel mai mic element din listă și îl plasează pe prima poziție.
    Procesul se repetă pentru a găsi și așeza următorul cel mai mic element până când întreaga listă este sortată.
    """
    if len(arr) > 0:
        items_with_keys = [(element, key(element) if key else element) for element in arr]
        bingo = min(items_with_keys, key=lambda x: x[1])
        largest = max(items_with_keys, key=lambda x: x[1])

        next_bingo = largest
        next_pos = 0

        while cmp(bingo[1], next_bingo[1]):
            start_pos = next_pos
            for i in range(start_pos, len(items_with_keys)):
                if items_with_keys[i] == bingo:
                    items_with_keys[i], items_with_keys[next_pos] = items_with_keys[next_pos], items_with_keys[i]
                    next_pos += 1
                elif cmp(items_with_keys[i][1], next_bingo[1]):
                    next_bingo = items_with_keys[i]

            bingo = next_bingo
            next_bingo = largest

        sorted_arr = [item[0] for item in items_with_keys]

        if reverse:
            sorted_arr.reverse()
    else:
        sorted_arr = []

    return sorted_arr


def bubble_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Parcurge lista și compară elementele consecutive. Schimbă-le pozițiile dacă nu sunt în ordine corectă.
    Repetă acest proces până când lista este sortată complet.
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            compare_result = cmp(key(arr[j]), key(arr[j + 1])) if not reverse else not cmp(key(arr[j]), key(arr[j + 1]))
            if compare_result:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Construiește lista sortată un element la un moment dat. Inserează fiecare element în poziția corectă, comparându-l cu elementele din lista sortată.
    """
    n = len(arr)

    for i in range(1, n):
        current_element = arr[i]
        j = i - 1

        while j >= 0 and (
                cmp(key(current_element), key(arr[j])) if not reverse else not cmp(key(current_element), key(arr[j]))):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_element
    return arr


def quick_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Alege un pivot, împarte lista în două subliste (mai mici și mai mari decât pivotul), și aplică recursiv Quick Sort pe ambele subliste.
    Concatenează subliste și pivotul pentru a obține lista sortată.
    """

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Alegem pivotul ca mijloc al listei

    left = [x for x in arr if cmp(key(x) if key else x, key(pivot) if key else pivot)]  # Elemente mai mici decât pivot
    middle = [x for x in arr if (key(x) if key else x) == (key(pivot) if key else pivot)]  # Elemente egale cu pivot
    right = [x for x in arr if
             cmp(key(x) if key else x, key(pivot) if key else pivot) is False]  # Elemente mai mari decât pivot

    sorted_left = quick_sort(left, key, cmp, reverse)
    sorted_right = quick_sort(right, key, cmp, reverse)

    if reverse:
        return sorted_right + middle + sorted_left
    else:
        return sorted_left + middle + sorted_right


def selection_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
        Parcurge lista și găsește cel mai mic element. Schimbă-l cu primul element al listei. Repetă acest proces pentru restul listei.
    """
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            compare_result = cmp(key(arr[j]), key(arr[min_index])) if not reverse else not cmp(key(arr[j]),
                                                                                               key(arr[min_index]))
            if compare_result:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def shell_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Impune distanțe între elemente și aplică sortare prin inserție la fiecare pas. Reduce treptat distanțele pentru a îmbunătăți eficiența.
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and cmp(key(arr[j - gap]) if key else arr[j - gap], key(temp) if key else temp):
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    if reverse:
        arr.reverse()

    return arr


def comb_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Este o variantă a Bubble Sort care utilizează un factor de reducere pentru a ajusta distanțele dintre elemente.
    Compară și interschimbă elemente la distanțe specifice.
    """
    n = len(arr)
    gap = n
    shrink_factor = 1.3

    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for i in range(n - gap):
            compare_result = cmp(key(arr[i]) if key else arr[i], key(arr[i + gap]) if key else arr[i + gap])
            if (reverse and compare_result) or (not reverse and not compare_result):
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr


def gnome_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Parcurge lista și compară elementele consecutive. Dacă găsește elemente în ordine greșită, le interschimbă și revine pentru a verifica elementul anterior.
    """
    n = len(arr)
    index = 0

    while index < n:
        if index == 0 or cmp(key(arr[index]) if key else arr[index], key(arr[index - 1]) if key else arr[index - 1]):
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    if reverse:
        arr.reverse()

    return arr


def shake_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False):
    """
    Este o variantă a Bubble Sort care parcurge lista în ambele direcții. Sortează elementele din ambele capete ale listei.
    """
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped and start < end:
        swapped = False

        for i in range(start, end):
            compare_result = cmp(key(arr[i]) if key else arr[i], key(arr[i + 1]) if key else arr[i + 1])
            if (reverse and compare_result) or (not reverse and not compare_result):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        end -= 1

        for i in range(end, start, -1):
            compare_result = cmp(key(arr[i - 1]) if key else arr[i - 1], key(arr[i]) if key else arr[i])
            if (reverse and compare_result) or (not reverse and not compare_result):
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1

    return arr


def generic_sort(arr, key=None, cmp=lambda x, y: x <= y, reverse=False, algorithm='merge_sort'):
    if algorithm == 'merge_sort':
        merge_sort(arr, key, cmp, reverse)
    elif algorithm == 'bingo_sort':
        arr = bingo_sort(arr, key, cmp, reverse)
    elif algorithm == 'bubble_sort':
        arr = bubble_sort(arr, key, cmp, reverse)
    elif algorithm == 'insertion_sort':
        arr = insertion_sort(arr, key, cmp, reverse)
    elif algorithm == 'quick_sort':
        arr = quick_sort(arr, key, cmp, reverse)
    elif algorithm == 'selection_sort':
        arr = selection_sort(arr, key, cmp, reverse)
    elif algorithm == 'shell_sort':
        arr = shell_sort(arr, key, cmp, reverse)
    elif algorithm == 'comb_sort':
        arr = comb_sort(arr, key, cmp, reverse)
    elif algorithm == 'gnome_sort':
        arr = gnome_sort(arr, key, cmp, reverse)
    elif algorithm == 'shake_sort':
        arr = shake_sort(arr, key, cmp, reverse)
    else:
        raise ValueError("Algoritm invalid.")
    return arr


def test_merge_sort():
    # Testeaza sortarea unei liste de numere în ordine crescatoare
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr1)
    assert arr1 == [3, 9, 10, 27, 38, 43, 82]

    # Testeaza sortarea unei liste de numere în ordine descrescatoare
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr2, reverse=True)
    assert arr2 == [82, 43, 38, 27, 10, 9, 3]

    # Testeaza sortarea unei liste de cuvinte în ordine crescătoare de lungime
    arr3 = ["apple", "banana", "cherry", "date", "fig"]
    merge_sort(arr3, key=lambda x: len(x))
    assert arr3 == ["fig", "date", "apple", "banana", "cherry"]

    # Testeaza sortarea unei liste de numere in ordine crescatoare cu functie de comparație personalizata
    arr4 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr4, cmp=lambda x, y: x % 10 < y % 10)
    assert arr4 == [10, 82, 3, 43, 27, 38, 9]

    # Testeaza soartarea unei liste vide
    arr5 = []
    merge_sort(arr5)
    assert arr5 == []


test_merge_sort()


def test_bingo_sort():
    # Testeaza sortarea unei liste de numere în ordine crescatoare
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    result1 = bingo_sort(arr1)
    assert result1 == [3, 9, 10, 27, 38, 43, 82]

    # Testeaza sortarea unei liste de numere în ordine descrescatoare
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    result2 = bingo_sort(arr2, reverse=True)
    assert result2 == [82, 43, 38, 27, 10, 9, 3]

    # Testeaza sortarea unei liste de cuvinte în ordine crescatoare de lungime
    arr3 = ["apple", "banana", "cherry", "date", "fig"]
    result3 = bingo_sort(arr3, key=lambda x: len(x))
    assert result3 == ["fig", "date", "apple", "banana", "cherry"]

    # Testeaza sortarea unei liste cu un singur element
    arr6 = [42]
    result6 = bingo_sort(arr6)
    assert result6 == [42]

    # Testeaza sortarea unei liste vide
    arr8 = []
    result8 = bingo_sort(arr8)
    assert result8 == []

    # Testeaza sortarea unei liste cu elemente identice
    arr7 = [5, 5, 5, 5, 5]
    result7 = bingo_sort(arr7)
    assert result7 == [5, 5, 5, 5, 5]


test_bingo_sort()


def test_selection_sort():
    # Testeaza sortarea unei liste de numere în ordine crescatoare
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    result1 = selection_sort(arr1)
    assert result1 == [3, 9, 10, 27, 38, 43, 82]

    # Testeaza sortarea unei liste de numere în ordine descrescatoare
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    result2 = selection_sort(arr2, reverse=True)
    assert result2 == [82, 43, 38, 27, 10, 9, 3]

    # Testeaza sortarea unei liste de cuvinte în ordine crescatoare de lungime
    arr3 = ["apple", "banana", "cherry", "date", "fig"]
    result3 = selection_sort(arr3, key=lambda x: len(x))
    assert result3 == ["fig", "date", "apple", "banana", "cherry"]

    # Testeaza sortarea unei liste cu un singur element
    arr6 = [42]
    result6 = selection_sort(arr6)
    assert result6 == [42]

    # Testeaza sortarea unei liste vide
    arr8 = []
    result8 = selection_sort(arr8)
    assert result8 == []

    # Testeaza sortarea unei liste cu elemente identice
    arr7 = [5, 5, 5, 5, 5]
    result7 = selection_sort(arr7)
    assert result7 == [5, 5, 5, 5, 5]


test_selection_sort()


def test_quick_sort():
    # Testeaza sortarea unei liste de numere în ordine crescatoare
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    result1 = quick_sort(arr1)
    assert result1 == [3, 9, 10, 27, 38, 43, 82]

    # Testeaza sortarea unei liste de numere în ordine descrescatoare
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    result2 = quick_sort(arr2, reverse=True)
    assert result2 == [82, 43, 38, 27, 10, 9, 3]

    # Testeaza sortarea unei liste de cuvinte în ordine crescatoare de lungime
    arr3 = ["apple", "banana", "cherry", "date", "fig"]
    result3 = quick_sort(arr3, key=lambda x: len(x))
    assert result3 == ["fig", "date", "apple", "banana", "cherry"]

    # Testeaza sortarea unei liste cu un singur element
    arr6 = [42]
    result6 = quick_sort(arr6)
    assert result6 == [42]

    # Testeaza sortarea unei liste vide
    arr8 = []
    result8 = quick_sort(arr8)
    assert result8 == []

    # Testeaza sortarea unei liste cu elemente identice
    arr7 = [5, 5, 5, 5, 5]
    result7 = quick_sort(arr7)
    assert result7 == [5, 5, 5, 5, 5]


test_quick_sort()

def test_insertion_sort():
    # Testeaza sortarea unei liste de numere în ordine crescatoare
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    result1 = insertion_sort(arr1)
    assert result1 == [3, 9, 10, 27, 38, 43, 82]

    # Testeaza sortarea unei liste de numere în ordine descrescatoare
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    result2 = insertion_sort(arr2, reverse=True)
    assert result2 == [82, 43, 38, 27, 10, 9, 3]

    # Testeaza sortarea unei liste de cuvinte în ordine crescatoare de lungime
    arr3 = ["apple", "banana", "cherry", "date", "fig"]
    result3 = insertion_sort(arr3, key=lambda x: len(x))
    assert result3 == ["fig", "date", "apple", "banana", "cherry"]

    # Testeaza sortarea unei liste cu un singur element
    arr6 = [42]
    result6 = insertion_sort(arr6)
    assert result6 == [42]

    # Testeaza sortarea unei liste vide
    arr8 = []
    result8 = insertion_sort(arr8)
    assert result8 == []

    # Testeaza sortarea unei liste cu elemente identice
    arr7 = [5, 5, 5, 5, 5]
    result7 = insertion_sort(arr7)
    assert result7 == [5, 5, 5, 5, 5]


test_insertion_sort()


def test_bubble_sort():
    # Testeaza sortarea unei liste de numere în ordine crescatoare
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    result1 = bubble_sort(arr1)
    assert result1 == [3, 9, 10, 27, 38, 43, 82]

    # Testeaza sortarea unei liste de numere în ordine descrescatoare
    arr2 = [38, 27, 43, 3, 9, 82, 10]
    result2 = bubble_sort(arr2, reverse=True)
    assert result2 == [82, 43, 38, 27, 10, 9, 3]

    # Testeaza sortarea unei liste de cuvinte în ordine crescatoare de lungime
    arr3 = ["apple", "banana", "cherry", "date", "fig"]
    result3 = bubble_sort(arr3, key=lambda x: len(x))
    assert result3 == ["fig", "date", "apple", "banana", "cherry"]

    # Testeaza sortarea unei liste cu un singur element
    arr6 = [42]
    result6 = bubble_sort(arr6)
    assert result6 == [42]

    # Testeaza sortarea unei liste vide
    arr8 = []
    result8 = bubble_sort(arr8)
    assert result8 == []

    # Testeaza sortarea unei liste cu elemente identice
    arr7 = [5, 5, 5, 5, 5]
    result7 = bubble_sort(arr7)
    assert result7 == [5, 5, 5, 5, 5]


test_bubble_sort()
