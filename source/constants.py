#TODO Load everything here from files not hard code
# system_names = [
#     'Centauri',
#     'Orion',
#     'Wolf',
#     'Cassiopeiae',
#     'Sirius',
#     'Arcturus',
#     'Rigel',
#     'Deneb',
#     'Altair',
#     'Pollux',
#     'Polaris',
#     'Pegasi',
#     'Formalhaut',
#     'Carinae',
#     'Vega',
#     'Ophiuchi',
#     'Puppis',
#     'Achernar',
#     'Junction',
#     'Farpoint',
#     'Balron',
#     'Eridanus',
#     'Acamar',
#     'Acrab',
#     'Acrux',
#     'Acubens',
#     'Adhafera',
#     'Adhara',
#     'Adhil',
#     'Ain',
#     'Aladfar',
#     'Alamak',
#     'Andromeda',
#     'Lyra',
#     'Alathfar',
#     'Cygnus',
#     'Ursa',
#     'Taurus',
#     'Draco',
#     'Pegasus',
#     'Perseus',
#     'Orion',
#     'Scorpius',
#     'Hydra',
#     'Aquila',
#     'Leo',
#     'Canis',
#     'Sagittarius',
#     'Gemini',
#     'Apollo',
#     'Crux',
#     'Libertas',
#     'Canis',
#     'Delphini',
#     'Subra',
#     'Shiva',
#     'Devia',
#     'Vishnu',
#     'Rama',
#     'Ganesh',
#     'Radha',
#     'Parvati',
#     'Shesha',
#     'Lakshmi',
#     'Sukra',
#     'Khepri',
#     'Ra',
#     'Varuna',
#     'Mitra',
#     'Yama',
#     'Indra',
#     'Agni',
#     'Soma',
#     'Dhruva',
#     'Anala',
#     'Ardra',
#     'Deva',
#     'Cthulu',
#     'Azathoth',
#     'Byatis',
#     'Hastur',
#     'Ithaqua',
#     'Kaluut',
#     'Lythalia',
#     'Mnomquah',
#     'Yog-Sothoth',
#     'Nyogtha',
#     'Oorn',
#     'Rokon',
#     'Sthanee',
#     'Thasaidon',
#     'Tsathoggua',
#     'Vibur',
#     'Xalafu',
#     'Xitalu',
#     'Xotli',
#     'Yhashtur',
#     'Zushakon',
#     'Zstylzhemghi',
#     'Nodens',
#     'Ulthar'
# ]

#FIXME: Name generation needs to be better
syllables = {
    0 : 'ab',
    1 : 'ad',
    2 : 'ae',
    3 : 'af',
    4 : 'ag',
    5 : 'ah',
    6 : 'ai',
    7 : 'ak',
    8 : 'al',
    9 : 'am',
    10 : 'an',
    11 : 'ao',
    12 : 'ap',
    13 : 'aq',
    14 : 'ar',
    15 : 'as',
    16 : 'at',
    17 : 'au',
    18 : 'av',
    19 : 'aw',
    20 : 'ax',
    21 : 'ay',
    22 : 'az',
    23 : 'ea',
    24 : 'eb',
    25 : 'ed',
    26 : 'ef',
    27 : 'eg',
    28 : 'eh',
    29 : 'ei',
    30 : 'ek',
    31 : 'el',
    32 : 'em',
    33 : 'en',
    34 : 'eo',
    35 : 'ep',
    36 : 'eq',
    37 : 'er',
    38 : 'es',
    39 : 'et',
    40 : 'eu',
    41 : 'ev',
    42 : 'ew',
    43 : 'ex',
    44 : 'ey',
    45 : 'ez',
    46 : 'ib',
    47 : 'id',
    48 : 'ie',
    49 : 'if',
    50 : 'ig',
    51 : 'ih',
    52 : 'ia',
    53 : 'ik',
    54 : 'il',
    55 : 'im',
    56 : 'in',
    57 : 'io',
    58 : 'ip',
    59 : 'iq',
    60 : 'ir',
    61 : 'is',
    62 : 'it',
    63 : 'iu',
    64 : 'iv',
    65 : 'iw',
    66 : 'ix',
    67 : 'iy',
    68 : 'iz',
    69 : 'oa',
    70 : 'ob',
    71 : 'od',
    72 : 'of',
    73 : 'og',
    74 : 'oh',
    75 : 'oi',
    76 : 'ok',
    77 : 'ol',
    78 : 'om',
    79 : 'on',
    80 : 'oa',
    81 : 'op',
    82 : 'oq',
    83 : 'or',
    84 : 'os',
    85 : 'ot',
    86 : 'ou',
    87 : 'ov',
    88 : 'ow',
    89 : 'ox',
    90 : 'oy',
    91 : 'oz',
    92 : 'oa',
    93 : 'ob',
    94 : 'od',
    95 : 'of',
    96 : 'og',
    97 : 'oh',
    98 : 'oi',
    99 : 'ok',
    100 : 'ol',
    101 : 'om',
    102 : 'on',
    103 : 'oa',
    104 : 'op',
    105 : 'oq',
    106 : 'or',
    107 : 'os',
    108 : 'ot',
    109 : 'ou',
    110 : 'ov',
    111 : 'ow',
    112 : 'ox',
    113 : 'oy',
    114 : 'oz',
    115 : 'ba',
    116 : 'be',
    117 : 'bi',
    118 : 'bo',
    119 : 'bu',
    120 : 'ca',
    121 : 'ce',
    122 : 'ci',
    123 : 'co',
    124 : 'cu',
    125 : 'da',
    126 : 'de',
    127 : 'di',
    128 : 'do',
    129 : 'du',
    130 : 'fa',
    131 : 'fe',
    132 : 'fi',
    133 : 'fo',
    134 : 'fu',
    135 : 'ga',
    136 : 'ge',
    137 : 'gi',
    138 : 'go',
    139 : 'gu',
    140 : 'ha',
    141 : 'he',
    142 : 'hi',
    143 : 'ho',
    144 : 'hu',
    145 : 'ja',
    146 : 'je',
    147 : 'ji',
    148 : 'jo',
    149 : 'ju',
    150 : 'ka',
    151 : 'ke',
    152 : 'ki',
    153 : 'ko',
    154 : 'ku',
    155 : 'ka',
    156 : 'ke',
    157 : 'ki',
    158 : 'ko',
    159 : 'ku',
    160 : 'la',
    161 : 'le',
    162 : 'li',
    163 : 'lo',
    164 : 'lu',
    165 : 'ma',
    166 : 'me',
    167 : 'mi',
    168 : 'mo',
    169 : 'mu',
    170 : 'na',
    171 : 'ne',
    172 : 'ni',
    173 : 'no',
    174 : 'nu',
    175 : 'pa',
    176 : 'pe',
    177 : 'pi',
    178 : 'po',
    179 : 'pu',
    180 : 'qa',
    181 : 'qe',
    182 : 'qi',
    183 : 'qo',
    184 : 'qu',
    185 : 'ra',
    186 : 're',
    187 : 'ri',
    188 : 'ro',
    189 : 'ru',
    190 : 'sa',
    191 : 'se',
    192 : 'si',
    193 : 'so',
    194 : 'su',
    195 : 'ta',
    196 : 'te',
    197 : 'ti',
    198 : 'to',
    199 : 'tu',
    200 : 'va',
    201 : 've',
    202 : 'vi',
    203 : 'vo',
    204 : 'vu',
    205 : 'wa',
    206 : 'we',
    207 : 'wi',
    208 : 'wo',
    209 : 'wu',
    210 : 'xa',
    211 : 'xe',
    212 : 'xi',
    213 : 'xo',
    214 : 'xu',
    215 : 'ya',
    216 : 'ye',
    217 : 'yi',
    218 : 'yo',
    219 : 'yu',
    220 : 'za',
    221 : 'ze',
    222 : 'zi',
    223 : 'zo',
    224 : 'zu',
}

greek_numbers = [
    '',
    'Alpha',
    'Beta',
    'Gamma',
    'Delta',
    'Epsilon',
    'Zeta',
    'Eta',
    'Theta',
    'Iota',
    'Kappa',
    'Lamda',
    'Mu',
    'Nu',
    'Xi',
    'Omicron',
    'Pi',
    'Rho',
    'Sigma',
    'Tau',
    'Upsilon',
    'Phi',
    'Chi',
    'Psi',
    'Omega'
]
