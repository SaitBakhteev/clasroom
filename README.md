### Шаг 1. Создайте папку для задания task.
### Шаг 2. Внутри этой папки создайте файл solution.py и вставьте в него заготовку ниже. Допишите реализацию функции вместо pass.
### Шаг 3. В той же папке создайте файл test_solution.py и вставьте в него тесты ниже. ‼️ Этот файл менять нельзя — он используется для проверки вашей работы.
### Шаг 4. Откройте терминал в этой папке и запустите тесты командой:

```bash
python test_solution.py
```

### Шаг 5. Если все тесты прошли — вы увидите OK. Если что-то не так — увидите FAILED и описание, какой именно тест не прошел.


# Задания и тесты к ним

## 📘 Задание 1. Объединение (Union)

```python
def union(r1: list[dict], r2: list[dict]) -> list[dict]:
    """
    Возвращает объединение двух отношений.

    Требования:
    - r1 и r2 — списки словарей (кортежей).
    - Отношения должны быть совместимы: одинаковый набор ключей
      и одинаковые типы значений для каждого ключа.
    - Если совместимость нарушена — выбросить ValueError.
    - Результат не содержит дубликатов.
    - Порядок кортежей в результате не важен.

    Пример:
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 2, "name": "B"}]
        union(r1, r2) ->
            [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    """
    # Ваш код здесь
    pass
```
## 📘 Тест задания 1. Объединение (Union)

```python
import unittest
from solution import task


def normalize(relation):
    """Приводит отношение к виду, не зависящему от порядка кортежей."""
    return sorted(tuple(sorted(d.items())) for d in relation)


class TestUnion(unittest.TestCase):

    def test_basic(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 2, "name": "B"}, {"id": 3, "name": "C"}]
        result = union(r1, r2)
        expected = [{"id": 1, "name": "A"},
                    {"id": 2, "name": "B"},
                    {"id": 3, "name": "C"}]
        self.assertEqual(normalize(result), normalize(expected))

    def test_no_common_tuples(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 2, "name": "B"}]
        result = union(r1, r2)
        expected = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        self.assertEqual(normalize(result), normalize(expected))

    def test_all_tuples_common(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        result = union(r1, r2)
        self.assertEqual(normalize(result), normalize(r1))

    def test_duplicates_inside_r1(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 1, "name": "A"}]
        r2 = [{"id": 2, "name": "B"}]
        result = union(r1, r2)
        expected = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        self.assertEqual(normalize(result), normalize(expected))

    def test_duplicates_across_relations(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "name": "A"}]
        result = union(r1, r2)
        self.assertEqual(normalize(result), normalize(r1))

    def test_empty_r1(self):
        r2 = [{"id": 1, "name": "A"}]
        result = union([], r2)
        self.assertEqual(normalize(result), normalize(r2))

    def test_empty_r2(self):
        r1 = [{"id": 1, "name": "A"}]
        result = union(r1, [])
        self.assertEqual(normalize(result), normalize(r1))

    def test_both_empty(self):
        self.assertEqual(union([], []), [])

    def test_incompatible_different_keys(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "age": 20}]
        with self.assertRaises(ValueError):
            union(r1, r2)

    def test_incompatible_different_count(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "name": "A", "age": 20}]
        with self.assertRaises(ValueError):
            union(r1, r2)

    def test_incompatible_different_types(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": "1", "name": "A"}]
        with self.assertRaises(ValueError):
            union(r1, r2)


if __name__ == "__main__":
    unittest.main()

```

## 📘 Задание 2. Пересечение (Intersection)
```python
def intersection(r1: list[dict], r2: list[dict]) -> list[dict]:
    """
    Возвращает пересечение двух отношений.

    Требования:
    - r1 и r2 — списки словарей (кортежей).
    - Отношения должны быть совместимы: одинаковый набор ключей
      и одинаковые типы значений для каждого ключа.
    - Если совместимость нарушена — выбросить ValueError.
    - В результат попадают только полностью совпадающие кортежи.
    - Дубликаты не допускаются.
    - Порядок кортежей в результате не важен.

    Пример:
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 2, "name": "B"}, {"id": 3, "name": "C"}]
        intersection(r1, r2) -> [{"id": 2, "name": "B"}]
    """
    # Ваш код здесь
    pass
```

## 📘 Тест задания 2. Пересечение (Intersection)

```python
import unittest
from solution import task


def normalize(relation):
    return sorted(tuple(sorted(d.items())) for d in relation)


class TestIntersection(unittest.TestCase):

    def test_basic(self):
        r1 = [{"id": 1, "name": "A"},
              {"id": 2, "name": "B"},
              {"id": 3, "name": "C"}]
        r2 = [{"id": 2, "name": "B"},
              {"id": 3, "name": "C"},
              {"id": 4, "name": "D"}]
        result = intersection(r1, r2)
        expected = [{"id": 2, "name": "B"}, {"id": 3, "name": "C"}]
        self.assertEqual(normalize(result), normalize(expected))

    def test_no_common_tuples(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 2, "name": "B"}]
        self.assertEqual(intersection(r1, r2), [])

    def test_all_tuples_common(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        result = intersection(r1, r2)
        self.assertEqual(normalize(result), normalize(r1))

    def test_duplicates_inside_r1(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 1, "name": "A"}]
        r2 = [{"id": 1, "name": "A"}]
        result = intersection(r1, r2)
        self.assertEqual(normalize(result),
                         normalize([{"id": 1, "name": "A"}]))

    def test_empty_r1(self):
        r2 = [{"id": 1, "name": "A"}]
        self.assertEqual(intersection([], r2), [])

    def test_empty_r2(self):
        r1 = [{"id": 1, "name": "A"}]
        self.assertEqual(intersection(r1, []), [])

    def test_both_empty(self):
        self.assertEqual(intersection([], []), [])

    def test_incompatible_different_keys(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "age": 20}]
        with self.assertRaises(ValueError):
            intersection(r1, r2)

    def test_incompatible_different_count(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "name": "A", "age": 20}]
        with self.assertRaises(ValueError):
            intersection(r1, r2)

    def test_incompatible_different_types(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": "1", "name": "A"}]
        with self.assertRaises(ValueError):
            intersection(r1, r2)


if __name__ == "__main__":
    unittest.main()
```

## 📘 Задание 3. Разность (Difference)
```python
def difference(r1: list[dict], r2: list[dict]) -> list[dict]:
    """
    Возвращает разность r1 - r2.

    Требования:
    - r1 и r2 — списки словарей (кортежей).
    - Отношения должны быть совместимы: одинаковый набор ключей
      и одинаковые типы значений для каждого ключа.
    - Если совместимость нарушена — выбросить ValueError.
    - В результат попадают кортежи, которые есть в r1,
      но отсутствуют в r2.
    - Дубликаты не допускаются.
    - Операция НЕ коммутативна: difference(A, B) != difference(B, A).
    - Порядок кортежей в результате не важен.

    Пример:
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 2, "name": "B"}]
        difference(r1, r2) -> [{"id": 1, "name": "A"}]
    """
    # Ваш код здесь
    pass
```
## 📘 Тесты задания 3. Разность (Difference)
```python
import unittest
from solution import difference


def normalize(relation):
    return sorted(tuple(sorted(d.items())) for d in relation)


class TestDifference(unittest.TestCase):

    def test_basic(self):
        r1 = [{"id": 1, "name": "A"},
              {"id": 2, "name": "B"},
              {"id": 3, "name": "C"}]
        r2 = [{"id": 2, "name": "B"}]
        result = difference(r1, r2)
        expected = [{"id": 1, "name": "A"}, {"id": 3, "name": "C"}]
        self.assertEqual(normalize(result), normalize(expected))

    def test_all_removed(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        self.assertEqual(difference(r1, r2), [])

    def test_nothing_removed(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 2, "name": "B"}]
        result = difference(r1, r2)
        self.assertEqual(normalize(result), normalize(r1))

    def test_not_commutative(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        r2 = [{"id": 2, "name": "B"}, {"id": 3, "name": "C"}]
        result_ab = difference(r1, r2)
        result_ba = difference(r2, r1)
        self.assertEqual(normalize(result_ab),
                         normalize([{"id": 1, "name": "A"}]))
        self.assertEqual(normalize(result_ba),
                         normalize([{"id": 3, "name": "C"}]))

    def test_duplicates_inside_r1(self):
        r1 = [{"id": 1, "name": "A"}, {"id": 1, "name": "A"}]
        r2 = []
        result = difference(r1, r2)
        self.assertEqual(normalize(result),
                         normalize([{"id": 1, "name": "A"}]))

    def test_empty_r1(self):
        r2 = [{"id": 1, "name": "A"}]
        self.assertEqual(difference([], r2), [])

    def test_empty_r2(self):
        r1 = [{"id": 1, "name": "A"}]
        result = difference(r1, [])
        self.assertEqual(normalize(result), normalize(r1))

    def test_both_empty(self):
        self.assertEqual(difference([], []), [])

    def test_incompatible_different_keys(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "age": 20}]
        with self.assertRaises(ValueError):
            difference(r1, r2)

    def test_incompatible_different_count(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": 1, "name": "A", "age": 20}]
        with self.assertRaises(ValueError):
            difference(r1, r2)

    def test_incompatible_different_types(self):
        r1 = [{"id": 1, "name": "A"}]
        r2 = [{"id": "1", "name": "A"}]
        with self.assertRaises(ValueError):
            difference(r1, r2)


if __name__ == "__main__":
    unittest.main()
```
