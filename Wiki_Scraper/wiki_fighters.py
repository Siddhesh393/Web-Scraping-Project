### Code snippet for extracting the data Beautifulsoup code

from parsel import Selector
from requests import get
import dateparser
import re

def get_opponents_with_info(html):
    opponents = get_opponents(html)
    for o in opponents:
        if link := o.get('link'):
            response = get(link)
            o['info'] = get_fighter_info(response.text)
    return opponents


def get_opponents(html):
    selector = Selector(text = html)
    matches = selector.xpath('//table[@class = "wikitable"]')[0]
    trs = matches.xpath(".//tr")

    opponents = []

    for tr in trs[1:]:
        opponent = {
            'link' : None,
            'name' : None,
            'outcome' : None
        } 
        opponent['outcome'] = tr.xpath("./td[1]/text()").get().strip('\n')
        opponent_node = tr.xpath("./td[3]")
        anchors = opponent_node.xpath('a')

        if len(anchors) == 1:
            a = anchors[0]
            href = a.xpath("@href").get()
            opponent['link'] = f"https://en.wikipedia.org{href}"
            opponent_name = a.xpath("text()").get()
        else :
            opponent_name = opponent_node.xpath("text()").get()


        opponent['name'] = opponent_name.strip('\n')
        opponents.append(opponent)
    
    return opponents

def get_fighter_info(html):
    selector = Selector(text=html)
    trs = selector.xpath('//table[@class="infobox vcard"]/tbody/tr')

    fighter_info = {
        'name' : None,
        'image' : None,
        'nickname' : None,
        'nationality' : None,
        'height' : None,
        'weight' : None,
        'birth' : None,
    }

    fighter_info['name'] = trs[0].xpath('.//span/text()').get()
    image = trs[1].xpath('.//a/@href').get()
    fighter_info['image'] = f"https://en.wikipedia.org{image}"
    for tr in trs[2:]:
        key = tr.xpath('./th/text()').get()
        value = tr.xpath('./td/text()').get()

        if key is None or value is None:
            continue

        if key.startswith('Nickname'):
            fighter_info['nickname'] = value
        elif key.startswith('Nationality'):
            fighter_info['nationality'] = value
        elif key.startswith('Height'):
            parts = value.split('(')
            imp = parts[0].strip(' ')
            metric = parts[1].strip(')')
            fighter_info['height'] = {
                'imperial' : imp.replace('\u00a0', ' '),
                'metric' : metric.replace('\u00a0', ' '),
            }
        elif key.startswith('Weight'):
            match = re.search('(?P<imperic>\d{1,3}.lb) \((?P<metric>\d{1,3}.kg); (?P<eng>[\d.]+.st(?: \d+.lb)?)\)', value)
            if match is None:
                print("failed weight match", value)
                continue
            fighter_info['weight'] = {
                'imperial' : match.group('imperic').replace('\u00a0', ' '),
                'metric' : match.group('metric').replace('\u00a0', ' '),
                'english' : match.group('eng').replace('\u00a0', ' '),
            }
        elif key.startswith('Born'):
            born_section = tr.xpath('./td').get()
            match = re.search('<\/span>(?P<date>[\w ,]+)<span', born_section)
            if match is None:
                continue
            fighter_info['birth'] = str(dateparser.parse(match.group('date')))
            
    return fighter_info


### Code snippet using beautifulsoup

# tds = tr.find_all("td")
#         if not tds:
#             continue
#         opponent_node = tds[2]
#         opponent_name = opponent_node.string
#         if opponent_name is None:
#             opponent_name = opponent_node.a.string

#         opponents.append(opponent_name.strip('\n'))