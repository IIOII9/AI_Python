class BaseClass:
    def __init__(self, clss_name):
        self.__class_name = clss_name

    def _get_class_name(self):
        return self.__class_name

    def show_info(self):
        print(f"This is a class named {self._get_class_name()}")


obj = BaseClass("BaseClass")
obj.show_info()


class Driver(BaseClass):
    def __init__(self, clss_name):
        super().__init__(clss_name)
        self.__class_name = "DriverClass"

    def show_info(self):
        print("I am a driver")
        super().show_info()


driver_obj = Driver("Driver")
driver_obj.show_info()
