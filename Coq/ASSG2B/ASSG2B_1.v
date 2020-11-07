Section Pred_Logic_Assg2b.
  Variable V : Set.
  Variable P Q : V -> Prop.
  Hypothesis H1 : forall x : V, P x -> Q x.
  Hypothesis H2 : exists x : V, P x.
  Lemma ASSG2B_1 : exists x : V, Q x.
  Proof.
    destruct H2 as [a H3].
    exists a.
    pose (H4 := H1 a).
    apply H4.
    exact H3.
  Qed.
