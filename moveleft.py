seq=[-1,9,-8,20,-7,6, 2 ,-5, -90, 7]
seq.shift()


def shift(seq, n=0):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]