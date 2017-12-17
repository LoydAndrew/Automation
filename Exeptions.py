def exeption_handling():
    car = {'make': 'bmw','model': '007', 'year': 1999}

    try:
        print (car[color])
    except:
        print("Dictionary key error")
    finally:
        print ('Resolve finally anyway')


exeption_handling()