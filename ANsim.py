import random;
import numpy as np;
import pylab as pl;
import matplotlib.patches as mpatches
from scipy import stats

def input_num2(prompt="Number of cards with CMC 0: "):
    while True:
        num_str = input(prompt).strip()
        if all(c in '+-.0123456789' for c in num_str):
            break
    if '.' in num_str:
        return float(num_str)
    else:
        return int(num_str)

def makedeck(manacurve):
    deck = []
    current = 0;
    for i in manacurve:
        for cmc in range(i):
            deck.append(current)
        current += 1;
    return deck

def adnauseam(deckstats, life, turn, draw):
    cards = 0;
    deck = makedeck(deckstats);
    random.shuffle(deck)
    for i in range(6 + turn + draw):
        deck.pop();
    while life >= max(deck):
        life -= deck.pop();
        cards += 1;
    return [life, cards]

big5 = [];

def repeatsimulations(n, deckstats, life, turn, draw):
    results = {};
    for base in range(50):
        results[base] = 0;
    resultslist = [];
    for a in range(n):
        resultslist.append(adnauseam(deckstats, life, turn, draw)[1]);
    for b in resultslist:
        results[b] += 1;
    big5.append(resultslist);
    return results

def confint(arr):
    mean, sigma, perc = np.mean(arr), np.std(arr), np.percentile(arr, 5)
    conf_int = stats.norm.interval(0.95, loc=mean, scale=sigma)
    print(mean)
    print(sigma)
    print(perc)
    return conf_int


def adnauseamwithmana(deckstats, life, turn, draw):
    cards = 0;
    mana = 0;
    deck = makedeck(deckstats) + list(ramps.keys());
    random.shuffle(deck)
    for i in range(6 + turn + draw):
        deck.pop();
    while life >= max([i for i in deck if isinstance(i, int)]):
        card = deck.pop();
        if card in ramps.keys():
            life -= ramps[card][0];
            mana += ramps[card][1];
            cards += 1;
        else:
            life -= card;
            cards += 1;
    return [cards, mana]

def repeatsimulationswithmana(n, deckstats, life, turn, draw):
    results = {};
    for base in range(50):
        results[base] = 0;
    resultslist = [];
    for a in range(n):
        resultslist.append(adnauseamwithmana(deckstats, life, turn, draw));
    big5.append(resultslist);
    return

def confint2(arr):
    mean, sigma, perc = np.mean([i[0] for i in arr]), np.std([i[0] for i in arr]), np.percentile([i[0] for i in arr], 5)
    meanm, sigmam, percm = np.mean([i[1] for i in arr]), np.std([i[1] for i in arr]), np.percentile([i[1] for i in arr], 5)
    print(mean, sigma, perc)
    print(meanm, sigmam, percm)
    return

ramps = {'CM':[0,1], 'GM':[2,1], 'LP':[0,1], 'MC':[0,2], 'MV':[1,2], 'MD':[0,1], 'SR':[1,2], 'MO':[0,1], 'DR':[1,2], 'CR':[2,3]}

shimmerzur = [35, 26, 25, 9, 2, 1, 0]
gitrog = [42, 26, 17, 10, 0, 2, 0, 0, 0, 0, 1]
thrasiostymna = [33, 26, 17, 13, 3, 4, 1]
jeleva = [34, 25, 21, 12, 2, 3, 1]
tazri = [34, 37, 14, 10, 1, 2]
paradoxt = [36, 30, 29, 9, 1, 2]
reanimator = [35, 27, 19, 10, 2, 0, 3, 0, 0, 0, 1] # Sphinx > AN
sbt = [35, 23, 19, 14, 4, 0, 1, 1, 1] # DTT > AN
newzur = [35, 25, 25, 9, 2, 1, 0, 0, 1] #Retract > DTT
newthrasios = [33, 26, 17, 12, 3, 4, 1, 0, 1] #Leovold > DTT
newjeleva = [34, 25, 21, 11, 2, 3, 1, 0, 1] #Dack > DTT
newtazri = [34, 37, 14, 9, 1, 2, 0, 0, 1] #Grasp > DTT
newgitrog = [42, 26, 18, 10, 0, 2] #Kozi > GB

zurm = [31, 23, 23, 9, 2, 1, 0]
paradoxm = [32, 27, 27, 9, 1, 2]
jelevam = [30, 22, 19, 12, 2, 3, 1]

zurms = repeatsimulationswithmana(100000, zurm, 30, 5, 5)
paradoxms = repeatsimulationswithmana(100000, paradoxm, 30, 5, 5)
jelevams = repeatsimulationswithmana(100000, jelevam, 30, 5, 5)



#shimmerzurs = repeatsimulations(100000, shimmerzur, 30, 5, 5)
#gitrogs = repeatsimulations(100000, gitrog, 30, 5, 5)
#thrasiostymnas = repeatsimulations(100000, thrasiostymna, 30, 5, 5)
#jelevas = repeatsimulations(100000, jeleva, 30, 5, 5)
#tazris = repeatsimulations(100000, tazri, 30, 5, 5)
#paradoxts = repeatsimulations(100000, paradoxt, 30, 5, 5)
#reanimators = repeatsimulations(100000, reanimator, 25, 5, 5)
#sbts = repeatsimulations(100000, sbt, 30, 5, 5)
#newzurs = repeatsimulations(100000, newzur, 30, 5, 5)
#newgitrogs = repeatsimulations(100000, newgitrog, 30, 5, 5)
#newthrasioss = repeatsimulations(100000, newthrasios, 30, 5, 5)
#newjelevas = repeatsimulations(100000, newjeleva, 30, 5, 5)
#newtazris = repeatsimulations(100000, newtazri, 30, 5, 5)



#shimmerzurp = pl.plot(list(shimmerzurs.keys()), list(shimmerzurs.values()), 'r')
#gitrogp = pl.plot(list(gitrogs.keys()), list(gitrogs.values()), 'g')
#thrasiostymnap = pl.plot(list(thrasiostymnas.keys()), list(thrasiostymnas.values()), 'b')
#jelevap = pl.plot(list(jelevas.keys()), list(jelevas.values()), 'y')
#tazrip = pl.plot(list(tazris.keys()), list(tazris.values()), 'k')
#paradoxtp = pl.plot(list(paradoxts.keys()), list(paradoxts.values()), 'm')
#newzurp = pl.plot(list(newzurs.keys()), list(newzurs.values()), 'g')
#newgitrogp = pl.plot(list(newgitrogs.keys()), list(newgitrogs.values()), 'b')
#newthrasiosp = pl.plot(list(newthrasioss.keys()), list(newthrasioss.values()), 'y')
#newjelevap = pl.plot(list(newjelevas.keys()), list(newjelevas.values()), 'k')
#newtazrip = pl.plot(list(newtazris.keys()), list(newtazris.values()), 'r')

pl.xlabel('Number of cards drawn')
pl.ylabel('Number of instances')

#red = mpatches.Patch(color='red', label='Shimmer Zur')
#green = mpatches.Patch(color='green', label='Gitrog')
#blue = mpatches.Patch(color='blue', label='Thrasios Tymna Telepathy')
#yellow = mpatches.Patch(color='yellow', label='Jeleva')
#black = mpatches.Patch(color='black', label='FC Tazri')
#magenta = mpatches.Patch(color='magenta', label='Paradox Thrasios')
#green1 = mpatches.Patch(color='green', label='New Zur')
#blue1 = mpatches.Patch(color='blue', label='New Gitrog')
#yellow1 = mpatches.Patch(color='yellow', label='New Thrasios Tymna Telepathy')
#black1 = mpatches.Patch(color='black', label='New Jeleva')
#red1 = mpatches.Patch(color='red', label='New FC Tazri')
#pl.legend(handles=[red, green, blue, yellow, black, magenta])
#pl.legend(handles=[green, blue1])

for i in big5:
    print(confint2(i))





#life = input_num2(prompt="Life total: ")
#turn = input_num2(prompt="Turn number: ")
#draw = input_num2(prompt="Number of extra cards drawn: ")
#repeat = input_num2("Number of simulations: ")
#choice = input_num2("4 for input, 0 to 3 for preselected, 5 for others ")
#if choice == 4:
#    cmc0 = input_num2(prompt="Number of cards with CMC 0 (including lands): ")
#    cmc1 = input_num2(prompt="Number of cards with CMC 1: ")
#    cmc2 = input_num2(prompt="Number of cards with CMC 2: ")
#    cmc3 = input_num2(prompt="Number of cards with CMC 3: ")
#    cmc4 = input_num2(prompt="Number of cards with CMC 4: ")
#    cmc5 = input_num2(prompt="Number of cards with CMC 5: ")
#    cmc6 = input_num2(prompt="Number of cards with CMC 6: ")
#    deckstats = [cmc0, cmc1, cmc2, cmc3, cmc4, cmc5, cmc6]
#elif choice != 5:
#    deckstats = [shimmerzur, gitrog, thrasiostymna, jeleva][choice]
#    repeatsimulations(repeat, deckstats, life, turn, draw)
#else:
#    repeatsimulations(repeat, shimmerzur, life, turn, draw)
#    repeatsimulations(repeat, gitrog, life, turn, draw)
#    repeatsimulations(repeat, thrasiostymna, life, turn, draw)
#    repeatsimulations(repeat, jeleva, life, turn, draw)






