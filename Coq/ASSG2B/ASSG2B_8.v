Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q R : V -> Prop.
  Hypothesis H1 : forall x : V, P x \/ Q x.
  Hypothesis H2 : exists x : V, ~ Q x.
  Hypothesis H3 : forall x : V, R x -> ~ P x.
  Lemma ASSG2B_8 : exists x : V, ~ R x.
  Proof.
    unfold not.
    unfold not in H2.
    unfold not in H3.
    destruct H2 as [a H4].
    pose (H5 := H1 a).
    pose (H6 := H3 a).
    exists a.
    intro H7.
    apply H6.
    exact H7.
    destruct H5 as [H5_i | H5_ii].
    + exact H5_i.
    + apply H4 in H5_ii.
      elim H5_ii.
  Qed.
  
