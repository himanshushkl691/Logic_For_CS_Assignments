Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q : V -> Prop.
  Hypothesis H1 : exists x,  P x.
  Hypothesis H2 : forall x y : V,  P x -> Q y.
  Lemma ASSG2B_3 : forall y : V,  Q y.
  Proof.
    intro b.
    destruct H1 as [a H3].
    pose (H4 := H2 a).
    pose (H5 := H4 b).
    apply H5.
    exact H3.
  Qed.
  
