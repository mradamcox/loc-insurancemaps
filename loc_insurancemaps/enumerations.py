MONTH_CHOICES = [
    (1, "JAN."),
    (2, "FEB."),
    (3, "MAR."),
    (4, "APR."),
    (5, "MAY."),
    (6, "JUN."),
    (7, "JUL."),
    (8, "AUG."),
    (9, "SEP."),
    (10, "OCT."),
    (11, "NOV."),
    (12, "DEC."),
]
STATE_CHOICES = [
    ('alabama', 'Alabama'),
    ('alaska', 'Alaska'),
    ('arizona', 'Arizona'),
    ('arkansas', 'Arkansas'),
    ('california', 'California'),
    ('colorado', 'Colorado'),
    ('connecticut', 'Connecticut'),
    ('delaware', 'Delaware'),
    ('florida', 'Florida'),
    ('georgia', 'Georgia'),
    ('hawaii', 'Hawaii'),
    ('idaho', 'Idaho'),
    ('illinois', 'Illinois'),
    ('indiana', 'Indiana'),
    ('iowa', 'Iowa'),
    ('kansas', 'Kansas'),
    ('kentucky', 'Kentucky'),
    ('louisiana', 'Louisiana'),
    ('maine', 'Maine'),
    ('maryland', 'Maryland'),
    ('massachusetts', 'Massachusetts'),
    ('michigan', 'Michigan'),
    ('minnesota', 'Minnesota'),
    ('mississippi', 'Mississippi'),
    ('missouri', 'Missouri'),
    ('montana', 'Montana'),
    ('nebraska', 'Nebraska'),
    ('nevada', 'Nevada'),
    ('new hampshire', 'New Hampshire'),
    ('new jersey', 'New Jersey'),
    ('new mexico', 'New Mexico'),
    ('new york', 'New York'),
    ('north carolina', 'North Carolina'),
    ('north dakota', 'North Dakota'),
    ('ohio', 'Ohio'),
    ('oklahoma', 'Oklahoma'),
    ('oregon', 'Oregon'),
    ('pennsylvania', 'Pennsylvania'),
    ('rhode island', 'Rhode Island'),
    ('south carolina', 'South Carolina'),
    ('south dakota', 'South Dakota'),
    ('tennessee', 'Tennessee'),
    ('texas', 'Texas'),
    ('utah', 'Utah'),
    ('vermont', 'Vermont'),
    ('virginia', 'Virginia'),
    ('washington', 'Washington'),
    ('west virginia', 'West Virginia'),
    ('wisconsin', 'Wisconsin'),
    ('wyoming', 'Wyoming'),
]
STATE_ABBREV = {
    'alabama': 'Ala.',
    'alaska': 'Alaska',
    'arizona': 'Ariz.',
    'arkansas': 'Ark.',
    'california': 'Calif.',
    'colorado': 'Colo.',
    'connecticut': 'Conn.',
    'delaware': 'Del.',
    'florida': 'Fla.',
    'georgia': 'Ga.',
    'hawaii': 'Hawaii',
    'idaho': 'Idaho',
    'illinois': 'Ill.',
    'indiana': 'Ind.',
    'iowa': 'Iowa',
    'kansas': 'Kan.',
    'kentucky': 'Ky.',
    'louisiana': 'La.',
    'maine': 'Maine',
    'maryland': 'Md.',
    'massachusetts': 'Mass.',
    'michigan': 'Mich.',
    'minnesota': 'Minn.',
    'mississippi': 'Miss.',
    'missouri': 'Mo.',
    'montana': 'Mont.',
    'nebraska': 'Neb.',
    'nevada': 'Nev.',
    'new hampshire': 'N.H.',
    'new jersey': 'N.J.',
    'new mexico': 'N.M.',
    'new york': 'N.Y.',
    'north carolina': 'N.C.',
    'north dakota': 'N.D.',
    'ohio': 'Ohio',
    'oklahoma': 'Okla.',
    'oregon': 'Ore.',
    'pennsylvania': 'Pa.',
    'rhode island': 'R.I.',
    'south carolina': 'S.C.',
    'south dakota': 'S.D.',
    'tennessee': 'Tenn.',
    'texas': 'Texas',
    'utah': 'Utah',
    'vermont': 'Vt.',
    'virginia': 'Va.',
    'washington': 'Wash.',
    'west virginia': 'W.Va.',
    'wisconsin': 'Wis.',
    'wyoming': 'Wyo.',
}
STATE_POSTAL = {
    'alabama': 'al',
    'alaska': 'ak',
    'arizona': 'az',
    'arkansas': 'ar',
    'california': 'ca',
    'colorado': 'co',
    'connecticut': 'cn',
    'delaware': 'de',
    'florida': 'fl',
    'georgia': 'ga',
    'hawaii': 'hi',
    'idaho': 'id',
    'illinois': 'il',
    'indiana': 'in',
    'iowa': 'ia',
    'kansas': 'ka',
    'kentucky': 'ky',
    'louisiana': 'la',
    'maine': 'me',
    'maryland': 'md',
    'massachusetts': 'ma',
    'michigan': 'mi',
    'minnesota': 'mn',
    'mississippi': 'ms',
    'missouri': 'mo',
    'montana': 'mn',
    'nebraska': 'ne',
    'nevada': 'nv',
    'new hampshire': 'nh',
    'new jersey': 'nj',
    'new mexico': 'nm',
    'new york': 'ny',
    'north carolina': 'nc',
    'north dakota': 'nd',
    'ohio': 'oh',
    'oklahoma': 'ok',
    'oregon': 'or',
    'pennsylvania': 'pa',
    'rhode island': 'ri',
    'south carolina': 'sc',
    'south dakota': 'sd',
    'tennessee': 'tn',
    'texas': 'tx',
    'utah': 'ut',
    'vermont': 'vt',
    'virginia': 'va',
    'washington': 'wa',
    'west virginia': 'wv',
    'wisconsin': 'wi',
    'wyoming': 'wy',
}
STATE_NAMES = [i[0] for i in STATE_CHOICES]
STATE_LOOKUP = { i[1]: i[0] for i in STATE_CHOICES }
STATE_POSTAL_LOOKUP = { v: k for k, v in STATE_POSTAL.items() }
