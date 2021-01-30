import logging

from animal import Animal
from decorator import log



class Cats(Animal):

    def __init__(self):
        self.wool = "短毛哦"
        super().__init__("Tom","蓝色","2岁","雄性")

    @log(logging.INFO)
    def catch(self):
        print(f"{self.name}抓老鼠很厉害")

    def shout(self):
        shout = "喵喵喵"
        print(f"{self.name}叫起来是{shout}")

if __name__ == '__main__':
    cat = Cats()
    cat.run()
    cat.catch()
    cat.shout()

