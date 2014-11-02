#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NYC Restaurant Inspection
    """

GRADING = {'A': 100.0, 'B': 90.0, 'C': 80.0, 'D': 70.0, 'F': 60.0}


def get_score_summary(filename):
    """Average scores for each borough

    Args: filename: name of the file to parse

    Ex: get_score_summary('inspection_results.csv')
    >>> {'BRONX': (156, 0.9762820512820514), 'BROOKLYN':
    (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955),
    'MANHATTAN': (748, 0.9771390374331531), 'QUEENS':
    (414, 0.9719806763285017)}
    """
    
    fh = open(filename, 'r')
    line = fh.readline()
    restos = {}
    while line:
        rest = {line[0]: [line[10], line[1]]}
        if (line[10] is True) and (line[10] != 'P'):
            restos.update(rest)
            line = fh.readline()
        else:
            line = fh.readline()
            continue
    fh.close()
    bx = 0
    bxscore = 0.0
    bk = 0
    bkscore = 0.0
    mh = 0
    mhscore = 0.0
    qu = 0
    quscore = 0.0
    si = 0
    siscore = 0.0
    for i, j in restos.values():
        if j == 'BRONX':
            bx += 1
            if i == 'A':
                bxscore += 100.0
            elif i == 'B':
                bxscore += 90.0
            elif i == 'C':
                bxscore += 80.0
            elif i == 'D':
                bxscore += 70.0
            else:
                bxscore += 60.0
        elif j == 'BROOKLYN':
            bk += 1
            if i == 'A':
                bkscore += 100.0
            elif i == 'B':
                bkscore += 90.0
            elif i == 'C':
                bkscore += 80.0
            elif i == 'D':
                bkscore += 70.0
            else:
                bkscore += 60.0
        elif j == 'MANHATTAN':
            mh += 1
            if i == 'A':
                mhscore += 100.0
            elif i == 'B':
                mhscore += 90.0
            elif i == 'C':
                mhscore += 80.0
            elif i == 'D':
                mhscore += 70.0
            else:
                mhscore += 60.0
        elif j == 'QUEENS':
            qu += 1
            if i == 'A':
                quscore += 100.0
            elif i == 'B':
                quscore += 90.0
            elif i == 'C':
                quscore += 80.0
            elif i == 'D':
                quscore += 70.0
            else:
                quscore += 60.0
        else:
            si += 1
            if i == 'A':
                siscore += 100.0
            elif i == 'B':
                siscore += 90.0
            elif i == 'C':
                siscore += 80.0
            elif i == 'D':
                siscore += 70.0
            else:
                siscore += 60.0
        scores = {'BRONX': (bx, (bxscore / bx)), 'BROOKLYN': (bk, (bkscore / bk)),
                  'STATEN ISLAND': (si, (siscore / si)), 'MANHATTAN': (mh / (mhscore)),
                  'QUEENS': (qu, (quscore / qu))}
        return scores
