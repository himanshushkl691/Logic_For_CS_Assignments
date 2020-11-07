Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable S : V -> (V -> Prop).
  Hypothesis H1 : forall x y z : V, S x y /\ S y z -> S x z.
  Hypothesis H2 : forall x : V, ~ S x x.
  Lemma ASSG2B_7 : forall x y : V, S x y -> ~ S y x.
  Proof.
    intros a b.
    unfold not.
    unfold not in H2.
    intros H3 H4.
    pose (H5 := H1 a).
    pose (H6 := H5 b).
    pose (H7 := H6 a).
    pose (H8 := H2 a).
    apply H8.
    apply H7.
    split.
    exact H3.
    exact H4.
  Qed.
  
