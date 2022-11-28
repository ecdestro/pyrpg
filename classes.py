class Inn:
    def __init__(self, id = 0, innKeeper = "", innName = "", level = 0, gold = 0, patronCap = 0) -> None: 
        self._id = id
        self._innKeeper = innKeeper
        self._innName = innName
        self._level = level
        self._gold = gold
        self._patronCap = patronCap
    def __repr__(self) -> str:
        return "Inn id:% s innKeeper:% s innName:% s level:% s gold:% s patronCap:% s" % (self._id, self._innKeeper, self._innName, self._level, self._gold, self._patronCap)
    def __str__(self) -> str:
        return "This inn's id is % s, owned by % s, named % s with a prestige of % s holding % s gold and servicing % s patrons." % (self._id, self._innKeeper, self._innName, self._level, self._gold, self._patronCap)
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, id) -> None:
        self._id = id
    @id.deleter
    def id(self) -> None:
        del self._id
    @property
    def innKeeper(self) -> str:
        return self._innKeeper
    @innKeeper.setter
    def innKeeper(self, innKeeper) -> None:
        self._innKeeper = innKeeper
    @innKeeper.deleter
    def innKeeper(self) -> None:
        del self._innKeeper
    @property
    def innName(self) -> str:
        return self._innName
    @innName.setter
    def innName(self, innName) -> None:
        self._innName = innName
    @innName.deleter
    def innName(self) -> None:
        del self._innName
    @property
    def level(self) -> int:
        return self._level
    @level.setter
    def level(self, level) -> None:
        self._level = level
    @level.deleter
    def level(self) -> None:
        del self._level
    @property
    def gold(self) -> int:
        return self._gold
    @gold.setter
    def gold(self, gold) -> None:
        self._gold = gold
    @gold.deleter
    def gold(self) -> None:
        del self._gold
    @property
    def patronCap(self) -> int:
        return self._patronCap
    @patronCap.setter
    def patronCap(self, patronCap) -> None:
        self._patronCap = patronCap
    @patronCap.deleter
    def patronCap(self) -> None:
        del self._patronCap

class Patron:
    def __init__(self, id = 0, name = "", xp = 0, hp = 0, gold = 0, dmg = 0, stat = 0, equip = 0) -> None:
        self._id = id
        self._name = name
        self._xp = xp
        self._hp = hp
        self._gold = gold
        self._dmg = dmg
        self._stat = stat
        self._equip = equip
    def __repr__(self) -> str:
        return "Patron id:% s name:% s xp:% s hp:% s gold:% s dmg:% s stat:% s equip:% s" % (self._id, self._name, self._xp, self._hp, self._gold, self._dmg, self._stat, self._equip)
    def __str__(self) -> str:
        return "The patron with the id of % s is named % s with an experience level of % s and % s hit points. They are carrying % s gold and can do % s damage. They are % s and using % s." % (self._id, self._name, self._xp, self._hp, self._gold, self._dmg, self._stat, self._equip)
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, id) -> None:
        self._id = id
    @id.deleter
    def id(self) -> None:
        del self._id
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name) -> None:
        self._name = name
    @name.deleter
    def name(self) -> None:
        del self._name
    @property
    def xp(self) -> int:
        return self._xp
    @xp.setter
    def xp(self, xp) -> None:
        self._xp = xp
    @xp.deleter
    def xp(self) -> None:
        del self._xp
    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self, hp) -> None:
        self._hp = hp
    @hp.deleter
    def hp(self) -> None:
        del self._hp
    @property
    def gold(self) -> int:
        return self._gold
    @gold.setter
    def gold(self, gold) -> None:
        self._gold = gold
    @gold.deleter
    def gold(self) -> None:
        del self._gold
    @property
    def dmg(self) -> int:
        return self._dmg
    @dmg.setter
    def dmg(self, dmg) -> None:
        self._dmg = dmg
    @dmg.deleter
    def dmg(self) -> None:
        del self._dmg
    @property
    def stat(self) -> int:
        return self._stat
    @stat.setter
    def stat(self, stat) -> None:
        self._stat = stat
    @stat.deleter
    def stat(self) -> None:
        del self._stat
    @property
    def equip(self) -> int:
        return self._equip
    @equip.setter
    def equip(self, equip) -> None:
        self._equip = equip
    @equip.deleter
    def equip(self) -> None:
        del self._equip

class Equipment:
    def __init__(self, id = 0, name = "", gold = 0, hpBuff = 0, dmgBuff = 0, goldBuff = 0) -> None:
        self._id = id
        self._name = name
        self._gold = gold
        self._hpBuff = hpBuff
        self._dmgBuff = dmgBuff
        self._goldBuff = goldBuff
    def __repr__(self) -> str:
        return "Equipment id:% s name:% s gold:% s hpBuff:% s dmgBuff:% s goldBuff:% s" % (self._id, self._name, self._gold, self._hpBuff, self._dmgBuff, self._goldBuff)
    def __str__(self) -> str:
        return "Equipment piece % s is a % s worth % s gold, and provides a hit point bonus of % s, a damage bonus of % s, and a % s percent increased gold bonus." % (self._id, self._name, self._gold, self._hpBuff, self._dmgBuff, self._goldBuff)
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, id) -> None:
        self._id = id
    @id.deleter
    def id(self) -> None:
        del self._id
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name) -> None:
        self._name = name
    @name.deleter
    def name(self) -> None:
        del self._name
    @property
    def gold(self) -> int:
        return self._gold
    @gold.setter
    def gold(self, gold) -> None:
        self._gold = gold
    @gold.deleter
    def gold(self) -> None:
        del self._gold
    @property
    def hpBuff(self) -> int:
        return self._hpBuff
    @hpBuff.setter
    def hpBuff(self, hpBuff) -> None:
        self._hpBuff = hpBuff
    @hpBuff.deleter
    def hpBuff(self) -> None:
        del self._hpBuff
    @property
    def dmgBuff(self) -> int:
        return self._dmgBuff
    @dmgBuff.setter
    def dmgBuff(self, dmgBuff) -> None:
        self._dmgBuff = dmgBuff
    @dmgBuff.deleter
    def dmgBuff(self) -> None:
        del self._dmgBuff
    @property
    def goldBuff(self) -> int:
        return self._goldBuff
    @goldBuff.setter
    def goldBuff(self, goldBuff) -> None:
        self._goldBuff = goldBuff
    @goldBuff.deleter
    def goldBuff(self) -> None:
        del self._goldBuff

class Monster:
    def __init__(self, id = 0, type = "", level = 0, hp = 0, gold = 0, dmg = 0) -> None:
        self._id = id
        self._type = type
        self._level = level
        self._hp = hp
        self._gold = gold
        self._dmg = dmg
    def __repr__(self) -> str:
        return "Monster id:% s type:% s level:% s hp:% s gold:% s dmg:% s" % (self._id, self._type, self._level, self._hp, self._gold, self._dmg)
    def __str__(self) -> str:
        return "Monster with id % s is a % s of level % s with % s hit points, carrying % s gold and doing % s damage." % (self._id, self._type, self._level, self._hp, self._gold, self._dmg)
    @property
    def id(self) -> int:
        return self._id
    @id.setter
    def id(self, id) -> None:
        self._id = id
    @id.deleter
    def id(self) -> None:
        del self._id
    @property
    def type(self) -> str:
        return self._type
    @type.setter
    def type(self, type) -> None:
        self._type = type
    @type.deleter
    def type(self) -> None:
        del self._type
    @property
    def level(self) -> int:
        return self._level
    @level.setter
    def level(self, level) -> None:
        self._level = level
    @level.deleter
    def level(self) -> None:
        del self._level
    @property
    def hp(self) -> int:
        return self._hp
    @hp.setter
    def hp(self, hp) -> None:
        self._hp = hp
    @hp.deleter
    def hp(self) -> None:
        del self._hp
    @property
    def gold(self) -> int:
        return self._gold
    @gold.setter
    def gold(self, gold) -> None:
        self._gold = gold
    @gold.deleter
    def gold(self) -> None:
        del self._gold
    @property
    def dmg(self) -> int:
        return self._dmg
    @dmg.setter
    def dmg(self, dmg) -> None:
        self._dmg = dmg
    @dmg.deleter
    def dmg(self) -> None:
        del self._dmg

if __name__ == "__main__":
    inn = Inn(1, "destro", "The Squeaky Wheel", 1, 500, 10)
    print(inn)
    print([inn])
    patron = Patron(1, "destro", 0, 25, 100, 5, 0, 0)
    print(patron)
    print([patron])
    equip = Equipment(1, "sword of +2 damage", 20, 0, 2, 0)
    print(equip)
    print([equip])
    enemy = Monster(1, "kobold", 1, 12, 3, 2)
    print(enemy)
    print([enemy])