import pytest

import sys
import pygame
from pygame.locals import *

from game import (
    Game
)
from character import MagmaBoy, HydroGirl
magma_boy = MagmaBoy()
hydro_girl = HydroGirl()

collision_cases = [
# Check for player collisions on floor
(hydro_girl, [], []),
# Check for player collisions on goo

# Check for player collisions on gates

# Check for player collisions on doors

]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("rectangle,tile,hit_list", collision_cases)
def test_collision(rectangle,tile,hit_list):
    assert Game.collision_test(rectangle, tile) == hit_list


"""
# Define sets of test cases.
get_reverse_complement_cases = [
    # Check an empty string
    ("", ""),
    # Check a single nucleotide, which should be the same as the complement.
    ("A", "T"),
    # Check a single nucleotide, which should be the same as the complement.
    ("T", "A"),
    # Check a single nucleotide, which should be the same as the complement.
    ("C", "G"),
    # Check a single nucleotide, which should be the same as the complement.
    ("G", "C"),
    # Check multiple of the same nucleotide.
    ("AAAAAA", "TTTTTT"),
    # Check a nucleotide with every possible character.
    ("ATCG", "CGAT"),
]

rest_of_orf_cases = [
    # Check an empty string
    ("", ""),
    # Check a start followed by a stop.
    ("ATGTGA", "ATG"),
    # Check a case without a stop codon.
    ("ATGAAA", "ATGAAA"),
    # Check a case without a stop codon where the length is not a multiple of 3.
    ("ATGA", "ATGA"),
    # Check a case with a stop codon that is not in the correct frame.
    ("ATGATAGAATGA", "ATGATAGAA"),
    # Check a strand with nested ORFs.
    ("ATGAAAATGGCATGA", "ATGAAAATGGCA"),
]

find_all_orfs_one_frame_cases = [
    # Check an empty string
    ("", []),
    # Check a strand with a single ORF.
    ("ATGTGA", ["ATG"]),
    # Check a strand with two ORFs.
    ("ATGTAAATGAAATAA", ["ATG", "ATGAAA"]),
    # Check a strand with nested ORFs.
    ("ATGAAAATGGCATGA", ["ATGAAAATGGCA"]),
    # Check a case with a stop codon that is not in the correct frame.
    ("ATGATAGAATGA", ["ATGATAGAA"]),
    # Check a case that does not start with the start codon
    ("GTTATGATAGAATGA", ["ATGATAGAA"]),
    # Check a case without a stop codon where the length is not a multiple of 3.
    ("ATGA", ["ATGA"]),
    # Check a case without an ORF
    ("TTTTTTGA", []),
]

find_all_orfs_cases = [
    # Check an empty string
    ("", []),
    # This case from find_all_orfs has no ORFs in other frames, so it should
    # return the same result as in the one_frame case.
    ("ATGTAAATGAAATAA", ["ATG", "ATGAAA"]),
    # Check a strand with a single ORF.
    ("ATGTGA", ["ATG"]),
    # Check a strand with two ORFs.
    ("ATGTAAATGAAATAA", ["ATG", "ATGAAA"]),
    # Check a case without a stop codon where the length is not a multiple of 3.
    ("ATGA", ["ATGA"]),
    # Check a strand with nested ORFs in the same frame.
    ("ATGAAAATGGCATAA", ["ATGAAAATGGCA"]),
    # Check a case with a stop codon that is not in the same frame as
    # the start codon.
    ("ATGATAGAATAA", ["ATGATAGAA"]),
    # Check a case with nested ORFS in different frames
    ("ATGAAAAATGCCCCATAAATAG", ["ATGAAAAATGCCCCA", "ATGCCCCATAAA"]),
    # Check a case without an ORF
    ("TTTTTTGA", []),
    # Check a case that does not start with the start codon
    ("GTTATGATAGA", ["ATGATAGA"]),
    # Check a case that is shifted by 1
    ("AATGTGA", ["ATG"]),
    # Check a case that is shifted by 2
    ("AAATGTGA", ["ATG"]),
]

find_all_orfs_both_strands_cases = [
    # Check an empty string
    ("", []),
    # Check a strand with a single ORF in the normal direction.
    ("ATGTGA", ["ATG"]),
    # Check a strand with a single ORF in the reverse complement.
    ("GGGCAT", ["ATGCCC"]),
    # Test a short strand starting with a start codon whose reverse complement
    # is itself. Thus this should return two copies of the same ORF.
    ("ATGCAT", ["ATGCAT", "ATGCAT"]),
    # Test a strand with nested ORFs in different directions
    ("ATGGCATAA", ["ATGGCA", "ATGCCAT"]),
]

get_longest_orf_cases = [
    # Check an empty string
    ("", ""),
    # An ORF covering the whole strand is by default the longest ORF.
    ("ATGAAAAAAAAA", "ATGAAAAAAAAA"),
    # An ORF with two complements one in the normal and one in the reverse
    # where the longest is in the normal
    ("ATGGCATCCCCCCCCTAA", "ATGGCATCCCCCCCC"),
    # An ORF with two complements one in the normal and one in the reverse
    # where the longest is in the reverse
    ("ATGGCATAA", "ATGCCAT"),
    # An ORF with two complements one in the normal and one in the reverse
    # where their lengths are the same, will return the first one found
    ("ATGCCCTAACTATTTCAT", "ATGCCC"),
]

coding_strand_to_aa_cases = [
    # Check an empty string
    ("", ""),
    # Check a single start codon.
    ("ATG", "M"),
    # Check a case in which the length is a multiple of 3.
    ("ATGCCCGCT", "MPA"),
    # Check a case in which the length is not a multiple of 3.
    ("ATGCCCGCTTT", "MPA"),
    # Check a case with an incomplete start codon.
    ("AT", ""),
]


# Define additional testing lists and functions that check other properties of
# functions in gene_finder.py.
@pytest.mark.parametrize("nucleotide", ["A", "T", "C", "G"])
def test_double_complement(nucleotide):
    
    Check that taking the complement of a complement of a nucleotide produces
    the original nucleotide.
    Args:
        nucleotide: A single-character string representing one of the four DNA
            nucleotides.
    
    assert get_complement(get_complement(nucleotide)) == nucleotide


################################################################################
# Don't change anything below these lines.
################################################################################



@pytest.mark.parametrize("strand,reverse_complement",
                         get_reverse_complement_cases)
def test_get_reverse_complement(strand, reverse_complement):
    assert get_reverse_complement(strand) == reverse_complement


@pytest.mark.parametrize("strand,rest", rest_of_orf_cases)
def test_rest_of_orf(strand, rest):
    assert rest_of_orf(strand) == rest


@pytest.mark.parametrize("strand,orfs", find_all_orfs_one_frame_cases)
def test_find_all_orfs_oneframe(strand, orfs):
    assert Counter(find_all_orfs_one_frame(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_cases)
def test_find_all_orfs(strand, orfs):
    assert Counter(find_all_orfs(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_both_strands_cases)
def test_find_all_orfs_both_strands(strand, orfs):
    assert Counter(find_all_orfs_both_strands(strand)) == Counter(orfs)


@pytest.mark.parametrize("strand,orf", get_longest_orf_cases)
def test_get_longest_orf(strand, orf):
    assert find_longest_orf(strand) == orf


@pytest.mark.parametrize("strand,protein", coding_strand_to_aa_cases)
def test_coding_strand_to_aa(strand, protein):
    assert encode_amino_acids(strand) == protein

"""