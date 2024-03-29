# Python Static Types
def add(a: int, b: int) -> int:
    return a + b

def to_upper_everything(coll: list[str]) -> list[str]:
    return [x.upper() for x in coll]

def main() -> None:
    print(add(13939, 20))

if __name__ == "__main__":
    l = ["abc", "def"]

    print(to_upper_everything(l))
    main()