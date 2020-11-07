Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q : V -> Prop.
  Hypothesis H1 : forall x : V, P x -> Q x.
  Lemma ASSG2B_12 : (forall x : V, ~ Q x) -> (forall x : V, ~ P x).
  Proof.
    unfold not.
    intros H2 a.
    pose (H3 := H1 a).
    pose (H4 := H2 a).
    intro H5.
    apply H3 in H5.
    apply H4 in H5.
    elim H5.
  Qed.
  
