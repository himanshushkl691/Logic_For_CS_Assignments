Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable b : V.
  Variable Q : V -> (V -> Prop).
  Variable S : V -> V.
  Hypothesis H1 : forall y : V, Q b y.
  Hypothesis H2 : forall x y : V, Q x y -> Q (S x) (S y).
  Lemma ASSG2B_6 : exists z : V, Q b z /\ Q z (S b).
  Proof.
    exists (S b).
    split.
    pose (H3 := H1 (S b)).
    exact H3.
    pose (H3 := H1 b).
    pose (H4 := H2 b).
    pose (H5 := H4 b).
    apply H5.
    exact H3.
  Qed.
  
