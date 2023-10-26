from bs4 import BeautifulSoup
import requests
import openpyxl

EXCEL = openpyxl.Workbook()

SHEET = EXCEL.active

SHEET.title = "Top Rated Anime"

SHEET.append(["Anime Rank", "Anime Name", "Year Of Release", "IMDB Rating"])



try:

   SOURCE = requests.get("https://www.imdb.com/list/ls033398199/")

   SOURCE.raise_for_status()

   SOUP = BeautifulSoup(SOURCE.text, "html.parser")

   ANIME_SERIES = SOUP.find("div", class_= "lister-list").find_all("div", class_= "lister-item mode-detail")



   for anime in ANIME_SERIES:

       NAME = anime.find("h3", class_="lister-item-header").a.text

       RANK = anime.find("h3", class_="lister-item-header").get_text(strip=True).split(".")[0]

       YEAR = anime.find("span", class_="lister-item-year text-muted unbold").text.strip("()")

       RATING = anime.find("span", class_="ipl-rating-star__rating").text

       print(RANK, NAME, YEAR, RATING)

       SHEET.append([RANK, NAME, YEAR, RATING])



except Exception as e:


   print(e)

EXCEL.save("IMDB Anime Rating.xlsx")



