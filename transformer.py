from typing import List, Dict

def get_winner_loser_per_year(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    year_to_teams = {}
    for team in data:
        year = team['year']
        if year not in year_to_teams:
            year_to_teams[year] = []
        year_to_teams[year].append(team)
    
    result = []
    for year, teams in year_to_teams.items():
        sorted_teams = sorted(teams, key=lambda x: x['wins'], reverse=True)
        winner = sorted_teams[0]
        loser = sorted_teams[-1]
        result.append({
            'Year': year,
            'Winner': winner['name'],
            'Winner Num. of Wins': winner['wins'],
            'Loser': loser['name'],
            'Loser Num. of Wins': loser['wins'],
        })
    return result