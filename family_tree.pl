% Facts
parent(john, mary).
parent(mary, susan).
parent(mary, tom).
parent(susan, emily).

male(john).
male(tom).
female(mary).
female(susan).
female(emily).

% Rules
ancestor(X, Y) :- parent(X, Y).              % Rule 1: Direct parent
ancestor(X,Y):- ancestor(Z,Y),parent(X,Z).

% Modus Ponens
% If someone is a parent, they are also an ancestor.
parent_to_ancestor :- parent(X, Y) -> ancestor(X, Y).
