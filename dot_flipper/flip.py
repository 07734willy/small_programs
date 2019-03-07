import re

def count3S(substrings):
    total = 0
    for substring in substrings:
        total += sum(len(s) // 3 for s in substring.split('.'))
    return total

def sub3S(substrings, flips, count):
    for i in range(len(substrings)):
        while flips and substrings[i][:3] == "SSS":
            substrings[i] = substrings[i][3:]
            count += 3
            flips -= 1
        while flips and substrings[i][-3:] == "SSS":
            substrings[i] = substrings[i][:-3]
            count += 3
            flips -= 1
        substrings[i] = substrings[i].strip('.')
    substrings = [substring for substring in substrings if substring]
    return substrings, flips, count

def flip(string, flips):
    count = string.count('.')
    string = string.strip('.')
    print(string)
    substrings = re.split("\.\.+", string)
    substrings, flips, count = sub3S(substrings, flips, count)


    if all(len(substring) == 1 for substring in substrings):
        return count + min(flips, len(substrings))
    print(substrings)

class flipper:
    def __init__(self, string, flips):
        self.string = string
        self.flips = flips
        self.dots = self.flip()
        
    def strsub(self, pattern, repl, string):
        last = None
        while self.flips and last != string:
            last, string = string, \
                    re.sub(pattern, repl, string, count=1)
            self.flips -= 1
        if last == string: self.flips += 1
        return string

    def flip(self):
        self.string = ".." + self.string + ".."
        self.string = self.strsub("\.\.SSS", "."*5, self.string)
        self.string = self.strsub("SSS\.\.", "."*5, self.string)

        print(self.flips)
        repl = lambda x: re.sub("SSS", "...", x.group(0), count=1)
        self.string = self.strsub("\.(SSS)+\.", repl, self.string)

        flip3 = sum(len(s)//3 for s in re.split("\.+", self.string))

        
        self.string = self.string[2:-2]
        print(self.string)

def main():
    string = "SSS..S.SSSSSS.SS...SSSS."

    flip(string, 3)
    flipper(string, 4)

if __name__ == "__main__":
    main()
