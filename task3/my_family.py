
% CCS 2226 - Foundation of AI
% Task 3 - My Own Family Tree
% Author: mobiuskyle

%  GRANDPARENTS
parent(dennis, moses).
parent(tunai, moses).
parent(rueben, ann).
parent(lucy, ann).

% --- PARENTS & CHILDREN ---
parent(moses, mobius).
parent(ann, mobius).
parent(moses, lucas).
parent(ann, lucas).

%  UNCLES & AUNTS (siblings of your parents)
parent(dennis, uncle_james).
parent(tunai, uncle_john).
parent(rueben, aunt_sophia).
parent(lucy, aunt_agatha).

%  COUSINS (children of uncles/aunts) 
parent(uncle_james, cousin_jack).
parent(uncle_john, cousin_yvonne).
parent(aunt_sophia, cousin_jody).

%  RULES (same as before) 
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
cousin(X, Y) :- parent(PX, X), parent(PY, Y), sibling(PX, PY).
uncle_or_aunt(X, Y) :- sibling(X, P), parent(P, Y).
grandchild(X, Z) :- grandparent(Z, X).