from inputimeout import inputimeout, TimeoutOccurred

while True:
    n1 = ""
    n2 = ""
    while n1 == "":
        try:
            n1 = inputimeout(prompt='Digite o primeiro número: ', timeout=5)
        except TimeoutOccurred:
            n1 = ""
    while n2 == "":
        n2 = input('Digite o segundo número: ')
    print(f'\nA soma dos dois números é {int(n1) + int(n2)}!\n')
  