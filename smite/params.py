__author__ = 'way2muchnoise'


queue = {
    'Conquest5v5': '423',
    'NoviceQueue': '424',
    'Conquest': '426',
    'Practice': '427',
    'ConquestChallenge': '429',
    'ConquestRanked': '430',
    'Domination': '433',
    'MOTD': '434',
    'Arena': '435',
    'ArenaChallenge': '438',
    'DominationChallenge': '439',
    'JoustLeague': '440',
    'JoustChallenge': '441',
    'Assault': '445',
    'AssaultChallenge': '446',
    'Joust3v3': '448',
    'ConquestLeague': '451',
    'ArenaLeague': '452'
}

langCode = {
    'English': 1,
    'German': 2,
    'French': 3,
    'Spanish': 7,
    'Spanish (Latin America)': 9,
    'Portuguese': 10,
    'Russian': 11,
    'Polish': 12,
    'Turkish': 13
}

leagues = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Masters']
tiers = ['V', 'IV', 'III', 'II', 'I']


def get_league_tier(number):
    if number > 0:
        number -= 1
    league = number / 5
    tier = number % 5
    if league == 5:
        tier = 4
    return leagues[league] + " " + tiers[tier]


def get_game_mode(number):
    for k, v in queue.iteritems():
        if number == v:
            return k