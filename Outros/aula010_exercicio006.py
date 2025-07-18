def ihsp():
    from time import sleep
    while True:
        print("-="*3, "Sistema de Ajuda PyHelp", "=-"*3)
        cmd = str(input("Qual comando você quer saber? ")).lower()
        msg = f"Buscando sobre {cmd}"
        print("-" * (len(msg) + 6))
        print(f"{msg:>{len(msg) + 3}}")
        print("-" * (len(msg) + 6))
        sleep(1)
        if cmd == "fim":
            msg = "Até logo"
            print("-" * (len(msg) + 6))
            print(f"{msg:>{len(msg) + 3}}")
            print("-" * (len(msg) + 6))
            break
        help(cmd)


ihsp()