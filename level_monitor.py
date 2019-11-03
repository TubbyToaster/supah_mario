from level_gen import Chunk


class Monitor:
    def __init__(self, ai_settings, screen, g_blocks, bg_blocks, chunks, enemies, items):
        self.ai_settings = ai_settings
        self.screen = screen
        self.g_blocks = g_blocks
        self.bg_blocks = bg_blocks
        self.x = 0
        self.items = items
        self.screen_rect = screen.get_rect()
        self.pos = 0
        self.cur = 1
        self.level_list = []
        self.level_listbg = []
        self.level_list2 = []
        self.level_listbg2 = []
        self.init_level()
        self.mario_pos = 0
        self.chunks = chunks
        self.enemies = enemies

    def init_level(self):
        a1 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "111111111111111",
            "111111111111111"
        ]

        a2 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0000000u0000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0u000tytut00000",
            "000000000000000",
            "000000000000023",
            "0000000@0000054",
            "111111111111111",
            "111111111111111"
        ]

        a3 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000002300000",
            "000000005400000",
            "0000@0005400000",
            "111111111111111",
            "111111111111111"
        ]

        a4 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "023000000000230",
            "054000000000540",
            "054000000000540",
            "0540000@0@00540",
            "111111111111111",
            "111111111111111"
        ]

        a5 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0000?0000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "111111111001111",
            "111111111001111"
        ]

        a6 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000@0@000000",
            "00000tttttttt00",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "00tyt0000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "111111111110001",
            "111111111110001"
        ]

        a7 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0tttu0000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0000z00000t.000",
            "000000000000000",
            "000000000000000",
            "0000000@0@00000",
            "111111111111111",
            "111111111111111"
        ]

        a8 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0000y0000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0u00u00u00000t0",
            "000000000000000",
            "000000000000000",
            "00#000000@0@000",
            "111111111111111",
            "111111111111111"
        ]

        a9 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "0ttt0000tuut000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000tt0000",
            "000000000000000",
            "000000000000000",
            "00000@@00@@0006",
            "111111111111111",
            "111111111111111"
        ]

        a10 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "006006000000000",
            "066006600000000",
            "666006660000006",
            "666006666000066",
            "111111111111111",
            "111111111111111"
        ]

        a11 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "066006000000000",
            "666006600000000",
            "666006660000023",
            "666006666000054",
            "111001111111111",
            "111001111111111"
        ]

        a12 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000ttut00000000",
            "000000000000000",
            "000000000000002",
            "00000000@@00005",
            "111111111111111",
            "111111111111111"
        ]

        a13 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000006600000",
            "000000066600000",
            "000000666600000",
            "000006666600000",
            "000066666600000",
            "000666666600000",
            "306666666600000",
            "466666666600000",
            "111111111111111",
            "111111111111111"
        ]

        a14 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000|00000000000",
            "000|00000000000",
            "000|00000000000",
            "000|00000000000",
            "000|00000000000",
            "000|00000000000",
            "000|00000000000",
            "000|00000000000",
            "000|000000=====",
            "0006000000=====",
            "111111111111111",
            "111111111111111"
        ]

        a15 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "111111111111111",
            "111111111111111"
        ]

        a16 = [
            "000000000000000",
            "000000000000000",
            "800088888880000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800088888880000",
            "8000888888800ab",
            "80008888888009c",
            "777777777777777",
            "777777777777777"
        ]

        a17 = [
            "000000000000000",
            "000000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "gf0000000000000",
            "df0000000000000",
            "ef0000000000000",
            "770000000000000",
            "770000000000000"
        ]
        a2_1 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000230",
            "000000000000540",
            "0000000000ijm40",
            "0000000000hkl40",
            "111111111111111",
            "111111111111111"
        ]
        a2_2 = [
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "111111111100000",
            "111111111100000"
        ]
        a2_3 = [
            "000000000000000",
            "000000000000000",
            "800000888888888",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "800000000000000",
            "000000000000000",
            "0000000000`~~~~",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "777777777777777",
            "777777777777777"
        ]
        a2_4 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "00000000000000+",
            "00000000n0n0000",
            "000000n0n0n0n00",
            "00]0n0n0n0n0n00",
            "0]n0n0n0n0n0n0]",
            "777777777777777",
            "777777777777777"
        ]
        a2_5 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000808888",
            "000000000808008",
            "000000000888008",
            "0n0000000000000",
            "0n0n00000000000",
            "0n0n0000000000{",
            "777777777777777",
            "777777777777777"
        ]
        a2_6 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000880088",
            "000000000880088",
            "000000088000000",
            "000000088000000",
            "0-0000088000000",
            "08000008800000",
            "880000088880088",
            "000000000880000",
            "000000000880000",
            "{00000000000000",
            "777777777777777",
            "777777777777777"
        ]
        a2_7 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "888800888800000",
            "8888008888000]0",
            "008800080000880",
            "008800080000880",
            "008800080000880",
            "008800080)008-0",
            "888800088800880",
            "000000000000000",
            "000000000000000",
            "{00]0]000000000",
            "777777777777777",
            "777777777777777"
        ]
        a2_8 = [
            "000000000000000",
            "000000000000000",
            "8888888888888(8",
            "088880000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000008888880",
            "0]0]00008888880",
            "088880000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "777770007777777",
            "777770007777777"
        ]
        a2_9 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "00000000000000[",
            "0000000000000op",
            "0000000000000gf",
            "0000000000]]]gf",
            "777777777777777",
            "777777777777777"
        ]
        a2_10 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "00000[000000000",
            "0000op000000000",
            "0000gf00000[000",
            "0000gf0000op000",
            "0000gf00]0gf000",
            "777777777777777",
            "777777777777777"
        ]
        a2_11 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "008800000000000",
            "00880000000000n",
            "0088000000000nn",
            "007700777777777",
            "007700777777777"
        ]
        a2_12 = [
            "000000000000000",
            "000000000000000",
            "888888888888888",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "000000000000000",
            "00000___0000000",
            "00]000000088888",
            "]nn000000000000",
            "nnn000000000000",
            "nnn000000000000",
            "nnn000000000{00",
            "77700___0077777",
            "777000000077777"
        ]
        a2_13 = [
            "000000000000000",
            "000000000000000",
            "888000000000888",
            "000000000000000",
            "000000000000000",
            "00000___0000000",
            "000000000000000",
            "000000000000000",
            ")00000000000000",
            "000000000000000",
            "000000000088888",
            "000000000088888",
            "00000___0088888",
            "777000000077777",
            "777000000077777"
        ]
        a2_14 = [
            "000gf8888888888",
            "000gf8888888888",
            "888gf8888888888",
            "000gf8888888888",
            "000gf8888888888",
            "000gf8888888888",
            "000gf8888888888",
            "000gf8888888888",
            "0abdf8888888888",
            "09cef8888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "777777777777777",
            "777777777777777"
        ]
        a2_15 = [
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "888888888888888",
            "777777777777777",
            "777777777777777"
        ]
        b2_1 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbpqqrbbbbbbbb",
            "bbbsttubbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbpqrbbb",
            "bvvvbbbbbstubbb",
            "byx1bbbbbbbbbbb",
            "vwwwvbbbbbbbbbb",
            "xxzxxbbbbbbbbbb",
            "xxaxxbbbbbbbbbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]
        b2_2 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbpqqrbbbbbbb",
            "bbbbsttubbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "aaaaaaaaaabbbbb",
            "aaaaaaaaaabbbbb"
        ]
        b2_3 = [
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]
        b1 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbpqrbbbb",
            "bbbbbbbbstubbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbhbbbbbbbbbbbb",
            "bgkibbbbbbbbbbb",
            "gkjlibbbbbbmnnn",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b2 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbpqrbbbbbbbb",
            "bbbbstubbbbbpqq",
            "bbbbbbbbbbbbstt",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbhbbbbbbbbbbbb",
            "ogkibbbbmnobbbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b3 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbpqqrbbbbb",
            "qrbbbbsttubbbbb",
            "tubbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbmnno",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b4 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbpqrb",
            "bbbbbbbbbbbstub",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbhbbbbbbbbb",
            "bbbbgkibbbbbbbb",
            "bbbgkjlibbbbbbm",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b5 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbpqrbbbbb",
            "bbbbbbbstubbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbhbbbbbbbbb",
            "nnnogkibbbbmnob",
            "aaaaaaaaabbaaaa",
            "aaaaaaaaabbaaaa"
        ]

        b6 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbpqqrbb",
            "pqqqrbbbbsttubb",
            "stttubbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbm",
            "aaaaaaaaaaabbba",
            "aaaaaaaaaaabbba"
        ]

        b7 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbp",
            "bbbbbbbbbbbbbbs",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbhbbbbbb",
            "bbbbbbbgkibbbbb",
            "nnobbbgkjlibbbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b8 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbpqrbb",
            "qrbbbbbbbbstubb",
            "tubbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbhbbbbbb",
            "bbmnnnogkibbbbm",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b9 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbpqq",
            "bbbpqqqrbbbbstt",
            "bbbstttubbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "nobbbbbbbbbbbbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b10 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "rbbbbbbbbbbbbbb",
            "ubbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbhbbb",
            "bbbbbbbbbbgkibb",
            "bbbnnbbbbgkjlbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b11 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbpq",
            "bbpqrbbbbbbbbst",
            "bbstubbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbhbbb",
            "bbbbbbbbbogkibb",
            "aaabbaaaaaaaaaa",
            "aaabbaaaaaaaaaa"
        ]

        b12 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "rbbbbbbbbbbbbbb",
            "ubbbbbpqqqrbbbb",
            "bbbbbbstttubbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbmnobbbbbbbbbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b13 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "pqqrbbbbbbbbbbb",
            "sttubbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbh",
            "bbbbbbbbbbbbbgk",
            "bbbbbbbbbbbbgkj",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b14 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbb3bbbbbbbbbbb",
            "bb56bpqrbbbbbbb",
            "bbb2bstubbbbbbb",
            "bbb2bbbbbbbbbbb",
            "bbb2bbbbbbbbbbb",
            "bbb2bbbbbbbbbbb",
            "bbb2bbbbvvvbbbb",
            "bbb2bbbbyx1bbbb",
            "bbb2bbbvwwwvbbb",
            "ibb2bbbxxzxxbbh",
            "libbbbbxxaxxogk",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]

        b15 = [
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bpqrbbbbbpqqqrb",
            "bstubbbbbstttub",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "bbbbbbbbbbbbbbb",
            "ibbbbmnobbbbbbb",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]
        b16 = [
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]
        b17 = [
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaa"
        ]
        self.level_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17]
        self.level_listbg = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]
        self.level_list2 = [a2_1, a2_2, a2_3, a2_4, a2_5, a2_6, a2_7, a2_8, a2_9, a2_10, a2_11, a2_12,
                            a2_13, a2_14, a2_15]
        self.level_listbg2 = [b2_1, b2_2, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3, b2_3]

    def update(self, level_list, scores):

        chck = 0
        num = 0
        if self.cur == 1:
            self.pos = 0
            self.cur = 2
            for ll in level_list:
                g1_1_2 = Chunk(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, ll,
                               self.enemies, self.items)
                g1_1_2.gen(chck, "g", scores)
                g1_1_2.check_edge = chck

                bg1_1_2 = Chunk(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self.level_listbg[num],
                                self.enemies, self.items)
                bg1_1_2.gen(chck, "bg", scores)
                bg1_1_2.check_edge = chck
                chck += 720
                num += 1

        if self.cur == 3:
            self.pos = 0
            self.cur = 4
            chck = 0
            num = 0
            for ll in level_list:
                g1_1_2 = Chunk(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, ll,
                               self.enemies, self.items)
                g1_1_2.gen(chck, "g", scores)
                g1_1_2.check_edge = chck

                bg1_1_2 = Chunk(self.ai_settings, self.screen, self.g_blocks, self.bg_blocks, self.level_listbg2[num],
                                self.enemies, self.items)
                bg1_1_2.gen(chck, "bg", scores)
                bg1_1_2.check_edge = chck
                chck += 720
                num += 1
