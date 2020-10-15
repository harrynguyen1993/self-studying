# pytest: helps you write better programs

- The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

## Installation and Getting Started
  ```
  >>> pip install -U pytest
  >>> pytest --version
  ```
  
## Create your first test
  ```
    class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
  ```
