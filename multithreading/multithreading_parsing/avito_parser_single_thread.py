import bs4
import requests
import datetime


# kemerovo
# rossiya
def fetch_avito_page(query):
    return requests.get(
        'https://www.avito.ru/rossiya',
        params={'q': query}
    )


def parse_avito_search_results(raw_page):
    soup = bs4.BeautifulSoup(raw_page.text, 'html.parser')
    parsed_results = []
    for searched_item in soup.find_all('div', {'class': 'item'}):
        parsed_results.append({
            'title': searched_item.find('a', {'class': 'item-description-title-link'}),
            'price': searched_item.find('div', {'class': 'about'})
        })
    return parsed_results


def get_results_from_avito(queries):
    results = []
    for query in range(len(queries)):
        raw_page = fetch_avito_page(queries[query])
        results = parse_avito_search_results(raw_page)
        print_parsed_results(results)
    return results


def print_parsed_results(results):
    for item in results:
        print("\n", item)


def main():
    queries = [
        'HP-G62',
        'HP',
        'оперативная память DDR3',
        'core i3',
        'core i7',
        'ssd',
        'мониторы',
        'блоки питания',
        'iphone',
        'ноутбуки hp',
        'hp g62',
        'кресло компьютерное',
        'компьютерный стол',
        'компьютерное освещение'
    ]
    start_time = datetime.datetime.now()
    get_results_from_avito(queries)
    print("\n" + "Время выполнения программы: ", datetime.datetime.now() - start_time)


if __name__ == '__main__':
    main()
