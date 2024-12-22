parent(albert,bob).

parent(albert, betsy).

parent(albert, bill).


parent(alice, betsy).

parent(alice, bob).

parent(albert, bill).

parent(bob, carl).
parent(bob, charlie).

teacher(albert).
teacher(alice).



get_all_grandChildren:-
    findall(Y, (parent(X,Y), parent(albert,X)), Grandchildren)
    write('Alberts grandchildren are: '), write(Grandchildren), nl.

