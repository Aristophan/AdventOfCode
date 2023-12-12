import utils as u
import numpy as np
import math as m
import copy

data = [line.split() for line in open('inputs/7.txt').read().strip().split('\n')]
letters = u.LETTERS
cards = list(map(str,['J',2,3,4,5,6,7,8,9,'T','Q','K','A']))

alpha = {}
for letter,card in zip(letters,cards):
    alpha[card]= letter

def pair(hand):
    for i,letter in enumerate(cards):
        if hand.count(letter)>=2:
            return True
    return False

def two_pair(hand):
    count = 0
    for i,letter in enumerate(cards):
        if hand.count(letter)>=2:
            count+=1
    return count==2

def three_of_a_kind(hand):
    for i,letter in enumerate(cards):
        if hand.count(letter)>=3:
            return True
    return False

def full_house(hand):
    count = np.zeros(13)
    for i,letter in enumerate(cards):
        count[i] = hand.count(letter)
    return 2 in count and 3 in count

def four_of_a_kind(hand):
    for i,letter in enumerate(cards):
        if hand.count(letter)>=4:
            return True
    return False

def five_of_a_kind(hand):
    for i,letter in enumerate(cards):
        if hand.count(letter)==5:
            return True
    return False

def get_power(hand):
    power = 0
    if pair(hand): power = 1
    if two_pair(hand): power = 2
    if three_of_a_kind(hand): power = 3
    if full_house(hand): power = 4
    if four_of_a_kind(hand): power = 5
    if five_of_a_kind(hand): power = 6
    return power

def iterate_jokers(hand,power):
    if 'J' in hand:
        for card in cards[1:]:
            power = iterate_jokers(hand.replace('J',card,1),power)
    return max(power, get_power(hand))

hands = []
for hand,bid in data:
    power = iterate_jokers(hand,get_power(hand))
    abc = u.concatenate([alpha[card] for card in hand])
    hands.append((hand,bid,power,abc))

hands_sorted = sorted(hands,key= lambda x : (x[2],x[3]))
sol1 = sum([int(hand[1])*(i+1) for i,hand in enumerate(hands_sorted)])

print(f'sol1 : {sol1}')

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456