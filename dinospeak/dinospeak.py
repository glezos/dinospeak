# -*- coding: utf-8 -*-

import base64, string
import smaz

 
class DinoEncoder():
    """Encode a string to dinasaur language (or try to do so).
    
    As a reference, dinosaur language sounds like this:
    "gnaaawr, hrrrraamf, gniaaaar"

    How to work with the class:
    >>> DinoEncoder.encode('hello')
    
    The current implementation works as follows:
    - input "hello world"
    - for each word with letters:
    - compress it to binary form (works well with EN)
    - convert binary to hex using standard base64.b16encode
    - convert whole word as one number to decimal (base10)
    - replace each digit to respective roarspeak letter alphabet (base10)
    
    Words are considered sequences of characters which belong in the WORD_AB
    alphabet.
    """
  
    WORD_AB = (string.letters +
               'αβγδεζηθικλμνξοπρστυφχψωάέύίήόώϋϊΰΐ' +
               'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΎΊΉΌΏ')
    ROAR_AB = 'rmwgehnauc'
    
    def compress(self, inp):
        return smaz.compress(inp)

    def decompress(self, inp):
        return smaz.decompress(inp)
        
    def encode_word(self, word):
        """Encode a single word to dinospeak."""
        compressed_word = self.compress(word)
        ids = str(int(base64.b16encode(compressed_word), 16))
        new_word = ''.join([self.ROAR_AB[int(id)] for id in ids])
        return new_word

    def encode_words(self, inp):
        """Encode a string's words to dinospeak."""
        out = ''
        cur_word = '' # Store current letter word
        for i, c in enumerate(inp):
            if c in self.WORD_AB:
                cur_word = cur_word + c
                if i == len(inp) - 1:
                    # End of string. Compress last word.
                    out = out + self.encode_word(cur_word)
                    cur_word = ''
            else:
                # Non-word char. Compress last word.
                if cur_word:
                    out = out + self.encode_word(cur_word)
                    cur_word = ''
                out = out + c
        return out

    def encode(self, inp):
        """Encode a string to dinospeak.
        
        It currently defaults in using the word-by-word encoding method.
        """
        return self.encode_words(inp)

    def decode(self, inp):
        raise NotImplementedError

