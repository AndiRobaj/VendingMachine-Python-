for ora in range(24):
    for minut in range(60):
        for sekonda in range(60):
            if sekonda % 2 == 0:
                continue
            print(f'Ora: {ora}, minuta: {minut}, sekonda: {sekonda}')