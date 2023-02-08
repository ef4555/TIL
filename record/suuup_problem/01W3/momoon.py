
def count_vowels(a):
    m_count = 0
    moon = 'aeiou'
    for i in a:
        if i in moon:
            m_count += 1
    return m_count


count_vowels('apple') #=> 2
count_vowels('banana') #=> 3


