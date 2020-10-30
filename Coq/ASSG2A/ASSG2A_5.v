Section Prop_Logic_Assg2A.
(* {} |- ~p->(p->(p->q)) *)
Variable P Q : Prop.
Lemma ASSG2A_5 : ~P->(P->(P->Q)).
Proof.
  intro H1.
  unfold not in H1.
  intro H2.
  intro H3.
  apply H1 in H3.
  elim H3.
Qed.