import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from database import engine, Base


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
