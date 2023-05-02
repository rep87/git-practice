# Test python env
def print_hello():
    animals = ['dog', 'cat','hamster'] # in one line
    foods = [
            'Spagetti',
            'Pizza'
            'bib'
            ] # w/o trailng comma
    names =[
            'John',
            'Jane',
            'Gil-dong',
            'dong-eun',
            'Yeon-jin'
    ] # w/ trailing comma
    for f_name in names:
        print(f'hello, {f_name}') 

if __name__ == '__main__':
    print_hello()
