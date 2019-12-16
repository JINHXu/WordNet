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

        
        
        
        

    def get_synsets(self, noun):
        """
        Returns the list of synsets where noun appears as a lemma. An empty list should be returned if the noun is not part of any WordNet synsets.
        Parameter
        ---------
        noun : Lemma
            a lemma(noun)
        Return
        ------
        synsets : list
            a list of synsets, each synset is an object of Synset
        """
        synsets = []
        return synsets

    def __iter__(self):
        """provide an iteration over its synsets"""
        pass

    def _graph_repr(self):
        pass


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
        return hash(id(self))

    def __iter__(self):
        """provide an iteration over its lemmas"""
        pass

    def _node_repr(self):
        pass


class Relation:
     """ The Relation class stores the origin and the destination of the relation.(functions as the Edge class of a Graph class)"""

    def __init__(self, origin, destinition):
        """The constructor of the edge class Realtion of Graph Synset
        Parameters
        ----------
        origin : string 
            id of origin synset
        
        destination : string
            id of destination synset
        """
        self._origin = oringin
        self._destination = destination

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

   
    def _edge_repr(self):
        pass
class Lemma:
    """The Lemma class stores lemma."""

    def __init__(self, lemma, idList, glossesList):
        """The constructor of the Lemma class
        Parameters
        ----------
        lemma : string
            a lemma in WordNet
        idList : list
            a list of ids of this lemma(each id is a string)
        glossesList : list
            a list of glosses of this lemma(each gloss is a string)
        """
        self._lemma = lemma

        # ???

        self._id = idList
        self._glossesList = glossesList
    # to be determined
    @property
    def lemma(self):
        """lemma getter: return the lemma of this lemma
        Return
        ------
        self._lemma : string
            the lemma of this lemma
        """
        return self._lemma

    @property
    def idList(self):
        """idList getter: return a list of ids of this lemma
        Return
        ------
        idList : list
            a list of ids of this lemma
        """
        return self._idList
    
    @property
    def glossesList(self):
        """glossesList getter: return a list of glosses of this lemma
        Return
        ------
        glossesList : list
            a list of glosses of this lemma
        """
        return self._glossesList

    def _lemma_repr(self):
        pass


