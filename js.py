class Date:
    def __init__(self, date, event):
        self._date = date
        self._events = [event]

    def get_date(self):
        return self._date

    def get_event(self):
        return self._events

    def add_event(self, event):
        self._events.append(event)
        self._events.sort()

    def __str__(self):
        returnStr = ""
        for i in self._events:
            returnStr = returnStr + self._date + ': ' + i + "\n"
        return returnStr


class DateSet:
    def __init__(self):
        self._dict = {}

    def add_date(self, date, event):
        added = False
        for key in self._dict:
            if key == date:
                self._dict[date].add_event(event)
                added = True
        if not added:
            self._dict[date] = Date(date, event)

        # function definitions


def canonicalize_date(date_str):
    y = ''
    m = ''
    d = ''
    temp = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = "0123456789"
    for item in date_str:
        if item in numbers:
            temp += item
            if len(temp) > 3:
                y = temp
        elif item.lower() in letters:
            temp += item
            if len(temp) == 3:
                if temp == "Jan":
                    m = "01"
                elif temp == "Feb":
                    m = "02"
                elif temp == "Mar":
                    m = "03"
                elif temp == "Apr":
                    m = "04"
                elif temp == "May":
                    m = "05"
                elif temp == "Jun":
                    m = "06"
                elif temp == "Jul":
                    m = "07"
                elif temp == "Avg":
                    m = "08"
                elif temp == "Sep":
                    m = "09"
                elif temp == "Oct":
                    m = "10"
                elif temp == "Nov":
                    m = "11"
                else:
                    m = "12"
        else:
            if len(temp) > 3:
                y = temp
            elif m == "":
                m = temp
            else:
                d = temp
            temp = ""
    if d == "":
        d = temp
    return "{:d}-{:d}-{:d}".format(int(y), int(m), int(d))


def putinlist(whole_line):
    line = whole_line.strip()
    l = []
    if len(line) > 20:
        i = line.index(':')
        l.append(line[0])
        l.append((str(line[2: i]).strip()))
        s = str(line[i + 1:]).strip()
        l.append(s)
    else:
        l.append(line[0])
        l.append(line[2:])
    return l


def find_indexes(string, substring):
    l = []
    for i in range(len(string)):
        if string[i] == substring:
            l.append(i)
    return l


def main():
    file_name = input()
    f = open(file_name, 'r')
    events_object = DateSet()
    for line in f:
        if line[0] == 'I':
            lineX = putinlist(line)
        elif line[0] == 'R':
            lineX = ["R", line.strip()[2:]]
        else:
            print('Error - Illegal operation.')
        lineX_date = canonicalize_date(lineX[1])
        if lineX[0] == 'I':
            events_object.add_date(lineX_date, lineX[2])
        elif lineX[0] == 'R':
            if lineX_date in events_object._dict:
                print(events_object._dict[lineX_date])


main()
