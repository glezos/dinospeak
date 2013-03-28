# -*- coding: utf-8 -*-

from __future__ import division
from dinospeak import DinoEncoder

encoder = DinoEncoder()

def test_dinospeak():
    test_data = [
        'Dinosaur-human alliance for the win.',
	'@glezos This is absurd! They will devour us right away.',
	'@glezos Devouring humanity in progress. Please rule us.'
    ]
    len_comps = []  # Store length comparisons for statistics at the end
    for d in test_data:
        assert(d == encoder.decompress(encoder.compress(d)),
               "Ensure compression works perfectly for this string")

        d_enc = encoder.encode(d)
        #FIXME: We need to test decoding as well.

        len_comp = len(d_enc)/len(d)*100
        len_comps.append(len_comp)

        print("In:  %s" % d)
        print("Out: %s" % d_enc)
        print("%s→%s chr, diff: %s%%\n" % (len(d),
                                           len(d_enc),
                                           int(len_comp),))

    print("String length comparisons: max: %s%%, min: %s%%, avg: %s%%" % (
        int(max(len_comps)),
        int(min(len_comps)),
        int(sum(len_comps, 0.0) / len(len_comps)),))

if __name__ == "__main__":
    test_dinospeak()
