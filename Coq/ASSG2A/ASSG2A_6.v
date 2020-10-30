Section Prop_Logic_Assg2A.
(* {q} |- (p&q)|(~p|q) *)
Variable P Q : Prop.
Hypothesis H1 : Q.
Lemma ASSG2A_6 : (P /\ Q) \/ (~P \/ Q).
Proof.
  right.
  right.
  exact H1.
Qed.