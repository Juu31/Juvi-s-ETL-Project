from typing import List, Dict
from openpyxl import Workbook

def write_to_excel(all_data: List[Dict[str, str]], winner_loser_data: List[Dict[str, str]], output_file: str):
    wb = Workbook()
    
    # Sheet 1: NHL Stats 1990-2011
    ws1 = wb.active
    ws1.title = "NHL Stats 1990-2011"
    # Add headers for the new columns
    ws1.append(['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For', 'Goals Against', '+ / -'])
    for team in all_data:
        ws1.append([
            team['name'],
            team['year'],
            team['wins'],
            team['losses'],
            team['ot_losses'],  # OT Losses
            team['win_percentage'],  # Win %
            team['goals_for'],  # Goals For
            team['goals_against'],  # Goals Against
            team['plus_minus'],  # + / -
        ])
    
    # Sheet 2: Winner and Loser per Year
    ws2 = wb.create_sheet("Winner and Loser per Year")
    ws2.append(['Year', 'Winner', 'Winner Num. of Wins', 'Loser', 'Loser Num. of Wins'])
    for row in winner_loser_data:
        ws2.append([row['Year'], row['Winner'], row['Winner Num. of Wins'], row['Loser'], row['Loser Num. of Wins']])
    
    wb.save(output_file)