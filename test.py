# -*- coding: utf-8 -*-

from __future__ import division
from dinospeak import DinoEncoder

encoder = DinoEncoder()

def test_dinospeak():
    test_data = [
        'Σκέφτομαι να πάω ανάσταση με τη φόρμα... Αν με κοιτανε περίεργα, θα κάνω ότι είμαι παιδι ειδικών αναγκών...',
        '@kalavros lol! thanks, επίσης! :)',
        '@apas Σε σκέφτηκα γιατί εσύ τα κάνεις κάτι τέτοια! Καλή Ανάσταση man :)',
        'Σε εστιατόριο. -μπορείτε να πάρετε το κοτόπουλο να μου το ψήσετε λίγο ακόμα; -Γιατί τι έχει; -Μου τρώει τις πατάτες',
        '@kalavros no, δεν είμαι. πρώτη φορά το βλέπω!',
        'Slides from Releasing Extension on PGXN presented at PDXPUG slidesharenetjustatheory',
        '@aethaeth blah.',
    ]
    len_comps = []  # Store length comparisons for statistics at the end
    for d in test_data:
        assert(d == encoder.decompress(encoder.compress(d)),
               "Ensure compression works perfectly for this string")

        d_enc = encoder.encode(d)
        #FIXME: We need to test decoding as well.

        len_comp = len(d_enc)/len(d)*100
        len_comps.append(len_comp)

        print("In:%s" % d)
        print("Out: %s" % d_enc)
        print("Stats: %s→%s chr, diff: %s%%\n" % (len(d),
                                                  len(d_enc),
                                                  int(len_comp),))

    print("String length comparisons: max: %s%%, min: %s%%, avg: %s%%" % (
        int(max(len_comps)),
        int(min(len_comps)),
        int(sum(len_comps, 0.0) / len(len_comps)),))

if __name__ == "__main__":
    test_dinospeak()
