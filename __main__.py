import json
from pathlib import Path

# Путь для сохранения proof
proof_file = Path("proofs.json")

# Пример данных proof
proof_data = {
    "user": "Anna",
    "token": "ADT",
    "contribution": "Initial setup",
    "status": "completed"
}

# Сохраняем в JSON
with open(proof_file, "w", encoding="utf-8") as f:
    json.dump(proof_data, f, indent=4)

print(f"✅ Proof generated successfully: {proof_file}")
