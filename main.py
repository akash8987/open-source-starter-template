class Application:
    def __init__(self, name):
        self.name = name

    def run(self):
        self._initialize()

    def _initialize(self):
        pass


def main():
    app = Application("OpenSourceApp")
    app.run()


if __name__ == "__main__":
    main()
