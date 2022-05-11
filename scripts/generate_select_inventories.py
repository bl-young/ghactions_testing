import stewi

def main(inventory, years):
    print(inventory)
    print(years)
    if '-' in years:
        years_list = years.split('-')
        year_iter = list(range(int(years_list[0]), int(years_list[1]) + 1))
    else:
        # Else only a single year defined, create an array of one:
        year_iter = [years]
    for i_year in year_iter:
        stewi.globals.generate_inventory(inventory, i_year)

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--years', help='description for option1')
    parser.add_argument('--inventory', help='description for option2')

    args = vars(parser.parse_args())

    main(args['inventory'], args['years'])
