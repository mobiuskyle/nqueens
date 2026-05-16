
% CCS 2226 - Foundation of AI
% Task 3 - Family Tree in Prolog
% Author: mobiuskyle


% FACTS: parent(Parent, Child)
parent(george, john).
parent(george, mary).
parent(martha, john).
parent(martha, mary).
parent(john, peter).
parent(john, susan).
parent(mary, kevin).
parent(mary, lisa).
parent(peter, emma).

% RULES 

% Grandparent rule
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

% Sibling rule (same parent, different person)
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% Cousin rule (parents are siblings)
cousin(X, Y) :-
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY).

% Uncle/Aunt rule
uncle_or_aunt(X, Y) :-
    sibling(X, P),
    parent(P, Y).

% Grandchild rule
grandchild(X, Z) :-
    grandparent(Z, X).