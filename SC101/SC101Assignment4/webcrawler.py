"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('table', {'class': "t-stripe"})
        total_male = 0
        total_female = 0
        male_index = 2
        female_index = 4
        for tag in tags:
            value = tag.tbody.text.split()  # value = ['1', 'Noah', '183,172' .....] # male is at [2] female at [4]
            for i in range(200):
                # handle male value
                male_num = value[male_index]  # male is at [2]
                male_num_without_commas = ''.join(male_num.split(','))  # remove the comma in the number string
                total_male += int(male_num_without_commas)  # turn into integer and sum of male_value
                male_index += 5  # move to next male value

                # handle female value
                female_num = value[female_index]  # female at [4]
                female_num_without_commas = ''.join(female_num.split(','))  # remove the comma in the number string
                total_female += int(female_num_without_commas)  # turn into integer and sum of female_value
                female_index += 5  # move to next female value
        print(f"Male number: {total_male}")
        print(f"Female number: {total_female}")


if __name__ == '__main__':
    main()
