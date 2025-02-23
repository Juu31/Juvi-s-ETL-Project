import pytest
from transformer import get_winner_loser_per_year

def test_get_winner_loser_per_year():
    data = [
        {'name': 'Team A', 'year': 1990, 'wins': 50, 'losses': 20},
        {'name': 'Team B', 'year': 1990, 'wins': 40, 'losses': 30},
        {'name': 'Team C', 'year': 1991, 'wins': 60, 'losses': 10},
        {'name': 'Team D', 'year': 1991, 'wins': 30, 'losses': 40},
    ]
    result = get_winner_loser_per_year(data)
    assert result == [
        {'Year': 1990, 'Winner': 'Team A', 'Winner Num. of Wins': 50, 'Loser': 'Team B', 'Loser Num. of Wins': 40},
        {'Year': 1991, 'Winner': 'Team C', 'Winner Num. of Wins': 60, 'Loser': 'Team D', 'Loser Num. of Wins': 30},
    ]