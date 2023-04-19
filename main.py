from EmojiHash import EmojiHash

input_data = "Пример данных для хеширования"
input_bytes = b"Some bytes to hash"
input_file = "example.txt"
input_object = {"key": "value", "number": 42}

emoji_hasher = EmojiHash()

# Хеширование строки
string_hash = emoji_hasher.hash_string(input_data)
print(f"String hash: {string_hash}")

# Хеширование байт
bytes_hash = emoji_hasher.hash_bytes(input_bytes)
print(f"Bytes hash: {bytes_hash}")

# Создание файла с некоторым содержимым для хеширования
with open(input_file, "w") as f:
    f.write("Example file content for hashing\n")

# Хеширование файла
file_hash = emoji_hasher.hash_file(input_file)
print(f"File hash: {file_hash}")

# Хеширование объекта
object_hash = emoji_hasher.hash_object(input_object)
print(f"Object hash: {object_hash}")
