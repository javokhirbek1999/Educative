from typing import Any

class Course:

    def __init__(self, title) -> None:
        self.title = title

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'Object "{self.title}" is called\n\
            Positional arguments: {args}\n\
            Keywork arguments: {kwds}')

class Course2:

    def __init__(self, title) -> None:
        self.title = title


obj = Course('Mastering the Art of Programming in Python3')
obj('Jeff', 120, 'Awesome', category='Programming', rate='5/5')

obj2 = Course2('Mastering the Art of Programming in C++')

print(f'Is Object 1 callable ? -> {callable(obj)}')
print(f'Is Object 2 callable ? -> {callable(obj2)}')
