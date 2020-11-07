Section Prop_Logic_Assg2A.

(* {P|(P&Q)} |- P *)
Variable P Q : Prop.
Hypothesis H1 : P \/ (P /\ Q).
Lemma ASSG2A_3 : P.
Proof.
  case H1.
  intro H2.
  exact H2.
  intro H2.
  destruct H2 as [H2 H3].
  exact H2.
Qed.