'''
Copyright Daniela Cojocaru 2022:)
'''

class Vote:
    '''
    Definition of a single vote object
    '''

    # Exercise 1
    def __init__(self, preference_list):
        self.preference_list = preference_list

    def __str__(self):
        if len(self.preference_list) == 0:
            return 'Blank'
        else:
            return ' > '.join(self.preference_list)

    def __repr__(self):
        return 'Vote(' + str(self.preference_list) + ')'

    def first_preference(self):
        '''
        Returns the first preference in a vote
        or none if the vote is empty
        '''
        if len(self.preference_list) != 0:
            return self.preference_list[0]
        return None

    # Exercise 6
    def preference(self, names):
        """Return the first preference in a vote"""
        for pref in self.preference_list:
            if pref in names:
                return pref
        return None

class Election:
    '''
    A basic election class
    '''

    # Exercise 2
    def __init__(self, parties):
        self.parties = parties
        self.blank = []
        self.piles = {name: [] for name in self.parties}

    def add_vote(self, vote):
        """Append the vote to the corresponding pile."""
        if vote.first_preference() is None:
            self.blank.append(vote)
        else:
            self.piles[vote.first_preference()].append(vote)

    def status(self):
        """Return the current status of the election:
        a dictionary mapping each of the party names in the piles
        to the number of votes in their pile.
        """
        votes = {}
        for party, vote_count in self.piles.items():
            votes[party] = len(vote_count)

        return votes

    # Exercise 3
    def add_votes_from_file(self, filename):
        """
        Convert each line of the file into a Vote,
        and append each of the votes to the correct pile.
        """
        infile = open(filename, 'r', encoding = "utf-8")
        for line in infile:
            if line[0] == '\n':
                self.add_vote(Vote([]))
            else:
                prefs = line.strip('\n').split(' ')
                for preference in prefs:
                    if preference not in self.parties:
                        prefs.remove(preference)
                self.add_vote(Vote(prefs))

# Exercise 4
class FirstPastThePostElection(Election):
    """
    First-past-the-post elections: whoever gets the most first-preference votes wins.
    """
    def winner(self):
        """Return the winner of this election under
        the first-past-the-post system, or None if
        the election is tied.
        """
        max_votes = 0
        max_key = ''
        for party, votes in self.status().items():
            if votes > max_votes:
                #print (f'{party}, {votes}, {max_votes}')
                max_votes = votes
                max_key = party

        for party, votes in self.status().items():
            if votes == max_votes and party != max_key:
                return None
        if max_votes == 0:
            return None
        return max_key

# Exercise 5
class WeightedElection(Election):
    """
    Weighted elections: each vote contributes to a party's total
    according to that party's position among the vote's preferences.
    """
    def status(self):
        """Returns a dictionary with keys being the parties
        and values being the number of points (counted using
        the weighted scheme) that the party got.
        """
        votes = {name: 0 for name in self.parties}
        for value in self.piles.items():
            for vote in value[1]:
                k = 0
                for choice in vote.preference_list:
                    votes[choice] += 5 - k
                    k += 1
        return votes

    def winner(self):
        """
        Return the winner of this election under
        the weighted voting scheme.
        """

        return sorted(self.status().items(), key=lambda y: y[1], reverse=True)[0][0]

# Exercise 7
class PreferentialElection(Election):
    """
    Simple preferential/instant-runoff elections.
    """

    def __init__(self, parties):
        super().__init__(parties)  # Initialize as for Elections
        self.dead = []

    def eliminate(self, party):
        """Remove the given party from piles, and redistribute its
        votes among the parties not yet eliminated, according to
        their preferences.  If all preferences have been eliminated,
        then add the vote to the dead list.
        """
        pass
