Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable b : V.
  Variable P : V -> Prop.  
  Hypothesis H1 : forall x : V, P x <-> x = b.
  Lemma ASSG2B_5 : P b /\ forall x y : V, P x /\ P y -> x = y.
  Proof.
    split.
    pose (H2 := H1 b).
    apply H2.
    reflexivity.
    
    intro c.
    intro d.
    intro H2.
    destruct H2 as [H2 H3].
    apply H1 in H2.
    apply H1 in H3.
    rewrite -> H3.
    exact H2.
  Qed.
  
