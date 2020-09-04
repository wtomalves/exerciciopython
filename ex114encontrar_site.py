def website():
    r = 0
    import requests

    try:
        r = requests.get('http://www.pudim.com.br/')
        b = r.status_code
    except:
        print('\033[31mSite não encontrado\033[m')
    else:
        print('\033[35mSite encontrado')

    return r

website()