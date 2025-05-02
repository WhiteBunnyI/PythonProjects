from config import filename
from task2 import huffman

def lzw_compress(text):
    # Инициализация словаря ASCII символов (0-255)
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256  # Следующий доступный код
    current_str = ""  # Текущая строка
    compressed_data = []  # Сжатые данные (коды)

    for char in text:
        current_str += char
        # Если текущей строки нет в словаре, добавляем ее
        if current_str not in dictionary:
            compressed_data.append(dictionary[current_str[:-1]])
            dictionary[current_str] = next_code
            next_code += 1
            current_str = char  # Начинаем новую строку с текущего символа

    # Добавляем последнюю оставшуюся строку
    if current_str:
        compressed_data.append(dictionary[current_str])
    print(dictionary)
    return compressed_data

def calculate_bits(compressed_data, bit_length):
    return len(compressed_data) * bit_length

def main():
    # Чтение текста из файла
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().replace('\n', ' ')  # Заменяем переносы на пробелы

    # Проверка уникальных символов
    unique_chars = set(text)
    print(f"Уникальных символов: {len(unique_chars)} (должно быть <= 64)")

    # Сжимаем текст алгоритмом LZW
    compressed = lzw_compress(text)
    
    # Вычисляем битовую длину для разных методов
    lzw_bits = calculate_bits(compressed, 12)  # Предполагаем 12 бит на код
    uniform_bits = len(text) * 6  # 6 бит на символ
    huffman_bits = huffman()[0]  # Здесь нужно подставить результат из задачи 2
    
    print(f"Длина исходного текста: {len(text)} символов")
    print(f"LZW: {lzw_bits} бит ({len(compressed)} кодов по 12 бит)")
    print(f"Равномерный код: {uniform_bits} бит")
    print(f"Коэффициент сжатия LZW/Равномерный: {lzw_bits/uniform_bits:.2f}")
    print(f"Коэффициент сжатия LZW/Хаффман: {lzw_bits/huffman_bits:.2f}")

if __name__ == "__main__":
    main()
