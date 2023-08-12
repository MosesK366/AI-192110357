forward chaining:-
% Facts
father(john, jim).
father(jim, chris).
mother(lisa, jim).
mother(mary, lisa).

% Rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).
grandfather(X, Y) :- father(X, Z), father(Z, Y).
grandmother(X, Y) :- mother(X, Z), mother(Z, Y).

% Forward Chaining
forward_chaining(X) :- parent(X, Y), write(X), write(' is the parent of '), write(Y), nl, fail.
forward_chaining(X) :- grandfather(X, Y), write(X), write(' is the grandfather of '), write(Y), nl, fail.
forward_chaining(X) :- grandmother(X, Y), write(X), write(' is the grandmother of '), write(Y), nl, fail.

% Query
:- forward_chaining(_).

backward chaining:-
% Facts
father(john, jim).
father(jim, chris).
mother(lisa, jim).
mother(mary, lisa).

% Rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).
grandfather(X, Y) :- father(X, Z), father(Z, Y).
grandmother(X, Y) :- mother(X, Z), mother(Z, Y).
% Backward Chaining
backward_chaining(X) :- grandfather(X, Y), write(X), write(' is the grandfather of '), write(Y), nl, !.
backward_chaining(X) :- grandmother(X, Y), write(X), write(' is the grandmother of '), write(Y), nl, !.
backward_chaining(X) :- parent(X, Y), write(X), write(' is the parent of '), write(Y), nl, !.
% Query
:- backward_chaining(chris).
