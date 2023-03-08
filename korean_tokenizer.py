from pecab import PeCab

pecab = PeCab()


def tokenizer(sentence):
    pos = pecab.pos(sentence)

    # NNG: 일반명사, NNP: 고유명사, VV: 동사, VA: 형용사, MAG: 일반부사, IC: 감탄사
    words = [p[0] for p in pos if p[1] in [
        'NNG', 'NNP', 'VV', 'VA', 'MAG', 'IC']]

    # NP: 대명사, VV: 동사, VA: 형용사, VX: 보조용언
    plus = [p[0] for p in pos if p[1].find(
        'NP+') != -1 or p[1].find('VV+') != -1 or p[1].find('VA+') != -1 or p[1].find('VX+') != -1]

    # SY: 기호, SF: 마침표, 물음표, 느낌표, 쉼표, 세미콜론, 콜론, 빗금, 줄표, 따옴표, 괄호표, 줄임표
    symbols = set([p[0] for p in pos if p[1] in ['SY', 'SF'] and p[0] == '?'])
    return words + plus + list(symbols)
