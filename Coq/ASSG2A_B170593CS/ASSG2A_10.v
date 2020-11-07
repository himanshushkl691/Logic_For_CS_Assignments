Section Prop_Logic_Assg2A.
(* {} |- ((p->q)&(q->p))->((p|q)->(p&q)) *)
Variable P Q : Prop.
Lemma ASSG2A_10 : ((P -> Q) /\ (Q -> P))->((P \/ Q) -> (P /\ Q)).
Proof.
  intro H1.
  destruct H1 as [H1 H2].
  intro H3.
  split.
  case H3.
  intro H4.
  exact H4.
  exact H2.
  case H3.
  exact H1.
  intro H4.
  exact H4.
Qed.