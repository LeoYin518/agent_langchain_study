def demo01():
    sentence = "Hello from agent-study!"
    print(sentence.split(" "))
    print(sentence.strip())


def demo02():
    names = ["hello", "  tom", "my", "darling"]
    arr = [name.strip() for name in names]
    print(arr)


if __name__ == "__main__":
    demo02()
