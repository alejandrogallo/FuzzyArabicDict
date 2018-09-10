# -*- coding: utf-8 -*-
from aramorph.transliterate import *


def test_b2u():
    assert(b2u('salAm') == unicode('سَلام'))
    assert(b2u('ElY') == unicode('على'))


def test_u2b():
    artxt = (
        "يُولَدُ جَمِيعُ ٱلنَّاسِ أَحْرَارًا مُتَسَاوِينَ فِي ٱلْكَرَامَةِ وَٱلْحُقُوقِ. وَقَدْ وُهِبُوا"
        " عَقْلًا وَضَمِيرًا وَعَلَيْهِمْ أَنْ يُعَامِلَ بَعْضُهُمْ بَعْضًا بِرُوحِ ٱلْإِخَاءِ"
    )
    butxt = (
        "yuwladu jamiyEu {lna~Asi >aHoraArFA mutasaAwiyna fiy"
        " {lokaraAmapi wa{loHuquwqi. waqado wuhibuwA EaqolFA "
        "waDamiyrFA waEalayohimo >ano yuEaAmila baEoDuhumo baEoDFA "
        "biruwHi {lo<ixaA'i"
    )
    assert(u2b(artxt) == butxt)
