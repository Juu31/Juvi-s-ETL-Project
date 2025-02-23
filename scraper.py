import aiohttp
import asyncio
from bs4 import BeautifulSoup
from typing import List, Dict

async def fetch_page(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()

async def scrape_all_pages(base_url: str) -> List[Dict[str, str]]:
    all_data = []
    async with aiohttp.ClientSession() as session:
        page_num = 1
        while True:
            url = f"{base_url}?page_num={page_num}"
            html = await fetch_page(session, url)
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.select('tr.team')
            if not rows:
                break
            for row in rows:
                # Handle empty fields by providing default values
                ot_losses = row.select_one('.ot-losses').text.strip()
                ot_losses = int(ot_losses) if ot_losses else 0  # Default to 0 if empty

                win_percentage = row.select_one('.pct').text.strip()
                win_percentage = float(win_percentage) if win_percentage else 0.0  # Default to 0.0 if empty

                goals_for = row.select_one('.gf').text.strip()
                goals_for = int(goals_for) if goals_for else 0  # Default to 0 if empty

                goals_against = row.select_one('.ga').text.strip()
                goals_against = int(goals_against) if goals_against else 0  # Default to 0 if empty

                plus_minus = row.select_one('.diff').text.strip()
                plus_minus = int(plus_minus) if plus_minus else 0  # Default to 0 if empty

                team_data = {
                    'name': row.select_one('.name').text.strip(),
                    'year': int(row.select_one('.year').text.strip()),
                    'wins': int(row.select_one('.wins').text.strip()),
                    'losses': int(row.select_one('.losses').text.strip()),
                    'ot_losses': ot_losses,  # OT Losses (handled empty case)
                    'win_percentage': win_percentage,  # Win % (handled empty case)
                    'goals_for': goals_for,  # Goals For (handled empty case)
                    'goals_against': goals_against,  # Goals Against (handled empty case)
                    'plus_minus': plus_minus,  # + / - (handled empty case)
                }
                all_data.append(team_data)
            page_num += 1
    return all_data