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
