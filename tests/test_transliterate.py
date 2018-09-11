# -*- coding: utf-8 -*-
from aramorph.transliterate import *


def test_unicode():
    assert('على')
    assert(u'على')
    assert(b2u('slAm'))


def test_b2u():
    assert(b2u('salAm') == u'سَلام')
    assert(b2u('ElY') == u'على')


def test_u2b():
    artxt = (
        u"يُولَدُ جَمِيعُ ٱلنَّاسِ أَحْرَارًا مُتَسَاوِينَ فِي ٱلْكَرَامَةِ وَٱلْحُقُوقِ. وَقَدْ وُهِبُوا"
        u" عَقْلًا وَضَمِيرًا وَعَلَيْهِمْ أَنْ يُعَامِلَ بَعْضُهُمْ بَعْضًا بِرُوحِ ٱلْإِخَاءِ"
    )
    butxt = (
        "yuwladu jamiyEu {lna~Asi >aHoraArFA mutasaAwiyna fiy"
        " {lokaraAmapi wa{loHuquwqi. waqado wuhibuwA EaqolFA "
        "waDamiyrFA waEalayohimo >ano yuEaAmila baEoDuhumo baEoDFA "
        "biruwHi {lo<ixaA'i"
    )
    assert(u2b(artxt) == butxt)

def test_b2ala_wehr_letter():
    assert(b2ala_wehr_letter('l') == 'l')
    assert(b2ala_wehr_letter('l~') == 'l~')
    assert(b2ala_wehr_letter('k') == 'k')
    assert(b2ala_wehr_letter('q') == 'q')
    assert(b2ala_wehr_letter('$') == u"š")

def test_b2ala_wehr():
    assert(b2ala_wehr('HAr}b') == u'ḥārʾb')
