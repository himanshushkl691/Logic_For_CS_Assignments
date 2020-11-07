Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q R : V -> Prop.
  Hypothesis H1 : exists x : V, P x /\ Q x.
  Hypothesis H2 : forall x : V, P x -> R x.
  Lemma ASSG2B_11 : exists x : V, R x /\ Q x.
  Proof.
    destruct H1 as [a H3].
    destruct H3 as [H3 H4].
    pose (H5 := H2 a).
    apply H5 in H3 as H6.
    exists a.
    split.
    exact H6.
    exact H4.
  Qed.
  
