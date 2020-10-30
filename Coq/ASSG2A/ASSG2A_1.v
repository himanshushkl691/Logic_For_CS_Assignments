Section Prop_Logic_Assg2A.

(* {} |- (p&(q|r)) <=> ((p&q)|(p&r)) *)
Variable P Q R : Prop.
Lemma ASSG2A_1 : P /\ (Q \/ R) <-> (P /\ Q) \/ (P /\ R).
Proof.
  split.
(*   P&(Q|R) -> (P&Q)|(P&R) *)
  intro H1.
  destruct H1 as [H1 H2].
  case H2.
  intro H3.
  left.
  split.
  exact H1.
  exact H3.
  intro H3.
  right.
  split.
  exact H1.
  exact H3.
(* (P&Q)|(P&R) -> P&(Q|R) *)
  intro H1.
  split.
  case H1.
  intro H2.
  destruct H2 as [H2 H3].
  exact H2.
  intro H2.
  destruct H2 as [H2 H3].
  exact H2.
  case H1.
  intro H2.
  destruct H2 as [H2 H3].
  left.
  exact H3.
  intro H2.
  destruct H2 as [H2 H3].
  right.
  exact H3.
Qed.