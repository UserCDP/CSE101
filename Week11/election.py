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
        return 'Vote([' + ','.join(self.preference_list) + '])'

    def first_preference(self):
        '''
        Returns the first preference in a vote
        or none if the vote is empty
        '''
        if len(self.preference_list) != 0:
            return self.preference_list[0]
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
        infile = open(filename, 'r')
        for line in infile:
            if line[0] == '\n':
                self.add_vote(Vote([]))
            else:
                self.add_vote(Vote(line.strip('\n').split(' ')))

    # Exercise 4
    def first_past_the_post_winner(self):
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
    def weighted_status(self):
        """Returns a dictionary with keys being the parties
        and values being the number of points (counted using
        the weighted scheme) that the party got.
        """
        votes = self.status()
        k = 0
        print(self.piles)
        for pile in self.piles.items():
            votes[pile[0]] += 5 - k
            k += 1
        return votes

    def weighted_winner(self):
        """
        Return the winner of this election under
        the weighted voting scheme.
        """
        return sorted(self.status().items())
