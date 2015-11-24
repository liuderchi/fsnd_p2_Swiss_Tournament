#!/usr/bin/env python
"""tournament.py

Created Date: 2015-11-05
Arthur: Derek Liu
Description: UDND P2: implementation of a Swiss-system tournament
"""

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE from matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE from players;")
    cursor.execute("DELETE from standings;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("select * from players;")
    results = cursor.fetchall()
    db.close()
    return  len(results)


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO players ( name ) VALUES ( %s );" , (name,) ) #avoid injection
    cursor.execute("INSERT INTO standings ( name, wins, matches ) VALUES ( %s, %s, %s );" ,(name, 0, 0)  )
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    my_query = "SELECT * FROM standings ORDER BY wins DESC;"
    cursor.execute(my_query)
    results = cursor.fetchall()
    db.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    csr = db.cursor()

    #update standings: winner
    csr.execute("SELECT pid,name,wins,matches FROM standings WHERE pid=%s;",
                 (winner,))
    results = csr.fetchall()
    wins = results[0][2] + 1
    matches = results[0][3] + 1
    csr.execute("UPDATE standings set wins=%s, matches=%s where pid=%s;",
                (wins, matches, winner))

    #update standings: loser
    csr.execute("SELECT pid,name,wins,matches FROM standings WHERE pid=%s;", (loser,))
    results = csr.fetchall()
    matches = results[0][3] + 1
    csr.execute("UPDATE standings set matches=%s where pid=%s;", (matches, loser))

    #add a match
    csr.execute("SELECT pid,name FROM standings WHERE pid=%s;", (loser,))
    loser_name = csr.fetchall()[0][1]
    csr.execute("SELECT pid,name FROM standings WHERE pid=%s;", (winner,))
    winner_name = csr.fetchall()[0][1]
    csr.execute("INSERT INTO matches (winner, loser) VALUES ( %s, %s);",
                (winner_name, loser_name))

    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []
    standings = playerStandings()
    while len(standings) > 0:
        player1 = standings.pop(0)
        player2 = standings.pop(0)
        pairings[ len(pairings):] = [ (player1[0], player1[1], player2[0], player2[1]) ]
    return pairings
