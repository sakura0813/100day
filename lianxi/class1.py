import abc
import random


class Fighter(object, metaclass=abc.ABCMeta):
    __slots__ = ("_name", "_hp")

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if hp >= 0:
            self._hp = hp
        else:
            self._hp = 0

    @property
    def alive(self):
        return self._hp > 0

    @abc.abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ("_name", "_hp", "_mp")

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp = other.hp - random.randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp = self._mp - 50
            injury = other.hp * 3 // 4
            if injury >= 50:
                injury = injury
            else:
                injury = 50
            other.hp = other.hp - injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp = self._mp - 20
            for temp in others:
                if temp.alive:
                    temp.hp = temp.hp - random.randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = random.randint(1, 10)
        self._mp = self._mp + incr_point
        return incr_point

    def __str__(self):
        return "~~~{0}奥特曼~~~\n生命值：{1}\n魔法值：{2}".format(self._name, self._hp,
                                                       self._mp)


class Monster(Fighter):
    __slots__ = ("_name", "_hp")

    def attack(self, other):
        other.hp = other.hp - random.randint(10, 20)

    def __str__(self):
        return "~~~{0}小怪兽~~~\n生命值：{1}\n".format(self._name, self._hp)


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = random.randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end="")


def main():
    u = Ultraman("sakura", 600, 700)
    m1 = Monster("迪达拉", 300)
    m2 = Monster("埃里克", 400)
    m3 = Monster("尼克", 700)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print("============第{0}回合============".format(fight_round))
        m = select_alive_one(ms)
        skill = random.randint(1, 10)
        if skill <= 6:
            print("{0}使用了普通攻击打了{1}".format(u.name, m.name))
            u.attack(m)
            print("{0}的魔法值恢复了{1}点".format(u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print("{0}使用魔法成功".format(u.name))
            else:
                print("{0}使用魔法失败！".format(u.name))
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            print("{0}回击了{1}".format(m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
        print("======战斗结束！======\n")

    if u.alive > 0:
        print("{0}奥特曼胜利！".format(u.name))
    else:
        print("怪兽胜利！")


if __name__ == "__main__":
    main()