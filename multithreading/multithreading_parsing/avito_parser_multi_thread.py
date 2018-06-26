import datetime
import time
from multiprocessing.pool import ThreadPool

import bs4
import requests


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


def parsing_process(query):
    raw_page = fetch_avito_page(query)
    results = parse_avito_search_results(raw_page)
    time.sleep(1)
    print_parsed_results(results)
    return results


def flat(list):
    return [item for sublist in list for item in sublist]


def get_results_from_avito(queries):
    # for query in range(len(queries)):
    #     parsing_process(query)

    pool = ThreadPool(3)
    return flat(pool.map(parsing_process, queries))
    # return pool.map(parsing_process, queries)


def print_parsed_results(results):
    for item in results:
        print("\n", item)

        # for key, value in item.items():
        #     if value == None:
        #         # print("По текущему запросу ничего не найдено...")
        #         break
        #     print("\n", item)


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
    ]

    start_time = datetime.datetime.now()
    # results = get_results_from_avito(queries)
    get_results_from_avito(queries)
    # print_parsed_results(results)
    print("\n" + "Время выполнения программы: ", datetime.datetime.now() - start_time)


if __name__ == '__main__':
    main()
