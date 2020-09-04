def site():
    try:
        from urllib.request import urlopen
        p = urlopen('http://www.pudim.com.br/')
    except:
        print('\033[31mSite não encontrado\033[m')
    else:
        print('\033[35mSite encontrado')
        return p

site()