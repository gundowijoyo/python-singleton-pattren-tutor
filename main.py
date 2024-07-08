class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

# Penggunaan
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()

print(singleton1 is singleton2)  # Output: True
