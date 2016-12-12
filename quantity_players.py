while True:
    try:
        q = int(input(' vvedite kolichestvo igrokov: '))
    except ValueError:
        print('eto ne chislo!! ')
        continue
    break
print('uchastvuyut', q, 'igroka')
