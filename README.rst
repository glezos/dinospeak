
=========
Dinospeak
=========

Dinospeak is a library to encode human language to dinosaur language.
You know, in case they come back to life or invade us using dino spaceships.

Dinospeak is optimized for small strings (eg. micro-blogging) and aims in
preserving punctuation. The implementation is very simple and naive. We
plan to improve it after the first encounter with the species and further
testing.

Source code repo: https://github.com/glezos/dinospeak


Examples
========

Here are the output of the sample tests::

    In:  Dinosaur-human alliance for the win.
    Out: amhnceahermrwennw-grehwehhg muachacwaw nu m mnnhh.
    36→50 chr, diff: 138%

    In:  @glezos This is absurd! They will devour us right away.
    Out: @wheuaarewmun mnnnaawe ga muncrhmweru! muhmh egwmgrw ncaecgn mne
    mcmneaguhc gmarmm.
    55→83 chr, diff: 150%

    In:  @glezos Devouring humanity in progress. Please rule us.
    Out: @wheuaarewmun wachnurhmcueehe mcchagwmmmahwg mh whcngmwcwugu.
    mrcwwnchuguae acnwea mne.
    55→87 chr, diff: 158%

    String length comparisons: max: 158%, min: 138%, avg: 149%


Installing
==========

You can install using the standard ``setuptools``::

  (sudo) easy_install dinospeak

With sudo, dinospeak will be installed eg. in
``/usr/lib/python2.6/site-packages/dinospeak-0.x-py2.6.egg/``.

The current implementation depends on smaz_. The above command should
install it automatically for you.

.. _smaz: http://github.com/antirez/smaz

Alternatively, grab the source code itself::

  git clone git://github.com/glezos/dinospeak.git

To run the tests::

    $ python <path-to-dinospeak>/test.py


Authors & Credits
=================

Original author: Dimitris Glezos

Thanks to Ios Kaye and Vasilis Georgitzikis for some cool implementation ideas.
Thanks to #ceidtrip for embracing a plastic dino like their own child.

