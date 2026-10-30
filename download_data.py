"""MovieLens 1M 데이터셋을 내려받아 data/ 폴더에 movies.dat, ratings.dat, users.dat 를 둔다."""
import io
import urllib.request
import zipfile
from pathlib import Path

URL = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
DATA_DIR = Path(__file__).resolve().parent / "data"
FILES = ["movies.dat", "ratings.dat", "users.dat"]


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    if all((DATA_DIR / f).exists() for f in FILES):
        print("이미 다운로드되어 있습니다:", DATA_DIR)
        return
    print("다운로드 중:", URL)
    with urllib.request.urlopen(URL) as resp:
        buf = io.BytesIO(resp.read())
    with zipfile.ZipFile(buf) as zf:
        for name in zf.namelist():
            base = Path(name).name
            if base in FILES:
                (DATA_DIR / base).write_bytes(zf.read(name))
                print("저장:", DATA_DIR / base)
    print("완료")


if __name__ == "__main__":
    main()
