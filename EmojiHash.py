import itertools
import json
from typing import Any, Union

class EmojiHash:
    EMOJIS = '😀😃😄😁😆😅😂😊😇😉😌😍😘😗😙😚😋😜😝😛😎😏😒😞😔😖😫😩😤😠😡😢😣😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏'

    def __init__(self, length: int = 32):
        self.length = length

    def _compute_hash(self, data: bytes) -> int:
        hash_value = 0
        for byte in data:
            hash_value = (hash_value * 31 + byte) % len(self.EMOJIS)
        return hash_value

    def _generate_emoji_hash(self, hash_value: int) -> str:
        hash_sequence = itertools.islice(itertools.cycle(self.EMOJIS), hash_value, hash_value + self.length)
        return ''.join(hash_sequence)

    def hash_string(self, input_str: str) -> str:
        hash_value = self._compute_hash(input_str.encode('utf-8'))
        return self._generate_emoji_hash(hash_value)

    def hash_bytes(self, input_bytes: bytes) -> str:
        hash_value = self._compute_hash(input_bytes)
        return self._generate_emoji_hash(hash_value)

    def hash_file(self, file_path: str) -> str:
        hash_value = 0
        with open(file_path, 'rb') as f:
            while (chunk := f.read(8192)):
                hash_value = self._compute_hash(chunk)
        return self._generate_emoji_hash(hash_value)

    def hash_object(self, input_object: Any) -> str:
        input_bytes = json.dumps(input_object, default=str, ensure_ascii=False).encode('utf-8')
        return self.hash_bytes(input_bytes)
