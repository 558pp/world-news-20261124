import hashlib
import os
import shutil
from pathlib import Path


def sha256(path: Path) -> bytes:
    with path.open("rb") as file:
        return hashlib.sha256(file.read()).digest()


def main() -> None:
    source = Path(__file__).resolve().with_name("entry.png")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / source.name
    if destination.resolve() != source:
        shutil.copyfile(source, destination)
    if sha256(source) != sha256(destination):
        raise OSError(f"SHA-256 mismatch for {destination}")
    print(f"Verified {destination.name} ({destination.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
