class Camera:
    def take_photo(self):
        print("Photo Taken")
class Phone(Camera):
    def make_call(self):
        print("Calling...")
    def take_photo(self):
        print("Photo Taken ")


class SmartPhone(Camera):
    def browse(self):

        print("Browsing the internet ")
    def take_photo(self):
        super().take_photo()
ph1 = SmartPhone()

ph1.take_photo()



