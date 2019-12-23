""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 3

    WordNet API
    Course:      Data Structures and Algorithms for CL III - WS1920
    Assignment:  WordNet API
    Author:      Jinghua Xu
    Description: a WordNet class to represent the WordNet synsets and the hyperonymy relation between them, and to support a variety of queries for extracting the information encoded in the hierarchical structure of WordNet.

    Honor Code:  I pledge that this program represents my own work.
"""


class WordNet:
    """API for querying WordNet information"""

    def __init__(self, synsets_file, hypernyms_file):
        """
        Constructor for the WordNet class. Build WordNet based on synsets file and hypernyms file.
        Parameters
        ----------
        synsets_file : string
            The file path of synset file.
        hypernyms_file : string
            The file path of hypernyms file.
        """
        # dictionary id: synset
        id2synset = dict()

        with open(synsets_file, 'r', encoding='utf-8') as f_synsets:
            lines = f_synsets.readlines()
            for line in lines:
                data = line.split(',')
                id = data[0]
                # list of lemmas(string)
                lemmas = data[1].split(' ')
                # list of lemmas(object of Lemma)
                new_lemmas = []
                for lemma in lemmas:
                    l = Lemma(lemma)
                    new_lemmas.append(l)

                gloss = data[2]

                synset = Synset(id, new_lemmas, gloss)

                id2synset[id] = synsets

        self._verticesDict = id2synset

        # dictionary oringin id : list of relations
        origin2relation = dict()
        with open(hypernyms_file, 'r', encoding='utf-8') as f_hypernyms:
            lines = f_hypernyms.readlines()
            for line in lines:

                data = line.split(',')
                origin_id = data[0]
                origin = id2synset[origin_id]

                # list of ids that are hyper
                hypers = data[1:]
                relations = []

                for hyper in hypers:
                    destination_id = hyper
                    destination = origin2relation[destination_id]
                    relation = Relation(origin, destination)
                    realtions.append(realtion)

                origin2relation[origin_id] = relations

        self._edgesDict = origin2relation

        # dictionary lemma : list of synsets where this lemma appears
        lemma2synset = dict()
        for synset in id2synset.values():
            for lemma in synset.lemma:
                lemma_string = lemma.lemma

                if lemma in lemma2synset.keys():
                    lemma2synset[lemma].append(synset)
                else:
                    lemma2synset[lemma] = [synset]

        self._lemmasDict = lemma2synset

    def get_synsets(self, noun):
        """
        Returns the list of synsets where noun appears as a lemma. An empty list should be returned if the noun is not part of any WordNet synsets.
        Parameter
        ---------
        noun : string
            a lemma(noun)
        Return
        ------
        synsets : list
            a list of synsets, each synset is an object of Synset
        """
        lemma = Lemma(noun)
        for synset in self._lemmasDict[lemma]:
            yield synset

    # not used, might be deleted
    def incident_realtions(self, synset):
        """
        A helper function of bfs, returns incident relations of synset.
        Parameter
        ---------
        synset : Synset
            a synset of WordNet
        Return
        ------
        incident_relations : list
            a list of incident edges of this synset
        """
        incident_realtions = self._edgesDict[synset.id]
        return incident_realtions

    def bfs(self, synset):
        """
        Returns a dictionary containing all the hypernym synsets on the paths from the current synset to the root node by runing a bfs traversal.
        Parameter
        ---------
        synset : Synset
            Current seynset from which the bfs will start to the root node.
        Return
        ------
        discovered : dictionary
            A dictionary containing all the hypernym synsets on the paths from the current synset to the root node.
            The keys of the dictionary should be Synset objects representing the hypernyms of synset,
            while the values should be tuples of the form (relation, distance). relation is the Relation edge used to discover that hypernym and distance is the integer distance,
            measured in number of edges, from the synset given as parameter to the current key.
        """
        # level number
        distance = 1
        # return dict
        discovered = dict()
        # list of vertices in each level, first level contains only synset
        level = [synset]
        while(len(level) > 0):
            next_level = []
            # for each vertex in this level(the origins)
            for u in level:
                # incident realtions whose origin is u
                incident_realtions = self._edgesDict[u.id]
                for relation in incident_realtions:
                    # the hyper synset
                    v = relation.destination
                    if v not in discovered:
                        discovered[v] = (relation, distance)
                        next_level.append(v)
            level = next_level
            distance += 1

    def __iter__(self):
        """
        provide an iteration over its synsets
        Return
        ------
        the list of synsets of this wordnet graph
        """
        yield from self.get_synsets()

    def __len__(self):
        return len(self._verticesDict)

    # require further modification/improvement
    def __str__(self):
        return


class Synset:
    """ The node(vertex) class Synset of the Graph class WordNet"""

    def __init__(self, id, lemma, gloss):
        """The constructor of this Synset class.
        Parameters
        ----------
        id : string
            The id if this Synset.
        lemma : list
            List lemmas(objects of Lemma class) of this synset.
        gloss : string
            The gloss of this sysnset.
        """
        self._id = id
        self._lemma = lemma
        self._gloss = gloss

    @property
    def id(self):
        """id getter: Return id associated with this Synset(vertex)
        Return
        -------
        self._id : string
            id associated with the synset
        """
        return self._id

    @property
    def lemma(self):
        """lemma getter: Return a list of lemmas associated with this Sysnset(vertex)
        Return
        -------
        self._lemma : list
            the list of lemmas(objects of Lemma class) associated with this Synset(vertex)
        """
        return self._lemma

    @property
    def gloss(self):
        """gloss getter: return the gloss associated with this Sysnset(vertex)
        Return
        -------
        self._gloss : string
            the gloss associated with this synset"""
        return self._gloss

    def ___hash___(self):
        """will allow vertex to be a map/set key
        Return
        -------
        hash(id(self)) : int
            a hashcode that is then used to insert objects into hashtables aka dictionaries"""
        return hash((self._id, self._lemma, self._gloss))

    def __eq__(self, othr):

        if isinstance(othr, type(self)):
            return ((self._id, self._lemma, self._gloss) == (othr._id, othr._lemma, othr._gloss))

        return NotImplemented

    def __iter__(self):
        """provide an iteration over its lemmas"""
        yield from self._lemma

    def __str__(self):
        return self.id + str(self.lemma) + str(self.gloss)


class Relation:
    """ The Relation class stores the origin and the destination of the relation.(functions as the Edge class of a Graph class)"""

    def __init__(self, origin, destination):
        """
        The constructor of the edge class Realtion of Graph Synset
        Parameters
        ----------
        origin : Synset
            origin vertice(synset)
        destination : Synset
            destination vertice(synset)
        """
        self._origin = origin
        self._destination = destination

    def origin(self):
        return self._origin

    def destination(self):
        return self._destination

    def endpoints(self):
        """Return (origin, destination) tuple for vertices origin and destination.
        Return
        ------
        (self._origin, self._destination) : tuple
            an edge(relation) representation as tuple(origin, destination)
        """
        return (self._origin, self._destination)

    def __hash__(self):
        """
        Will allow edge to be a map/set key.
        Return
        ------
        hash((self._origin, self._destination)) : int
            a hashcode that is then used to insert objects into hashtables aka dictionaries"""
        return hash((self._origin, self._destination))

    def __str__(self):
        return (str(self._origin), str(self._destination))


class Lemma:
    """The Lemma class stores lemma."""

    def __init__(self, lemma):
        """The constructor of the Lemma class
        Parameters
        ----------
        lemma : string
            a lemma in WordNet
        """
        self._lemma = lemma

    @property
    def lemma(self):
        """lemma getter: return the lemma of this lemma
        Return
        ------
        self._lemma : string
            the lemma of this lemma
        """
        return self._lemma

    def __str__(self):
        """__str__ function of lemma class, to make sure meaningful representations when displayed via the print() method
        Returns
        -------
        self._lemma : string
            the string lemma stored in this lemma
        """
        return self._lemma
