import Levenshtein as Lev

def cer(ref, hyp):
    return Lev.distance(ref, hyp) / max(1, len(ref))
