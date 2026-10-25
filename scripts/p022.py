# Using p022.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
# What is the total of all the name scores in the file?

from euler import solution

@solution
def solve():
    f = open(r"scripts\p022.txt")
    names = f.read().replace('"','').replace('\n', '').split(',')
    names.sort()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    total_name_score = 0
    for name in names:
        name_worth = 0
        for letter in name:
            name_worth += (alphabet.index(letter.lower()) + 1)
        
        total_name_score += name_worth * (names.index(name) + 1)
    
    return total_name_score
        

if __name__ == "__main__":
    solve()