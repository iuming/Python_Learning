#CalThreeKingdomsV1.py
import jieba
def getText():
    txt = open("ThreeKingdoms.txt", "r", encoding="utf-8").read()
    return txt

def main():
    ThreeKingdomsTxt = getText()
    words = jieba.lcut(ThreeKingdomsTxt)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(15):
        word, count =items[i]
        print("{0:<10}{1:>5}".format(word, count))

if __name__ == '__main__':
    main()