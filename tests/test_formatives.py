import pytest
from ithkuil.parser import parseWord

words_to_test = [
    
    ('iskoùt', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'i',
            'Cx': None,
            'Vp': None,
            'Cr': 'sk',
            'Vc': 'où',
            'Ci+Vi': None,
            'Ca': 't',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('iskoút', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'i',
            'Cx': None,
            'Vp': None,
            'Cr': 'sk',
            'Vc': 'oú',
            'Ci+Vi': None,
            'Ca': 't',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -1
        }),
    
    ('ròihwâl', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': None,
            'Cx': None,
            'Vp': None,
            'Cr': 'r',
            'Vc': 'òi',
            'Ci+Vi': 'hwâ',
            'Ca': 'l',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -1
        }),
    
    ('òspâtlök', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'ò',
            'Cx': None,
            'Vp': None,
            'Cr': 'sp',
            'Vc': 'â',
            'Ci+Vi': None,
            'Ca': 'tl',
            'VxC': [{ 'type': 'k', 'degree': 'ö' }],
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -1
        }),
    
    ('ksûtpöör', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': None,
            'Cx': None,
            'Vp': None,
            'Cr': 'ks',
            'Vc': 'û',
            'Ci+Vi': None,
            'Ca': 'tp',
            'VxC': [{ 'type': 'r', 'degree': 'öö' }],
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -1
        }),
    
    ('áksiyor', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'á',
            'Cx': None,
            'Vp': None,
            'Cr': 'ks',
            'Vc': 'i',
            'Ci+Vi': 'yo',
            'Ca': 'r',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -3
        }),
    
    ('ëitlàrrun',  {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'ëi',
            'Cx': None,
            'Vp': None,
            'Cr': 'tl',
            'Vc': 'à',
            'Ci+Vi': None,
            'Ca': 'rr',
            'VxC': [{ 'type': 'n', 'degree': 'u' }],
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -3
        }),
    
    ('ôrümzìl', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'ô',
            'Cx': None,
            'Vp': None,
            'Cr': 'r',
            'Vc': 'ü',
            'Ci+Vi': None,
            'Ca': 'mz',
            'VxC': [{ 'type': 'l', 'degree': 'ì' }],
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -3
        }),
    
    ('öömolûk', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'öö',
            'Cx': None,
            'Vp': None,
            'Cr': 'm',
            'Vc': 'o',
            'Ci+Vi': None,
            'Ca': 'l',
            'VxC': [{ 'type': 'k', 'degree': 'û' }],
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -3
        }),
    
    ('pʰal', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': None,
            'Cx': None,
            'Vp': None,
            'Cr': 'pʰ',
            'Vc': 'a',
            'Ci+Vi': None,
            'Ca': 'l',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('eqoec', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'e',
            'Cx': None,
            'Vp': None,
            'Cr': 'q',
            'Vc': 'oe',
            'Ci+Vi': None,
            'Ca': 'c',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('¯üaklaršlá', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'üa',
            'Cx': None,
            'Vp': None,
            'Cr': 'kl',
            'Vc': 'a',
            'Ci+Vi': None,
            'Ca': 'ršl',
            'VxC': None,
            'Vf': 'á',
            'Cb': None,
            'tone': '¯',
            'stress': -1
        }),
    
    ('uipʰawâtļûxe’ň', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'ui',
            'Cx': None,
            'Vp': None,
            'Cr': 'pʰ',
            'Vc': 'a',
            'Ci+Vi': 'wâ',
            'Ca': 'tļ',
            'VxC': [{ 'type': 'x', 'degree': 'û' }],
            'Vf': 'e',
            'Cb': 'ň',
            'tone': None,
            'stress': -2
        }),
    
    ('hremsoqaiţsurkoi', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': 'hr',
            'Cs': None,
            'Vr': 'e',
            'Cx': 'ms',
            'Vp': 'o',
            'Cr': 'q',
            'Vc': 'ai',
            'Ci+Vi': None,
            'Ca': 'ţs',
            'VxC': [{ 'type': 'rk', 'degree': 'u' }],
            'Vf': 'oi',
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('/qʰûl-lyai’svukšei’arpîptó’ks', {
            'type': 'formative',
            'Cv': 'qʰ',
            'Vl': 'û',
            'Cg': None,
            'Cs': 'l-ly',
            'Vr': 'ai',
            'Cx': 'sv',
            'Vp': 'u',
            'Cr': 'kš',
            'Vc': 'ei’a',
            'Ci+Vi': None,
            'Ca': 'rp',
            'VxC': [{ 'type': 'pt', 'degree': 'î' }],
            'Vf': 'ó',
            'Cb': 'ks',
            'tone': '/',
            'stress': -1
        }),
    
    ('elal', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'e',
            'Cx': None,
            'Vp': None,
            'Cr': 'l',
            'Vc': 'a',
            'Ci+Vi': None,
            'Ca': 'l',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('pʰall', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': None,
            'Cx': None,
            'Vp': None,
            'Cr': 'pʰ',
            'Vc': 'a',
            'Ci+Vi': None,
            'Ca': 'll',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('upšáll', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'u',
            'Cx': None,
            'Vp': None,
            'Cr': 'pš',
            'Vc': 'á',
            'Ci+Vi': None,
            'Ca': 'll',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -1
        }),
    
    ('eqatļ', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'e',
            'Cx': None,
            'Vp': None,
            'Cr': 'q',
            'Vc': 'a',
            'Ci+Vi': None,
            'Ca': 'tļ',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        }),
    
    ('aukkras', {
            'type': 'formative',
            'Cv': None,
            'Vl': None,
            'Cg': None,
            'Cs': None,
            'Vr': 'au',
            'Cx': None,
            'Vp': None,
            'Cr': 'kkr',
            'Vc': 'a',
            'Ci+Vi': None,
            'Ca': 's',
            'VxC': None,
            'Vf': None,
            'Cb': None,
            'tone': None,
            'stress': -2
        })  
]

@pytest.mark.parametrize('word, expected', words_to_test)  
def test_word(word, expected):
    parsedWord = parseWord(word)
    for key in expected:
        if not expected[key]:
            assert key not in parsedWord
        else:
            assert parsedWord[key] == expected[key]
