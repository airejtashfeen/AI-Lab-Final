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

% Brotherhood relationship
brother(X, Y) :-
    parent(P, X),     % X and Y share the same parent P
    parent(P, Y),     % X and Y are siblings
    male(X),          % X is male
    X\=Y           % X and Y are not the same person

% Uncle relationship
uncle(Uncle, Person) :-
    parent(Parent, Person),  % Find the parent of the person
    brother(Uncle, Parent).  % Check if someone is a brother of that parent

