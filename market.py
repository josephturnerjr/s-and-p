def stats(data, window_len):
    up = 0
    down = 0
    tie = 0
    pct = 0.0
    for ind in range(len(data) - window_len + 1):
        window = data[ind:ind + window_len + 1]
        start = window[0]
        d = window[-1]
        pct += d / start - 1.0
        if d < start:
            down += 1
        elif d > start:
            up += 1
        else:
            tie += 1
    sum = up + down + tie
    print "UP: %s (%0.2f%%)" % (up, float(up) / sum)
    print "DOWN: %s (%0.2f%%)" % (down, float(down) / sum)
    print "TIE: %s (%0.2f%%)" % (tie, float(tie) / sum)
    print "EXPECTED: %0.2f%%" % (pct / sum)

if __name__ == "__main__":
    with open('market.data') as f:
        text = map(lambda x: x.strip(), f.readlines())
    data = []
    for d in text:
        if d:
            data.append(float(d))
    print "DAYS"
    stats(data, 1)
    print "\nWEEKS"
    stats(data, 7)
    print "\nMONTHS (31 days)"
    stats(data, 31)
    print "\n6 MONTHS (180 days)"
    stats(data, 180)
    print "\nYEAR (365 days)"
    stats(data, 365)
    print "\n5 YEAR (5 * 365 days)"
    stats(data, 5 * 365)
    print "\n10 YEAR (10 * 365 days)"
    stats(data, 10 * 365)
    print "\n20 YEAR (20 * 365 days)"
    stats(data, 6933)
