Section Prop_Logic_Assg2A.

(* {p->(q|r),~q,~r} |- ~p *)
Variable P Q R : Prop.
Hypothesis H1 : P -> (Q \/ R).
Hypothesis H2 : ~Q.
Hypothesis H3 : ~R.
Lemma ASSG2A_4 : ~P.
Proof.
  unfold not.
  unfold not in H2.
  unfold not in H3.
  intro H4.
  apply H1 in H4.
  case H4.
  intro H5.
  apply H2 in H5.
  exact H5.
  intro H5.
  apply H3 in H5.
  exact H5.
Qed.