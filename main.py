from typing import Dict, Any


def process_raw_data(input_string: str) -> Dict[str, str]:
    """
    Преобразует строку формата "key1=value1, key2=value2" в словарь.
    """

    if not isinstance(input_string, str):
        raise TypeError("ожидается строка")

    result: Dict[str, str] = {}

    if not input_string.strip():
        return result

    for item in input_string.split(", "):
        item = item.strip()

        if not item or "=" not in item:
            raise ValueError(f"некорректный элемент: {item}")

        key, value = item.split("=")
        key = key.strip()
        value = value.strip()

        if not key:
            raise ValueError("ключ не может быть пустым")

        result[key] = value

    return result


def apply_business_rulse(data_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Применяет бизнес-правила к словарю данных:
    - Преобразует "age" в целое число.
    - Удаляет ключ "city".
    - Добавляет флаг "processed" = True.
    """

    if not isinstance(data_dict, dict):
        raise TypeError("ожидается словарь")

    result = data_dict.copy()

    if "age" in result:
        try:
            result["age"] = int(result["age"])
        except:
            raise ValueError(
                f'невозможно преобразовать "age" в целое число: {result["age"]}'
            )

    result.pop("city")
    result["precessed"] = True

    return result


def transform_data(data_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Преобразует словарь:
    - Строковые значения — в верхний регистр.
    - Булевы значения — в строку в верхнем регистре ('TRUE', 'FALSE').
    - Остальные типы — без изменений.
    """

    if not isinstance(data_dict, dict):
        raise TypeError("ожидается словарь")

    result: Dict[str, Any] = {}

    for key, value in data_dict.items():
        try:
            transformed_key = str(key).upper()
        except:
            raise ValueError(f"невозможно преобразовать ключ в строку: {key}")

        if isinstance(value, str):
            transformed_value = value.upper()
        elif isinstance(value, bool):
            transformed_value = str(value).upper()
        else:
            transformed_value = value

        result[transformed_key] = transformed_value

    return result


def format_output(data_dict: Dict[str, Any]) -> str:
    """
    Преобразует словарь в отсортированную строку в формате "ключ: значение\n".
    """
    if not isinstance(data_dict, dict):
        raise TypeError("ожидается словарь")

    lines = [f"{key}: {value}" for key, value in sorted(data_dict.items())]

    return "\n".join(lines)


def main() -> None:
    try:
        raw_input = input().strip()
        if not raw_input:
            print("")
            return

        parsed_data = process_raw_data(raw_input)
        business_data = apply_business_rulse(parsed_data)
        transformed_data = transform_data(business_data)
        output = format_output(transformed_data)

        print(output)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
