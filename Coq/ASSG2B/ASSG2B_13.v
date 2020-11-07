Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q : V -> Prop.
  Hypothesis H1 : forall x : V, P x -> ~ Q x.
  Lemma ASSG2B_13 : ~ exists x : V, P x /\ Q x.
  Proof.
    intro H2.
    destruct H2 as [a H2].
    destruct H2 as [H2 H3].
    pose (H4 := H1 a).
    apply H4 in H2.
    unfold not in H2.
    apply H2.
    exact H3.
  Qed.
  
