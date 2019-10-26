from level_gen import Chunk

mainClock = pygame.time.Clock()


def run_game():
    pygame.init()
    pygame.display.set_caption("Mario")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    g_blocks = Group()
    bg_blocks = Group()
    mario = Mario(ai_settings, screen, g_blocks)

    #gf.create_blocks(ai_settings, screen, blocks, 500, 368+32, 400)
    #gf.create_blocks(ai_settings, screen, blocks, 500, 280, 400)
    #gf.create_blocks(ai_settings, screen, blocks, 500+32, 280, 400)
    #gf.create_blocks(ai_settings, screen, blocks, 500+64, 280, 400)
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
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000023",
        "000000000000054",
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
        "000000005400000",
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
        "054000000000540",
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
        "000000000000000",
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
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
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

    a8 = [
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

    a9 = [
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
        "000000000000006",
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
        "000000000000000",
        "000000000000000",
        "000000000000002",
        "000000000000005",
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
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000000000000000",
        "000600000000000",
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
    g1_1_1 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a1)
    g1_1_2 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a2)
    g1_1_3 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a3)
    g1_1_4 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a4)
    g1_1_5 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a5)
    g1_1_6 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a6)
    g1_1_7 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a7)
    g1_1_8 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a8)
    g1_1_9 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a9)
    g1_1_10 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a10)
    g1_1_11 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a11)
    g1_1_12 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a12)
    g1_1_13 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a13)
    g1_1_14 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a14)
    g1_1_15 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a15)
    g1_1_16 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a16)
    g1_1_17 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a17)
    g1_2_1 = Chunk(ai_settings, screen, g_blocks, bg_blocks, a2_1)
    g1_1_1.gen(0, "g")
    g1_1_2.gen(720, "g")
    g1_1_3.gen(1440, "g")
    g1_1_4.gen(2160, "g")
    g1_1_5.gen(2880, "g")
    g1_1_6.gen(3600, "g")
    g1_1_7.gen(4320, "g")
    g1_1_8.gen(5040, "g")
    g1_1_9.gen(5760, "g")
    g1_1_10.gen(6480, "g")
    g1_1_11.gen(7200, "g")
    g1_1_12.gen(7920, "g")
    g1_1_13.gen(8640, "g")
    g1_1_14.gen(9360, "g")
    g1_1_15.gen(10080, "g")
    g1_1_16.gen(10800, "g")
    g1_1_17.gen(11520, "g")
    g1_2_1.gen(12240, "g")

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
        "bbb2bpqrbbbbbbb",
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

    bg1_1_1 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b1)
    bg1_1_2 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b2)
    bg1_1_3 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b3)
    bg1_1_4 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b4)
    bg1_1_5 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b5)
    bg1_1_6 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b6)
    bg1_1_7 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b7)
    bg1_1_8 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b8)
    bg1_1_9 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b9)
    bg1_1_10 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b10)
    bg1_1_11 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b11)
    bg1_1_12 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b12)
    bg1_1_13 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b13)
    bg1_1_14 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b14)
    bg1_1_15 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b15)
    bg1_2_1 = Chunk(ai_settings, screen, g_blocks, bg_blocks, b2_1)
    bg1_1_1.gen(0, "bg")
    bg1_1_2.gen(720, "bg")
    bg1_1_3.gen(1440, "bg")
    bg1_1_4.gen(2160, "bg")
    bg1_1_5.gen(2880, "bg")
    bg1_1_6.gen(3600, "bg")
    bg1_1_7.gen(4320, "bg")
    bg1_1_8.gen(5040, "bg")
    bg1_1_9.gen(5760, "bg")
    bg1_1_10.gen(6480, "bg")
    bg1_1_11.gen(7200, "bg")
    bg1_1_12.gen(7920, "bg")
    bg1_1_13.gen(8640, "bg")
    bg1_1_14.gen(9360, "bg")
    bg1_1_15.gen(10080, "bg")
    bg1_2_1.gen(12240, "bg")
    while True:
        gf.check_events(ai_settings, screen, mario)
        mario.update(g_blocks, bg_blocks)

        gf.update_screen(ai_settings, screen, mario, g_blocks, bg_blocks)
        mainClock.tick(40)


run_game()
