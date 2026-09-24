import builder
import composite
import team


def main():
    x = int(input('Выберите паттерн дял запуска: 1 - строитель, 2 - компоновщик, 3 - команда: '))
    match x:
        case 1: 
            builder.main()
        case 2:
            composite.main()
        case 3:
            team.main()

if __name__ == "__main__":
    main()
