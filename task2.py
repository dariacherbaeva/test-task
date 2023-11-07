import os
import requests

HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/116.0.0.0 Safari/537.36",
}


# Есть вероятность, что данные сохранятся некорректно из-за особенностей сайта (решается передачей нужных параметров
# запроса или использованием дополнительных инструментов (например selenium),
# невозможно реализовать для абстрактных ссылок)
# В случае необходимости дальнейшей работы с HTML можно использовать библиотеку BeautifulSoup
def get_urls_html_data(urls_list: list[str], filenames: list[str] = None, directory_name: str = "html"):
    """
    Функция, которая получает из Сети код страниц из списка и сохраняет его (код) на диск

    :param urls_list: список ссылок, обязательный параметр
    :param filenames: список названий файлов на выходе, не обязательный параметр
     (важен порядок, в случае несовпадения длины со списком ссылок не используется)
     :param directory_name: название папки с итоговыми файлами, не обязательный параметр
    """
    counter = 1
    for url in urls_list:
        if not filenames or len(filenames) != len(urls_list):
            file_name = f"file{counter}.html"
        else:
            file_name = f"{filenames[counter - 1]}.html"
        name = f"{directory_name}/{file_name}"
        os.makedirs(os.path.dirname(name), exist_ok=True)
        response = requests.get(url=url, headers=HEADERS)
        with open(name, "a+") as file:
            file.write(response.text)
        counter += 1


URLS_LIST: list[str] = [
    "https://en.wikipedia.org/wiki/Python",
    "https://habr.com/ru/articles/772404/",
    "https://www.britannica.com/topic/Halloween",
]
FILENAMES: list[str] = ["Python Wikipedia", "Habr VPN Article", "Britannica Halloween"]
get_urls_html_data(URLS_LIST, FILENAMES)
