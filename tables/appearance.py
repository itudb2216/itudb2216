class Appearance:
    def __init__(self, appearance_id, game_id, player_id, player_club_id, date, 
        player_pretty_name, competition_id, yellow_cards, red_cards, goals, assists, minutes_played):
        self.appearance_id = appearance_id
        self.game_id = game_id
        self.player_id = player_id
        self.player_club_id = player_club_id
        self.date = date
        self.player_pretty_name = player_pretty_name 
        self.competition_id = competition_id
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.goals = goals
        self.assists = assists
        self.minutes_played = minutes_played

    def add(self):
        query = "INSERT INTO APPEARANCES (appearance_id, game_id, player_id, player_club_id, date, player_pretty_name, competition_id, yellow_cards, red_cards, goals, assists, minutes_played) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        tupel = (self.appearance_id, self.game_id, self.player_id, self.player_club_id, self.date, self.player_pretty_name, self.competition_id, self.yellow_cards, self.red_cards, self.goals, self.assists, self.minutes_played)
        return query, tupel

    def update(self, old_appearance_id):
        query = "UPDATE APPEARANCES SET appearance_id = ?, game_id = ?, player_id = ?, player_club_id = ?, date = ?, player_pretty_name = ?, competition_id = ?, yellow_cards = ?, red_cards = ?, goals = ?, assists = ?, minutes_played = ? WHERE (appearance_id = ?)"
        tupel = (self.appearance_id, self.game_id, self.player_id, self.player_club_id, self.date, self.player_pretty_name, self.competition_id, self.yellow_cards, self.red_cards, self.goals, self.assists, self.minutes_played, old_appearance_id)
        return query, tupel

    def delete(self):
        query = "DELETE FROM APPEARANCES WHERE (appearance_id = ?)"
        return query, (self.appearance_id,)