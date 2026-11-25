import os
from hashlib import file_digest
from pathlib import Path
from shutil import copyfile


def sha256(path: Path) -> bytes:
    with path.open("rb") as image:
        return file_digest(image, "sha256").digest()


def main() -> None:
    source = Path(__file__).resolve().with_name("entry.png")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / source.name
    copyfile(source, destination)

    if sha256(source) != sha256(destination):
        raise RuntimeError(f"SHA-256 mismatch after copying to {destination}")
    print(f"Verified {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
