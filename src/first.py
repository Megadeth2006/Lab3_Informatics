import re

test = "Кривошеее существо гуляет по парку"
test1 = "На берегу реки стояла старая мельница, где каждое утро собирались местные жители, чтобы обсудить новости и поделиться историями."
test2 = "На вершине холма раскинулся старинный замок, окружённый густым лесом, где каждую ночь звёзды светили ярче, чем где-либо ещё, создавая волшебную атмосферу для всех, кто осмеливался подняться туда."
test3 = "На берегу тихого озера, утопающего в зелени, стояла старая деревянная лодка, покрытая слоем пыли и воспоминаний. Каждый вечер, когда солнце медленно опускалось за горизонт, её тень растягивалась по воде, словно приглашая путешественников в мир забытой сказки, где ветер шептал истории о любви, потерях и надежде, оставляя за собой лишь лёгкий след на поверхности."
test4 = "Там, где было особенно трудно лошадям, мы слезали с брички, шли пешком. Под сапогами хлюпал размокший снег, идти было тяжело, но по обочинам дороги все еще держался хрустально поблескивавший на солнце ледок, и там пробираться было еще труднее. Только часов через шесть покрыли расстояние в тридцать километров, подъехали к переправе через речку Еланку."
test5 = "Был полдень. Солнце светило горячо, как в мае. Я надеялся, что папиросы скоро высохнут. Солнце светило так горячо, что я уже пожалел о том, что надел в дорогу солдатские ватные штаны и стеганку. Это был первый после зимы по-настоящему теплый день. Хорошо было сидеть на плетне вот так, одному, целиком покорясь тишине и одиночеству, и, сняв с головы старую солдатскую ушанку, сушить на ветерке мокрые после тяжелой гребли волосы, бездумно следить за проплывающими в блеклой синеве белыми грудастыми облаками."

def check(main_test, c):
    
    string1 = re.findall(r"\b\w+\b", main_test)
    answer = []
    count_glasn = []
    count_sogl = []

    for i in string1:
    
        if (len(re.findall(r"\b\w+[уеёыаоэяию]{2}\w+\b", i, re.IGNORECASE))) == 1:
            count_glasn.append(1)
        else:
            count_glasn.append(0)
        
    for i in string1:
    
        if (len(re.findall(r"[йцкнгшщзхфвпрлджчсмтб]", i, re.IGNORECASE))) <= 3:
            count_sogl.append(1)
        else:
            count_sogl.append(0)
        
    for i in range(len(string1)-1):
        if count_glasn[i] == 1 and count_sogl[i+1] == 1:
            answer.append(string1[i])
    print("Номер теста " + str(c) + ":", end=" ")
    
    for i in answer:
        print(i, end=" ")
    print()

def main():
    c = 0
    tests = [test, test1, test2, test3, test4, test5]
    for current_test in tests:
        check(current_test, c)
        c += 1

if __name__ == "__main__":
    main()