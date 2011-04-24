from __future__ import division
from smaz import compress, decompress


class Encoder():
    """Encode a string to a new alphabet.
    
    Steps: prepare -> steps[1,..] -> convert -> unsteps
    Example run:
    
    >>> coder = Coder()
    >>> coder.string = "foobar"
    >>> 
    """

    OLD_ALPHABET = ['abcdefghijklmnopqrstuvwxyz']
    ALPHABET = ['raceghnmuw']

    def encode(self, input):
        #inp = self.prepare(inp)
        enc = ''
        for letter in inp:
            if letter in OLD_ALPHABET:

    def test():
        strs = ['Σκέφτομαι να πάω ανάσταση με τη φόρμα... Αν με κοιτανε περίεργα, θα κάνω ότι είμαι παιδι ειδικών αναγκών...',
            '@kalavros lol! thanks, επίσης! :)',
            '@apas Σε σκέφτηκα γιατί εσύ τα κάνεις κάτι τέτοια! Καλή Ανάσταση man :)',
            'Σε εστιατόριο. -μπορείτε να πάρετε το κοτόπουλο να μου το ψήσετε λίγο ακόμα; -Γιατί τι έχει; -Μου τρώει τις πατάτες',
            '@kalavros no, δεν είμαι. πρώτη φορά το βλέπω!',
            'Slides from Releasing Extension on PGXN presented at PDXPUG slidesharenetjustatheory',
            '@aethaeth blah.',
        ]

        for s in strs:
            enc = 
            dec = decompress(enc.decode('hex'))
            print s, dec


