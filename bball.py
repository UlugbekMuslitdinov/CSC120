class Team:

    def __init__(self, line):
        self.name = line[0]
        self.conference = line[1]
        self.wins = line[2]
        self.losses = line[3]

    def name(self):
        return self.name

    def conf(self):
        return self.conference

    def win_ratio(self):
        return int(self.wins)/(int(self.wins)+int(self.losses))

    def __str__(self):
        "{} : {}".format(self.name, str(self.win_ratio))


class Conference:

    def __init__(self, conf):
        self.name = conf
        self.teams = []

    def __contains__(self, team):
        if team in self.teams:
            return True
        return False

    def name(self):
        return self.name

    def add(self, team):
        self.teams.append(team)

    def win_ratio_avg(self):
        sum_points = 0
        for team in self.teams:
            sum_points += team.win_ratio()
        return sum_points/len(self.teams)

    def __str__(self):
        return "{} : {}".format(self.name, str(self.win_ratio_avg()))


class ConferenceSet:

    def __init__(self):
        self.conferences = []

    def add(self, team):
        found = 0
        for conference in self.conferences:
            if conference.name == team.conference:
                conference.add(team)
                found = 1
        if found == 0:
            conf = Conference(team.conf())
            self.conferences.append(conf)
            conf.add(team)

    def best(self):
        winners = [self.conferences[0].name]
        max_score = self.conferences[0].win_ratio_avg()
        for conf in self.conferences:
            if conf.win_ratio_avg() > max_score:
                winners = [conf.name]
                max_score = conf.win_ratio_avg()
            elif conf.win_ratio_avg() == max_score:
                if conf.name not in winners:
                    winners.append(conf.name)
        return winners, max_score


def main():
    confs = ConferenceSet()
    f_name = input()
    file = open(f_name, 'r')
    lines = file.read().splitlines()
    for line in lines:
        if line[0] != "#":
            contents = line.split()
            pass_list = [contents.pop(len(contents) - 2), contents.pop(len(contents) - 1)]
            conf = ""
            if ")" in contents[-1] and "(" in contents[-1]:
                conf = contents[-1].strip("()")
            elif ")" in contents[-1]:
                while "(" not in contents[-1]:
                    conf += contents.pop(len(contents)-1)
                conf = contents.pop(len(contents)-1) + " " + conf
                conf = conf.strip("()")
            name = " ".join(contents)
            pass_list = [name, conf] + pass_list
            confs.add(Team(pass_list))
    best_confs, score = confs.best()
    for conf in sorted(best_confs):
        print("{} : {}".format(conf, score))


main()
