Section Prop_Logic_Assg2A.
(* {} |- (p|(q&r)) <=> ((p|q)&(p|r)) *)
Variable P Q R : Prop.
Lemma ASSG2A_2 : P \/ (Q /\ R) <-> (P \/ Q) /\ (P \/ R).
Proof.
  split.
(* (p|(q&r)) -> ((p|q)&(p|r)) *)
  intro H1.
  split.
  case H1.
  intro H2.
  left.
  exact H2.
  intro H2.
  destruct H2 as [H2 H3].
  right.
  exact H2.
  case H1.
  intro H2.
  left.
  exact H2.
  intro H2.
  destruct H2 as [H2 H3].
  right.
  exact H3.
(* ((p|q)&(p|r)) -> (p|(q&r)) *)
  intro H1.
  destruct H1 as [H1 H2].
  case H2.
  intro H3.
  left.
  exact H3.
  intro H3.
  case H1.
  intro H4.
  left.
  exact H4.
  intro H4.
  right.
  split.
  exact H4.
  exact H3.
Qed.