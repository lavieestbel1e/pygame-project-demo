class BellTower:
    def __init__(self, *args):
        self.sounds = []
        for elem in args:
            self.sounds.append(elem)

    def append(self, bell):
        self.sounds.append(bell)

    def sound(self):
        for bell in self.sounds:
            bell.sound()
        print('...')


class BigBell(BellTower):
    bell = True

    def sound(self):
        if self.bell:
            print('ding')
            self.bell = False
        else:
            print('dong')
            self.bell = True


class LittleBell(BellTower):
    def sound(self):
        print('ding')


bell_tower = BellTower()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()